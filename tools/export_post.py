#!/usr/bin/env python3
"""Derive the Markdown, static figures and PDF of a hand-written blog post.

    python3 tools/export_post.py sd-or-se

blog/<slug>/index.html is the source. The script writes, next to it:

  fig<N>.svg     each <svg id="fig<N>"> as the page's scripts draw it, made standalone
                 (light theme), for the Markdown version;
  index.md       the post body between <!--md-body--> and <!--/md-body-->, converted with
                 pandoc. Regions between <!--md-skip--> and <!--/md-skip--> are left out,
                 and each <!--md-fig figN--> … <!--/md-fig--> figure becomes an image
                 plus its caption;
  <slug>.pdf     the page printed by headless Chrome (A4, the page's print stylesheet).

It also copies index.md into the page's <textarea id="pt-md">, which "Copy as Markdown"
falls back on when index.md cannot be fetched. Running it twice gives the same files.
Needs Google Chrome and pandoc.
"""
import html
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = os.environ.get('CHROME', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
SITE = 'https://selcukorkmaz.github.io/blog/'

# Classes the figure scripts use (the same rules as in the posts' own CSS).
SVG_CLASSES = '''text{font-family:"IBM Plex Sans","Helvetica Neue",Arial,sans-serif}
.t-ink{fill:var(--ink)} .t-2{fill:var(--ink-2)} .t-mu{fill:var(--muted)}
.grid{stroke:var(--rule);stroke-width:1} .axis{stroke:var(--muted);stroke-width:1}'''


def light_tokens(page):
    """The light-theme custom properties: every top-level `:root{...}` rule, later ones winning."""
    tokens = {}
    for block in re.findall(r'(?m)^:root\{([^}]*)\}', page):
        for name, value in re.findall(r'(--[\w-]+)\s*:\s*([^;]+)', block):
            tokens[name] = value.strip()
    return ';'.join('%s:%s' % kv for kv in tokens.items())


def chrome(*args):
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
                    '--hide-scrollbars', '--virtual-time-budget=15000', *args],
                   check=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)


def rendered_dom(path):
    out = subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
                          '--virtual-time-budget=15000', '--dump-dom', 'file://' + path],
                         check=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    return out.stdout.decode('utf-8')


def write_if_changed(path, data):
    raw = data if isinstance(data, bytes) else data.encode('utf-8')
    if os.path.exists(path):
        with open(path, 'rb') as f:
            if f.read() == raw:
                return False
    with open(path, 'wb') as f:
        f.write(raw)
    return True


