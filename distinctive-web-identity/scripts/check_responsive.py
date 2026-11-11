#!/usr/bin/env python3
"""Buka halaman di 375px dan 1366px, laporkan horizontal overflow dan elemen penyebabnya.

Pakai: python scripts/check_responsive.py <file.html | URL> [--shots folder]
Butuh Playwright + Chromium (di Claude Code biasanya sudah ada). Exit 1 kalau overflow.
Kenapa ada: kode/tabel/pre yang lebar adalah penyebab overflow mobile paling umum, dan
tidak kelihatan kalau cuma membaca source.
"""
import argparse, os, sys
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser(); ap.add_argument("target"); ap.add_argument("--shots")
a = ap.parse_args()
url = a.target if "://" in a.target else "file://" + os.path.abspath(a.target)
bad = False
with sync_playwright() as p:
    exe = "/opt/pw-browsers/chromium"
    b = p.chromium.launch(executable_path=exe) if os.path.exists(exe) else p.chromium.launch()
    for w in (375, 768, 1366):
        pg = b.new_page(viewport={"width": w, "height": 800}); pg.goto(url); pg.wait_for_timeout(500)
        sw = pg.evaluate("document.documentElement.scrollWidth")
        if sw > w + 1:
            bad = True
            els = pg.evaluate("""w=>[...document.querySelectorAll('body *')].filter(e=>e.getBoundingClientRect().right>w+1).slice(0,5).map(e=>e.tagName.toLowerCase()+(e.className?'.'+String(e.className).split(' ')[0]:''))""", w)
            print(f"[OVERFLOW] {w}px: scrollWidth={sw}; penyebab: {', '.join(els)}. Beri min-width:0 pada grid/flex child dan overflow-x:auto pada pre/tabel.")
        else:
            print(f"[ok] {w}px")
        if a.shots:
            os.makedirs(a.shots, exist_ok=True); pg.screenshot(path=f"{a.shots}/{w}.png", full_page=True)
    b.close()
sys.exit(1 if bad else 0)
