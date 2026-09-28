
# Personal Academic Website for Selçuk Korkmaz
Plain static HTML, CSS and JavaScript served by GitHub Pages (https://selcukorkmaz.github.io/).
There is no build step for the site itself.

## Blog

The blog lives in `blog/`:

- `blog/index.html` is the list of posts.
- Each post has its own folder, `blog/<slug>/index.html`, so its address is
  `https://selcukorkmaz.github.io/blog/<slug>/`.

### Adding a post

1. Create `blog/<slug>/index.html` (lower-case words joined by hyphens, e.g.
   `blog/my-new-paper/index.html`). Inside the post, link to the home page as `../../`
   and to the post list as `../`. Reuse the site's theme mechanism: the choice is stored
   in `localStorage` under the key `theme` (`"light"` or `"dark"`) and applied as the
   class `light`/`dark` on `<html>`; paper-style posts also set `data-theme` on `<html>`,
   which their CSS reads.
2. In `blog/index.html`, copy one whole `<article class="card post"> … </article>` block,
   paste it at the top of the list (newest first), and change the link (`<slug>/`, with the
   trailing slash), the title, the `<time datetime="YYYY-MM-DD">` date, the reading time,
   the summary and the tags. The comment above the list repeats these steps. The card's
   "Share" menu (share links and BibTeX/APA citations) is built from those fields.
3. Commit and push; GitHub Pages publishes the change.

### Posts generated from a paper

`blog/leakage-defence-in-layers/` is generated, not hand-written. Everything in that
folder (`index.html`, `index.md`, `leakage-defence-in-layers.pdf`, `fig*.png`, `fig*.svg`)
is produced by `export_blog.py`, kept next to the paper source `leakage-defence.html`.
Do not edit these files by hand; revise the paper and re-run:

```sh
python3 export_blog.py      # needs Google Chrome for the Markdown and PDF steps
```

The script wraps the paper in a full page, adds the site bar, the post tools (PDF,
Markdown, Cite, Share, Translate) and the comments section, renders the page with
headless Chrome to build `index.md`, and prints the PDF. Running it twice gives identical
files. It prints the reading time; update the post's card in `blog/index.html` if that
changes.

### Hand-written posts

`blog/sd-or-se/` is written by hand: `index.html` is the source, and you edit it directly.
Its companion files (`index.md`, `fig*.svg`, `sd-or-se.pdf`) are derived from it by
`tools/export_post.py`. After editing the page, re-run:

```sh
python3 tools/export_post.py sd-or-se      # needs Google Chrome and pandoc
```

The script renders the page in headless Chrome, saves each `<svg id="figN">` as drawn by
the page's scripts as a standalone `figN.svg`, converts the text between `<!--md-body-->`
and `<!--/md-body-->` to `index.md` with pandoc (leaving out `<!--md-skip-->` regions and
turning each `<!--md-fig figN-->` figure into an image with its caption), copies the
Markdown into the page's `<textarea id="pt-md">` for offline "Copy as Markdown", and prints
the PDF. Running it twice gives the same files. It prints the reading time; update the
post's card in `blog/index.html` if that changes.

The same markers work for a new hand-written post if it follows this post's page structure:
the paper-style tokens on `:root` (the figure SVGs take their light-theme colours from every
top-level `:root{…}` rule), an `<h1>` with an optional `<span>` subtitle, and optionally a
`<div class="kicker">` and a `<div class="byline">Author<small>date</small></div>`. Headless
Chrome does not wait for the Google Fonts, so the PDF is set in the fallback fonts (Georgia,
Helvetica Neue), as the other post's PDF is. The PDF is rewritten only when its content
changes; Chrome's timestamps and internal structure-node numbers are ignored.

### Comments (giscus)

Posts can show comments through [giscus](https://giscus.app), which stores them in
GitHub Discussions of this repository. They stay off, and the post shows "Comments are
coming soon", until a Discussions category is configured. To switch them on:

1. On GitHub, open this repository's **Settings → General → Features** and tick
   **Discussions**.
2. Install the giscus app for this repository: https://github.com/apps/giscus
   ("Only select repositories", then `selcukorkmaz.github.io`).
3. Choose the Discussions category for comments. **Announcements** is a good choice:
   only maintainers and giscus can open new discussions there.
4. Get the category name and id, either
   - from https://giscus.app: enter `selcukorkmaz/selcukorkmaz.github.io`, pick the
     category, and copy `data-category` and `data-category-id` from the generated
     snippet; or
   - with the GitHub CLI:

     ```sh
     gh api graphql -f query='
       query { repository(owner: "selcukorkmaz", name: "selcukorkmaz.github.io") {
         id
         discussionCategories(first: 20) { nodes { name id } } } }'
     ```

     The repository `id` should be `R_kgDOPupOnA`; the category id starts with `DIC_`.
5. Put the two values in the `GISCUS` block near the top of `export_blog.py`
   (`"category": "Announcements"`, `"categoryId": "DIC_…"`) and re-run the script. That
   block becomes the configuration object at the top of the post's script, the only place
   giscus is configured. Commit and push.

The comment box follows the site's light/dark toggle.
