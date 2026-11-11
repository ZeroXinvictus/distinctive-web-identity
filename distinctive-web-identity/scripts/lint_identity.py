#!/usr/bin/env python3
"""Cek cepat apakah sebuah proyek web masih "generik" atau melanggar aturan identitas.

Pakai:  python scripts/lint_identity.py <folder-proyek> [--tokens path/ke/tokens.css]

Yang dicek (semua deterministik, jadi hasilnya bisa dipercaya dan diulang):
  1. Token default dari assets/tokens.css belum diganti (font Inter + biru #3d7bff = resep generik).
  2. Warna hex / radius px yang di-hardcode di komponen, di luar file token.
  3. Headline/copy generik dan klaim yang kelihatan palsu (user count, "trusted by", dst).
  4. Fondasi accessibility: focus-visible dan prefers-reduced-motion hilang.

Exit code 0 kalau tidak ada temuan "high", 1 kalau ada. Ini alat bantu, bukan pengganti penilaian:
temuan "med/low" perlu dilihat konteksnya dulu.
"""
import argparse
import re
import sys
from pathlib import Path

SRC_EXT = {".css", ".scss", ".html", ".htm", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".astro", ".mdx"}
SKIP_DIRS = {"node_modules", ".next", "dist", "build", ".git", ".vercel", "out", "coverage"}

DEFAULT_MARKERS = {
    "#3d7bff": "primary biru default dari scaffold",
    "#2fd6a0": "accent hijau default dari scaffold",
    "#0b0d10": "background default dari scaffold",
    '"inter tight"': "font display default dari scaffold",
}

GENERIC_COPY = [
    r"revolutioni[sz]e", r"next[- ]generation", r"powering the future", r"build something amazing",
    r"unlock (the )?(power|your potential)", r"your success starts here", r"cutting[- ]edge",
    r"seamless(ly)?", r"ai[- ]powered", r"take (it|your \w+) to the next level", r"all[- ]in[- ]one solution",
]
FAKE_CLAIMS = [
    r"\b\d{1,3}(,\d{3})+\+?\s*(users|customers|clients|pengguna|downloads)",
    r"\b\d+(\.\d+)?[kKmM]\+\s*(users|customers|clients|pengguna)",
    r"trusted by\s+(thousands|millions|\d+)", r"dipercaya\s+(ribuan|jutaan|\d+)",
    r"\b(5|4\.9)/5\s*(rating|stars)?", r"lorem ipsum",
]
HEX = re.compile(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b")
RADIUS_PX = re.compile(r"border-radius\s*:\s*\d+px")


def iter_files(root: Path):
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in SRC_EXT and not (set(p.parts) & SKIP_DIRS):
            yield p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--tokens", help="path file token (dikecualikan dari cek hardcode)")
    a = ap.parse_args()
    root = Path(a.root).resolve()
    findings = []  # (level, file, msg)
    token_files = set()
    if a.tokens:
        token_files.add(Path(a.tokens).resolve())

    files = list(iter_files(root))
    for f in files:
        if f.name in {"tokens.css", "tokens.scss", "theme.css", "globals.css"} or "tokens" in f.stem:
            token_files.add(f.resolve())

    blob_all = ""
    for f in files:
        try:
            txt = f.read_text(errors="ignore")
        except OSError:
            continue
        blob_all += txt + "\n"
        low = txt.lower()
        rel = f.relative_to(root)
        is_token = f.resolve() in token_files

        if is_token:
            for marker, why in DEFAULT_MARKERS.items():
                if marker in low:
                    findings.append(("high", rel, f"token belum diganti: {marker} ({why})"))
        else:
            hexes = HEX.findall(txt)
            if len(hexes) >= 3:
                findings.append(("med", rel, f"{len(hexes)} warna hex di-hardcode di luar token (contoh: {hexes[0]})"))
            if RADIUS_PX.search(txt):
                findings.append(("low", rel, "border-radius px di-hardcode; pakai var(--radius-*)"))

        for pat in GENERIC_COPY:
            m = re.search(pat, low)
            if m and f.suffix.lower() not in {".css", ".scss"}:
                findings.append(("med", rel, f"copy generik: '{m.group(0)}'"))
        for pat in FAKE_CLAIMS:
            m = re.search(pat, txt, re.I)
            if m and f.suffix.lower() not in {".css", ".scss"}:
                findings.append(("high", rel, f"klaim yang mungkin palsu / placeholder: '{m.group(0)}' (verifikasi sumbernya)"))

    low_all = blob_all.lower()
    if files and ":focus-visible" not in low_all and "focus-visible:" not in low_all:
        findings.append(("high", "(proyek)", "tidak ada gaya :focus-visible, keyboard user tidak punya fokus yang terlihat"))
    if files and "prefers-reduced-motion" not in low_all and "motion-reduce" not in low_all:
        findings.append(("med", "(proyek)", "prefers-reduced-motion tidak dihormati"))

    order = {"high": 0, "med": 1, "low": 2}
    findings.sort(key=lambda x: order[x[0]])
    if not findings:
        print("Tidak ada temuan otomatis. Tetap jalankan tiga test di references/audit.md.")
        return 0
    for lvl, f, msg in findings:
        print(f"[{lvl.upper():4}] {f}: {msg}")
    high = sum(1 for x in findings if x[0] == "high")
    print(f"\n{len(findings)} temuan, {high} high. Cek konteks sebelum menghapus; ini heuristik.")
    return 1 if high else 0


if __name__ == "__main__":
    sys.exit(main())
