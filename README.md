# Ranveer Tiwari — personal website

Live address: https://ranvet.github.io/

Research: https://ranvet.github.io/research/

Publications: https://ranvet.github.io/publications/

Writing: https://ranvet.github.io/writing/

A small, portable personal site: static HTML and CSS, no third-party runtime dependencies, no trackers, no paid theme, and no external font requests. The homepage introduces Ranveer through his technical interests and four thematic featured groups, with employer affiliation providing context rather than defining the site's identity. Research, Publications, and Writing have separate navigation destinations. The Writing page contains 28 verified technical articles with original summaries and full author credits, grouped by year, with optional local search and topic/year filters. All entries remain readable without JavaScript.

## Files

- `index.html`: person-first introduction, four thematic featured groups, biography, and profile links.
- `research/index.html`: research interests and related technical writing.
- `publications/index.html`: verified published outputs, with precise publication types and attribution.
- `assets/style.css`: responsive layout and print styles.
- `writing/index.html`: generated technical article collection, committed so GitHub Pages can serve it directly.
- `data/articles.json`: verified article metadata and coverage notes.
- `templates/writing.html`: technical article page layout.
- `scripts/build_writing.py`: dependency-free Python 3 generator for the article collection.
- `assets/writing.js`: search and filters; no network calls.
- `assets/favicon.svg`: original text monogram.
- `404.html`: missing-page fallback.
- `robots.txt` and `sitemap.xml`: crawler discovery.
- `.nojekyll`: tells GitHub Pages to serve these files directly.

## Publish

1. Create a **public** repository owned by **Ranvet**, named **ranvet.github.io**. If publishing this existing local repository, do not initialize the remote with a README or license.
2. Push these files to its `main` branch.
3. In **Settings → Pages**, select **Deploy from a branch**, **main**, **/(root)**, then save.
4. Wait for the Pages deployment to complete and open https://ranvet.github.io/.
5. Confirm HTTPS and test Research, Publications, Writing, profile links, and the About/Connect homepage anchors.

This uses GitHub Pages for a public repository; no domain purchase is needed. GitHub documents eligibility and setup at https://docs.github.com/en/pages/quickstart.

## Preview locally

Run a static HTTP server from this directory, for example:

```sh
python3 -m http.server 4000 --bind 127.0.0.1
```

Visit http://127.0.0.1:4000/. Use an HTTP server instead of opening the HTML as a file, because site asset paths start at `/`.

## Edit and add writing

Edit `index.html` directly in GitHub using the pencil button, then commit the change to `main`. GitHub Pages republishes it automatically.

For another technical article entry, add its exact title, original URL, article-displayed ISO date, all byline authors, publisher, primary topic, and short original summary to `data/articles.json`. Update verification and coverage notes as appropriate. Run `python3 scripts/build_writing.py`, then commit both the metadata and generated `writing/index.html`. The four thematic featured groups are maintained separately in `index.html`; update its article-count callout when the collection grows. Navigation order is Research, Publications, Writing, About, Connect. Preserve the active-page marker and use `/#about` and `/#connect` from supporting pages. Do not hand-edit the generated article collection.

Coverage checked on 2026-09-13: all 27 distinct URLs from the earlier public author-profile inventory were verified against public source articles; one additional coauthored July 2026 article was found in A-Team’s Architecture category. Current author-profile pagination could not be completed because its dynamic list was inaccessible. Thus 28 is the verified inventory count, not a guarantee of every current post. External Oracle Cloud Infrastructure Blog entries linked by the author profile are included. Each JSON record retains relevant date corrections or source-verification limitations.

This site is a **portfolio**, not a full blogging CMS. It has no built-in rich-text editor, subscriber list, comments, or newsletter. HTML supports headings, tables, images, links, and code blocks. When adding original long-form posts, a Markdown generator such as Jekyll can be introduced without changing the public address; remove `.nojekyll` if moving to GitHub’s branch-based Jekyll build. Avoid publishing empty placeholder articles.

## Research and publications

The standalone `/research/` page presents stated research interests and related technical writing. The separate `/publications/` page presents verified published outputs. It currently contains one **published patent application**, with the publication identifier, publication date, inventor credits, and a source link. This is not presented as a granted patent, journal article, or conference paper. Technical articles remain available through the Writing page and link to their original Oracle publications.

The public Google Scholar and ORCID profiles were checked on 2026-09-13 and each listed the same patent application, not two distinct outputs. Their presence does not establish a list of peer-reviewed papers. Keep research interests distinct from claims about published results, and verify each new output's type, title, identifier, date, and attribution before adding it. Edit `research/index.html` and `publications/index.html` directly; preserve their separate canonical URLs and keep new local page routes in `sitemap.xml` without inventing update dates.

## Content boundaries

- Technical article entries link to the original public articles; full articles and Oracle images are not copied into this site. Local preservation backups remain separate and are not deployed here.
- Keep original bylines, product-support limitations, source links, and dates. Dates here are the source’s displayed publication dates, not a claim about its most recent revision.
- Confirm applicable publication/reuse permission before republishing employer-owned or jointly authored material.
- LinkedIn, Google Scholar, and ORCID addresses were supplied by the site owner. Public profile records support the identified patent-application entry; no citation counts, academic credentials, peer-reviewed papers, or patent-grant status are inferred.
- Do not commit credentials, customer data, unpublished patent material, or internal work documents.
- No open-source license is selected on the owner’s behalf.

## Add a personal domain later

Register the domain in an account you control, configure it in **Settings → Pages**, and follow GitHub’s current DNS and domain-verification instructions. Then update the canonical URL, Open Graph URL, Person schema URL, `robots.txt`, and `sitemap.xml`. No custom domain or `CNAME` file is configured in this version.

Keep a local copy of this repository. The content and layout can be moved to another static host; the free `github.io` address itself is provided by GitHub and is not an independently registered domain.
