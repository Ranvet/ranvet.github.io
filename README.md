# Ranveer Tiwari — personal website

Live address: https://ranvet.github.io/

Writing archive: https://ranvet.github.io/writing/

A small, portable personal site: static HTML and CSS, no third-party runtime dependencies, no trackers, no paid theme, and no external font requests. The homepage presents six selected articles. The writing archive contains 28 verified articles with original summaries and full author credits, grouped by year, with optional local search and topic/year filters. All entries remain readable without JavaScript.

## Files

- `index.html`: homepage, biography, article entries, and profile links.
- `assets/style.css`: responsive layout and print styles.
- `writing/index.html`: generated archive, committed so GitHub Pages can serve it directly.
- `data/articles.json`: verified article metadata and coverage notes.
- `templates/writing.html`: archive page layout.
- `scripts/build_writing.py`: dependency-free Python 3 archive generator.
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
5. Confirm HTTPS and test the writing/profile links.

This uses GitHub Pages for a public repository; no domain purchase is needed. GitHub documents eligibility and setup at https://docs.github.com/en/pages/quickstart.

## Preview locally

Run a static HTTP server from this directory, for example:

```sh
python3 -m http.server 4000 --bind 127.0.0.1
```

Visit http://127.0.0.1:4000/. Use an HTTP server instead of opening the HTML as a file, because site asset paths start at `/`.

## Edit and add writing

Edit `index.html` directly in GitHub using the pencil button, then commit the change to `main`. GitHub Pages republishes it automatically.

For another archive entry, add its exact title, original URL, article-displayed ISO date, all byline authors, publisher, primary topic, and short original summary to `data/articles.json`. Update verification and coverage notes as appropriate. Run `python3 scripts/build_writing.py`, then commit both the metadata and generated `writing/index.html`. The homepage selection is maintained separately in `index.html`; update its article-count callout when the archive grows. Do not hand-edit the generated archive.

Coverage checked on 2026-09-13: all 27 distinct URLs from the earlier public author-profile inventory were verified against public source articles; one additional coauthored July 2026 article was found in A-Team’s Architecture category. Current author-profile pagination could not be completed because its dynamic list was inaccessible. Thus 28 is the verified inventory count, not a guarantee of every current post. External Oracle Cloud Infrastructure Blog entries linked by the author profile are included. Each JSON record retains relevant date corrections or source-verification limitations.

This first version is a **portfolio**, not a full blogging CMS. It has no built-in rich-text editor, subscriber list, comments, or newsletter. HTML supports headings, tables, images, links, and code blocks. When adding original long-form posts, a Markdown generator such as Jekyll can be introduced without changing the public address; remove `.nojekyll` if moving to GitHub’s branch-based Jekyll build. Avoid publishing empty placeholder articles.

## Content boundaries

- All entries link to the original public articles; full articles and Oracle images are not copied.
- Keep original bylines, product-support limitations, source links, and dates. Dates here are the source’s displayed publication dates, not a claim about its most recent revision.
- Confirm applicable publication/reuse permission before republishing employer-owned or jointly authored material.
- LinkedIn, Google Scholar, and ORCID addresses were supplied by the site owner; no citation counts, credentials, or research-publication claims are inferred.
- Do not commit credentials, customer data, unpublished patent material, or internal work documents.
- No open-source license is selected on the owner’s behalf.

## Add a personal domain later

Register the domain in an account you control, configure it in **Settings → Pages**, and follow GitHub’s current DNS and domain-verification instructions. Then update the canonical URL, Open Graph URL, Person schema URL, `robots.txt`, and `sitemap.xml`. No custom domain or `CNAME` file is configured in this version.

Keep a local copy of this repository. The content and layout can be moved to another static host; the free `github.io` address itself is provided by GitHub and is not an independently registered domain.
