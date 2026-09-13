"""Build the static writing archive from verified metadata. No dependencies."""
import json
from datetime import date
from html import escape
from pathlib import Path
from string import Template
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "data/articles.json").read_text())
ARTICLES = DATA["articles"]
TOPICS = {
    "Security & IAM", "Audit & Observability", "Integration & Extensibility",
    "Applied AI", "Network Architecture",
}


def date_label(value):
    parsed = date.fromisoformat(value)
    return f"{parsed.day} {parsed.strftime('%b %Y')}"


def entry(article):
    title, url, published, publisher, topic, summary = (
        escape(article[key]) for key in ("title", "url", "date", "publisher", "topic", "summary")
    )
    authors = ", ".join(escape(author) for author in article["authors"])
    return f"""
        <article class="archive-entry" data-year="{published[:4]}" data-topic="{topic}">
          <time datetime="{published}">{date_label(published)}</time>
          <div>
            <div class="entry-meta"><span class="topic-tag">{topic}</span><span class="entry-publisher">{publisher}</span></div>
            <h3><a href="{url}">{title}</a></h3>
            <p class="entry-summary">{summary}</p>
            <p class="byline">{authors}</p>
          </div>
        </article>"""


def build():
    assert ARTICLES, "No articles"
    assert len({a["url"] for a in ARTICLES}) == len(ARTICLES), "Duplicate URLs"
    for article in ARTICLES:
        for key in ("title", "url", "date", "publisher", "topic", "summary"):
            assert article[key], f"Missing {key}"
        date.fromisoformat(article["date"])
        url = urlsplit(article["url"])
        assert url.scheme == "https"
        assert url.netloc in ("www.ateam-oracle.com", "blogs.oracle.com")
        assert "Ranveer Tiwari" in article["authors"], "Unverified authorship"
        assert article["topic"] in TOPICS, "Unknown topic"
    ordered = sorted(ARTICLES, key=lambda a: (-date.fromisoformat(a["date"]).toordinal(), a["title"]))
    years = sorted({a["date"][:4] for a in ordered}, reverse=True)
    topics = sorted({a["topic"] for a in ordered})
    groups = []
    for year in years:
        articles = [a for a in ordered if a["date"].startswith(year)]
        groups.append(f"""
      <section class="year-group" aria-labelledby="year-{year}">
        <div class="year-heading"><h2 id="year-{year}">{year}</h2><span class="year-count">{len(articles)} articles</span></div>
        {''.join(entry(a) for a in articles)}
      </section>""")
    template = Template((ROOT / "templates/writing.html").read_text())
    output = template.substitute(
        count=len(ordered), first_year=years[-1], last_year=years[0],
        topics="".join(f'<option value="{escape(t)}">{escape(t)}</option>' for t in topics),
        years="".join(f"<option>{y}</option>" for y in years),
        groups="".join(groups),
        coverage=escape(DATA["coverage_note"]),
        checked=date_label(DATA["verified_on"]),
    )
    (ROOT / "writing").mkdir(exist_ok=True)
    output = "\n".join(line.rstrip() for line in output.splitlines()) + "\n"
    (ROOT / "writing/index.html").write_text(output)
    print(f"Built {len(ordered)} articles across {len(years)} years and {len(topics)} topics.")


if __name__ == "__main__":
    build()
