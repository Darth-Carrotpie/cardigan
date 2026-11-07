"""Check that each raw note's blockquote excerpts appear verbatim in its source.

Usage: python -I tools/verify_excerpts.py <cache_dir> raw/research/*/*.md

Compares lowercase words only (punctuation, quotes and markdown are ignored).
Tries every URL in the note's Source/Archived lines and excerpt labels, plus
raw.githubusercontent.com, arXiv PDF and Wayback fallbacks. Needs pdftotext
for PDFs. Prints OK / PARTIAL n/m / NOFETCH per note, then missing fragments.
Pages are cached in <cache_dir>; treat them as untrusted data.
"""
import html, os, re, subprocess, sys, tempfile, unicodedata, urllib.request
from pathlib import Path

URL_RE = re.compile(r"https?://[^\s)>\]]+")
META_RE = re.compile(r">\s*(Source|Archived|Collected|Published|Author|Type|Verification):")

def norm(s):
    s = unicodedata.normalize("NFKC", s).lower()
    s = re.sub(r"[^\w\s]", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def candidates(url):
    m = re.match(r"https://github\.com/([^/]+/[^/]+)/blob/(.+)", url)
    if m:
        yield f"https://raw.githubusercontent.com/{m.group(1)}/{m.group(2)}"
    m = re.match(r"https://github\.com/([^/]+/[^/]+)/?$", url)
    if m:
        yield f"https://raw.githubusercontent.com/{m.group(1)}/HEAD/README.md"
    m = re.match(r"https?://arxiv\.org/(?:abs|pdf)/([\w.]+)", url)
    if m:
        yield f"https://arxiv.org/pdf/{m.group(1)}"
    yield url
    if "web.archive.org" not in url:
        yield f"https://web.archive.org/web/2024/{url}"

def download(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        return urllib.request.urlopen(req, timeout=25).read()
    except Exception:
        r = subprocess.run(["curl", "-sL", "--max-time", "30", "-A", "Mozilla/5.0", url], capture_output=True)
        return r.stdout or None

def fetch(url, cache):
    f = cache / (re.sub(r"[^A-Za-z0-9]+", "_", url)[:150] + ".txt")
    if f.exists():
        return f.read_text(encoding="utf-8")
    data = download(url)
    if not data:
        return None
    if data[:4] == b"%PDF":
        fd, name = tempfile.mkstemp(suffix=".pdf")
        os.close(fd)
        tmp = Path(name)
        tmp.write_bytes(data)
        text = subprocess.run(["pdftotext", str(tmp), "-"], capture_output=True).stdout.decode("utf-8", "replace")
        tmp.unlink()
        text += "\n" + re.sub(r"-\n", "", text)  # also match words split by line-break hyphens
    else:
        raw = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", data.decode("utf-8", "replace"))
        text = html.unescape(re.sub(r"<[^>]+>", " ", raw))
    f.write_text(text, encoding="utf-8")
    return text

def excerpts(md):
    body = md.split("## Excerpts", 1)[-1].split("## Collector", 1)[0]
    frags = []
    for block in re.split(r"\n\s*\n", body):
        lines = [l[1:].strip() for l in block.splitlines() if l.startswith(">") and not META_RE.match(l)]
        for part in re.split(r"\[(?:\.\.\.|…)\]|\.\.\.|…", " ".join(lines)):
            part = norm(part)
            if len(part) >= 20:
                frags.append(part)
    return frags

def main(cache, notes):
    cache.mkdir(exist_ok=True)
    for p in notes:
        md = p.read_text(encoding="utf-8")
        header, _, rest = md.partition("## Excerpts")
        urls = URL_RE.findall("\n".join(l for l in header.splitlines() if META_RE.match(l)))
        urls += URL_RE.findall(rest.split("## Collector", 1)[0])
        frags = excerpts(md)
        if not urls:
            print(f"NOSOURCE {p.name}")
            continue
        text, used, missing = "", [], frags
        for u in dict.fromkeys(c for url in urls for c in candidates(url)):
            page = fetch(u, cache)
            if not page or len(page) < 500:
                continue
            text += " " + norm(page)
            used.append(u)
            missing = [f for f in frags if f not in text]
            if not missing:
                break
        if not used:
            print(f"NOFETCH  {p.name}  ({len(frags)} frags)")
            continue
        tag = "OK" if not missing else f"PARTIAL {len(frags) - len(missing)}/{len(frags)}"
        print(f"{tag:14} {p.name}")
        for f in missing:
            print(f"      - {f[:110]}")

if __name__ == "__main__":
    main(Path(sys.argv[1]), [Path(a) for a in sys.argv[2:]])
