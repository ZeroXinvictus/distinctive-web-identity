---
name: distinctive-web-identity
description: Bikin, retrofit, atau audit website supaya punya identitas khas ala company besar dan bebas "slop" (generik, template, AI-looking). Pakai skill ini setiap kali user minta bikin landing page, website, dashboard, company profile, toko/panel/web app, redesign, tema (Next.js, Tailwind, shadcn, CSS injeksi), "biar keliatan mahal/profesional/beda", design system, design tokens, brand identity digital, atau minta review/audit tampilan web, walau user nggak nyebut kata "identitas" atau "anti-slop". Juga pakai saat user mengeluh hasil desain terlihat generik, template banget, atau kayak buatan AI.
---

# Distinctive Web Identity

Website yang terasa punya ciri khas bukan karena satu warna unik atau animasi mahal. Ciri khas datang dari design language yang konsisten: keputusan desain yang spesifik, diulang di semua halaman, sampai bisa dikenali tanpa logo. Skill ini bikin Claude membangun dari sistem dulu, baru halaman.

Rumus kerja: 80% familiar dan usable (navigasi, form, button, accessibility), 20% distinctive (typography, imagery, layout, motion, storytelling). Kalau semua bagian dipaksa jadi signature, hasilnya noisy dan susah dipakai.

## Alur kerja

0. **Tentukan mode.** Bangun baru, retrofit proyek yang sudah ada (jangan desain ulang dari nol; mulai dari nilai yang sudah dipakai, lihat `references/stack-mapping.md`), atau audit saja. Kalau proyek sudah punya kode, jalankan `python scripts/lint_identity.py <folder>` dulu: dalam hitungan detik ia menunjukkan hardcode, token default yang belum diganti, copy generik, dan fondasi accessibility yang hilang. Kalau ada `IDENTITY.md` dari sesi sebelumnya, baca itu dan lanjutkan, jangan mengulang diskusi.
1. **Brand core dulu.** Tentukan personality (3-5 kata sifat), audiens, dan satu kalimat "brand ini mau dikenal sebagai apa". Kalau user belum ngasih, ambil dari konteks proyek atau tanya satu pertanyaan singkat. Jangan mulai dari "animasi apa yang keren". Simpan hasil langkah 1-2 dan 5 di `IDENTITY.md` (template: `assets/identity-brief.md`) supaya semua halaman dan sesi berikutnya berpegang pada keputusan yang sama.
2. **Visual territory.** Tulis 4-6 design keywords dan wilayah visualnya (contoh: dark neutral, satu accent, technical grid, glow terkontrol). Ini jadi filter untuk setiap keputusan berikutnya.
3. **Tokens sebelum komponen.** Salin `assets/tokens.css`, ubah nilainya sesuai brand. Scaffold ini sengaja netral; font Inter + biru `#3d7bff` yang dibiarkan apa adanya justru tampilan paling generik, jadi ganti setidaknya font, primary, accent, dan radius berdasarkan visual territory. Semua warna, spacing, radius, font, dan motion dibaca dari token, tidak ada nilai hardcode di komponen.
4. **Komponen dengan state lengkap.** Button, input, card, navbar, modal: default, hover, focus, active, disabled, loading, error. Perbedaan kecil ditangani variant, bukan komponen baru.
5. **Satu signature element.** Pilih satu sampai dua (visual, interaksi, motion, atau gaya konten) yang lahir dari brand core. Terapkan konsisten, jangan taburkan di mana-mana.
6. **Konten spesifik.** Headline harus nggak bisa dipakai 1.000 brand lain. Pakai bahasa produk, angka nyata, screenshot asli. Detail ada di `references/content-and-proof.md`.
7. **Audit sebelum selesai.** Jalankan blind brand test, competitor swap test, dan checklist slop. Perbaiki sebelum menyerahkan hasil. Detail di `references/audit.md`.

## Aturan keras

- Tiap elemen harus bisa jawab "kenapa ada?". Kalau gradient, card, badge, glow, atau icon nggak punya fungsi, hapus.
- Jangan pernah bikin fake testimonial, fake user count, fake review, fake logo client, fake security badge, atau fake statistik. Kalau data nyata belum ada, pakai placeholder yang jelas bertanda dan bilang ke user.
- Jangan taruh secret atau API credential di frontend.
- Kombinasi dark background + neon gradient + glassmorphism + glow + 3D sphere + floating animation + grid background + copy "AI-powered / next generation" sekaligus adalah resep slop. Boleh dipakai satu-dua kalau ada alasan, tidak semua.
- Layout unik cuma boleh kalau memperkuat produk. Jangan bikin navigasi atau button aneh supaya terlihat beda.
- Accessibility dan performance bagian dari identitas: WCAG 2.2 AA sebagai baseline, `prefers-reduced-motion` dihormati, LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1.
- Prioritas saat konflik: clarity di atas dekorasi, purpose di atas trend, usability di atas animasi, proof di atas hype, hapus sebelum menambah.

## Kapan baca file referensi

- `references/identity-system.md`: saat menyusun design language lengkap (typography scale, color roles, spacing, layout, imagery, iconography, motion, micro-interaction, governance, 5 lapis identitas).
- `references/content-and-proof.md`: saat nulis hero, microcopy, empty/error/loading state, trust section, SEO.
- `references/stack-mapping.md`: saat menyambungkan token ke Next.js, Tailwind v3/v4, shadcn/ui, CSS injeksi, atau me-retrofit proyek yang sudah ada.
- `references/audit.md`: saat mengaudit website yang ada atau memeriksa hasil sendiri sebelum selesai (3 test, skor 12 dimensi, checklist slop, checklist publish).

## Format output

Kalau diminta membangun: serahkan kode yang jalan, token di satu file, komponen yang memakai token, dan satu paragraf pendek yang menyebut signature element yang dipilih beserta alasannya. Kalau diminta audit: skor per dimensi, tiga masalah terbesar, dan perbaikan konkret berurutan dari dampak terbesar. Sebelum menyerahkan hasil bangun, jalankan `scripts/lint_identity.py` dan `scripts/check_responsive.py <file>` lalu perbaiki temuan "high" dan overflow; membaca source saja tidak menangkap kode atau tabel yang meluber di layar HP. Tanpa recap panjang.

## Bekerja bersama skill desain lain

Kalau ada skill desain frontend umum (misalnya `frontend-design`), skill itu menangani eksekusi visual dan estetika per halaman; skill ini menangani konsistensi sistem dan audit identitas. Jalankan langkah 0-3 di sini dulu supaya keputusan visual dari skill lain jatuh di dalam token, bukan di luarnya.
