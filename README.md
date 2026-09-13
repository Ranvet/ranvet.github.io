# Ranveer Tiwari — personal website

Primary address: https://ranveertiwari.com/

Research: https://ranveertiwari.com/research/

Publications: https://ranveertiwari.com/publications/

Writing: https://ranveertiwari.com/writing/

Hosting repository: https://github.com/Ranvet/ranvet.github.io. The custom address requires the DNS and HTTPS checks described below; the domain registration alone does not connect the website.

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
- `CNAME`: the primary custom domain, `ranveertiwari.com`.

## Publish

1. Reuse the existing **Ranvet/ranvet.github.io** repository and authenticated GitHub connection. Do not recreate the repository or repeat onboarding.
2. Validate changes, commit only the intended files, and push to `main`.
3. Keep **Settings → Pages** configured for **Deploy from a branch**, **main**, **/(root)**, with custom domain `ranveertiwari.com`.
4. Wait for the Pages deployment matching the pushed commit to complete.
5. After DNS and HTTPS are ready, open https://ranveertiwari.com/ and test Research, Publications, Writing, profile links, and the About/Connect homepage anchors.

This uses GitHub Pages for a public repository. The separately registered domain does not require purchasing hosting or a website builder. GitHub documents eligibility and setup at https://docs.github.com/en/pages/quickstart.

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

## Personal domain and DNS

The primary domain is `ranveertiwari.com`, registered at Spaceship in the owner's account. Keep the existing Spaceship nameservers. GitHub account-level ownership verification was confirmed on 2026-09-13; retain its `_github-pages-challenge-Ranvet` TXT record in DNS. Its value is deliberately not stored in this repository.

Configure the repository custom domain before pointing DNS to GitHub Pages. The required web-routing records are:

| Host | Type | Value |
| --- | --- | --- |
| `@` | A | `185.199.108.153` |
| `@` | A | `185.199.109.153` |
| `@` | A | `185.199.110.153` |
| `@` | A | `185.199.111.153` |
| `www` | CNAME | `ranvet.github.io` |

Use the registrar's default TTL. Do not add wildcard records. Inspect conflicting apex or `www` routing records before changing them, and preserve unrelated TXT/MX records. Domain verification is not proof that these routing records are saved or that HTTPS is ready. Verify public DNS, the Pages certificate, and **Enforce HTTPS** before reporting the custom address as live. Once both names are configured, GitHub Pages redirects `www` to the primary apex domain; also verify the existing `ranvet.github.io` address redirects correctly.

The `CNAME` file, page canonical/Open Graph URLs, Person schema URL, `robots.txt`, and `sitemap.xml` use the custom domain. If changing hosts or domains later, update these together. Follow current GitHub guidance at https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site.

Keep a local copy of this repository. The content and layout can be moved to another static host; the free `github.io` address itself is provided by GitHub and is not an independently registered domain.