def main(slug):
    folder = os.path.join(ROOT, 'blog', slug)
    page_path = os.path.join(folder, 'index.html')
    page = open(page_path, encoding='utf-8').read()
    url = SITE + slug + '/'

    # ---------- figures: the SVGs as the scripts drew them ----------
    dom = rendered_dom(page_path)
    style = '<style>\nsvg{%s;background:#ffffff}\n%s\n</style>' % (light_tokens(page), SVG_CLASSES)
    figs = {}
    for fid, attrs, inner in re.findall(r'<svg id="(fig\d+)"([^>]*)>(.*?)</svg>', dom, re.S):
        vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', attrs)
        lab = re.search(r'aria-label="([^"]*)"', attrs)
        label = html.unescape(lab.group(1)) if lab else fid
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="%s" height="%s" viewBox="0 0 %s %s" role="img" aria-label="%s">\n%s\n%s\n</svg>\n'
               % (vb.group(1), vb.group(2), vb.group(1), vb.group(2), html.escape(label), style, inner))
        write_if_changed(os.path.join(folder, fid + '.svg'), svg)
        figs[fid] = label

    # ---------- Markdown ----------
    body = re.search(r'<!--md-body-->(.*?)<!--/md-body-->', page, re.S).group(1)
    body = re.sub(r'<!--md-skip-->.*?<!--/md-skip-->', '', body, flags=re.S)

    def figure(m):
        fid, block = m.group(1), m.group(2)
        cap = re.search(r'<figcaption>(.*?)</figcaption>', block, re.S)
        alt = re.sub(r'^Figure \d+\.\s*', '', figs.get(fid, fid))
        img = '<p><img src="%s%s.svg" alt="%s"></p>' % (url, fid, html.escape(alt))
        return img + ('\n<p>%s</p>' % cap.group(1).strip() if cap else '')
    body = re.sub(r'<!--md-fig (fig\d+)-->(.*?)<!--/md-fig-->', figure, body, flags=re.S)
    body = re.sub(r'<sup class="cite">(.*?)</sup>', lambda m: re.sub(r'<[^>]+>', '', m.group(1)), body)
    body = re.sub(r'<span class="n">([\d.]+)</span>', r'\1 ', body)
    body = re.sub(r'<span class="m">(.*?)</span>', r'<code>\1</code>', body)
    body = re.sub(r'<span class="nw">(.*?)</span>', r'\1', body)
    body = re.sub(r'</?section[^>]*>', '', body)
    body = re.sub(r'<li id="[^"]*">', '<li>', body)
    # Table captions become a paragraph above the table (pandoc would drop the markup).
    body = re.sub(r'<div class="tw"><table>\s*<caption>(.*?)</caption>', r'<p>\1</p>\n<table>', body, flags=re.S)
    body = body.replace('</table></div>', '</table>')
    body = re.sub(r'<div class="(box|kw)">(.*?)</div>', r'<p>\2</p>', body, flags=re.S)
    body = re.sub(r'<div class="eq">(.*?)</div>',
                  lambda m: re.sub(r'<span>(.*?)</span>', r'<p>\1</p>', m.group(1)), body, flags=re.S)
    # Code: drop the highlighting spans; a class on <pre> (e.g. "r") becomes the fence language.
    body = re.sub(r'<pre([^>]*)><code>(.*?)</code></pre>',
                  lambda m: '<pre%s><code>%s</code></pre>' % (m.group(1), re.sub(r'<[^>]+>', '', m.group(2))), body, flags=re.S)
    # gfm keeps <sub>/<sup> as HTML, which GitHub and most Markdown viewers render.
    md = subprocess.run(['pandoc', '-f', 'html', '-t', 'gfm', '--wrap=none'],
                        input=body.encode('utf-8'), check=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
    md = re.sub(r'\n{3,}', '\n\n', md).strip() + '\n'

    # Header: title (and subtitle, if the <h1> has a <span>), kicker, source line, byline.
    text = lambda frag: html.unescape(re.sub(r'<[^>]+>', '', frag)).strip()
    h1 = re.search(r'<h1>(.*?)</h1>', page, re.S).group(1)
    sub = re.search(r'<span>(.*?)</span>', h1, re.S)
    kicker = re.search(r'<div class="kicker">(.*?)</div>', page, re.S)
    byline = re.search(r'<div class="byline">(.*?)<small>(.*?)</small>', page, re.S)
    author, date_h = (text(byline.group(1)), text(byline.group(2))) if byline else ('', '')
    head = '# %s\n\n' % text(re.sub(r'<span>.*?</span>', '', h1, flags=re.S))
    if sub:
        head += '*%s*\n\n' % text(sub.group(1))
    if kicker:
        head += '%s\n\n' % text(kicker.group(1))
    head += '> Source: %s%s\n\n' % (url, ' · ' + date_h if date_h else '')
    if author:
        head += '%s\\\n%s\n\n' % (author, date_h)
    md = head + md
    changed_md = write_if_changed(os.path.join(folder, 'index.md'), md)

    # The embedded copy used when index.md cannot be fetched (file:// or offline).
    new_page = re.sub(r'(<textarea id="pt-md"[^>]*>).*?(</textarea>)',
                      lambda m: m.group(1) + html.escape(md, quote=False) + m.group(2), page, flags=re.S)
    changed_page = write_if_changed(page_path, new_page)

    # ---------- PDF ----------
    pdf = os.path.join(folder, slug + '.pdf')
    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, 'out.pdf')
        chrome('--no-pdf-header-footer', '--print-to-pdf=' + out, 'file://' + page_path)
        data = open(out, 'rb').read()
    # Chrome stamps creation dates into the PDF, and its tagged-PDF structure elements carry internal
    # node numbers (/ID (node…)) that depend on script timing; rewrite only when anything else changed.
    strip = lambda b: re.sub(rb'/ID \(node\d+\)', b'', re.sub(rb'/(CreationDate|ModDate) \(D:[^)]*\)', b'', b))
    if not (os.path.exists(pdf) and strip(open(pdf, 'rb').read()) == strip(data)):
        open(pdf, 'wb').write(data)

    words = len(re.sub(r'\(https?://[^)]*\)', '', md).split())
    print(json.dumps({'figures': sorted(figs), 'index.md changed': changed_md, 'index.html changed': changed_page,
                      'words': words, 'reading time (min, 245 wpm)': round(words / 245)}, indent=2))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('usage: python3 tools/export_post.py <slug>')
    main(sys.argv[1])
