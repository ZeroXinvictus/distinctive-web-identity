# Identity System

Isi: 5 lapis identitas, lalu aturan per dimensi desain. Baca bagian yang relevan saja.

- [5 lapis identitas](#5-lapis-identitas)
- [Typography](#typography)
- [Color system](#color-system)
- [Spacing dan grid](#spacing-dan-grid)
- [Layout](#layout)
- [Image art direction](#image-art-direction)
- [Iconography](#iconography)
- [Motion](#motion)
- [Micro-interaction](#micro-interaction)
- [Information architecture](#information-architecture)
- [Component dan tokens](#component-dan-tokens)
- [Dark mode](#dark-mode)
- [Governance dan sinkron design-code](#governance-dan-sinkron-design-code)

## 5 lapis identitas

Bangun dari bawah ke atas. Signature harus lahir dari empat lapis sebelumnya.

1. Brand core: mission, audience, positioning, personality, values.
2. Visual identity: logo, color, typography, imagery, iconography.
3. Digital design language: layout, grid, spacing, radius, components, motion.
4. Experience: navigation, interaction, content, accessibility, performance.
5. Signature: interaksi, visual, storytelling, motion, atau gaya konten yang khas.

Identitas digital yang matang terdokumentasi, terhubung ke code, dipakai lintas halaman, dan punya aturan siapa boleh menambah komponen.

## Typography

Kontrol typography sering jadi pembeda terbesar. Tetapkan family, weight, letter spacing, line height, heading scale, lebar paragraf, gaya angka, dan capitalization.

Skala contoh (angka bukan identitas, konsistensi penggunaannya yang penting):

- Display 72/76, weight 650
- H1 56/60
- H2 40/46
- Body 18/28
- Caption 14/20

Minimal lima level: display, heading, subheading, body, caption. Pakai family seminimal mungkin. Heading boleh berkarakter, body tetap mudah dibaca. Hindari uppercase berlebihan dan font dekoratif untuk body. Font unik dengan hierarchy buruk lebih jelek daripada font biasa dengan hierarchy bagus.

## Color system

Definisikan peran, bukan satu hex brand: primary, secondary, accent, background, surface, text, muted, border, success, warning, error.

Tetapkan juga kapan dipakai, seberapa intens, kontrasnya, state interaksi, dan versi dark mode. Contoh peran: primary untuk CTA, accent untuk perhatian, muted untuk info sekunder, surface untuk pengelompokan konten, error untuk aksi destruktif. Ciri khas muncul dari hubungan antar warna, bukan satu warna. Hindari gradient sebagai solusi semua komponen dan neon yang menurunkan keterbacaan.

## Spacing dan grid

Pakai spacing tokens: 4, 8, 12, 16, 24, 32, 48, 64, 80, 96, 128. Tidak semua angka harus dipakai. Tujuannya rhythm, hierarchy, dan prediktabilitas. Container width konsisten, alignment antar-section jelas, whitespace dipakai sebagai alat hierarchy, bukan ruang kosong.

## Layout

Jangan default ke navbar + hero + 3 card + testimonial + CTA + footer. Pola editorial yang bisa jadi signature: oversized typography, asymmetric grid, full-bleed imagery, dense data presentation, split-screen, sticky storytelling, modular blocks. Pilih yang memperkuat produk. Mobile dirancang dari awal, bukan hasil kecilin desktop. Hindari horizontal overflow, baris teks terlalu panjang, CTA kecil, dan section tinggi tanpa isi.

## Image art direction

Dua website dengan font dan warna sama bisa terasa beda karena art direction gambar. Tetapkan subject, lighting, camera angle, cropping, background, color treatment, composition, aspect ratio, dan density. Urutan preferensi asset: asset asli produk, screenshot produk, foto asli, ilustrasi custom, stock yang benar-benar relevan, AI-generated yang dikurasi. Stock acak melemahkan identitas. Semua image penting punya alt text sesuai konteks.

## Iconography

Satu bahasa visual: tetapkan stroke width, corner style, fill atau outline, ukuran, grid, optical alignment. Jangan campur 3D icon, emoji, outline, filled, dan SVG acak tanpa alasan art direction. Icon tidak boleh menggantikan label penting. Jangan kasih icon untuk setiap kalimat.

## Motion

Definisikan motion language: durasi (fast, normal, slow), easing (standard, enter, exit, emphasized), dan behavior (fade, slide, scale, reveal, morph). Tanya "bagaimana brand ini bergerak?":

- Finansial: tenang, presisi
- Gaming: energetik
- Luxury: lambat, tertahan
- Developer platform: fungsional, tajam

Animasi untuk state change, feedback, orientasi, dan hubungan antar elemen. Hindari semua-elemen-fade-in, parallax berlebihan, floating tanpa henti, cursor effect mengganggu, dan scroll animation yang bikin lambat. Hormati `prefers-reduced-motion`.

## Micro-interaction

Identitas sering ada di detail: button hover, copy feedback, toggle, validasi input, toast, loading, skeleton, modal, dropdown, pesan error. Perlakukan sebagai bagian inti pengalaman. Skeleton hanya kalau membantu memahami struktur konten; untuk aksi singkat pakai loading state di button.

## Information architecture

Navigasi mencerminkan mental model pengguna, bukan struktur internal perusahaan. Website kecil cukup: Home, About, Product/Service, Documentation/Project, Contact. Jangan 15 menu karena semua halaman ada. CTA utama konsisten di semua halaman.

## Component dan tokens

Contoh token minimum: `--color-primary`, `--color-surface`, `--color-text`, `--radius-sm/md/lg`, `--space-1..n`, `--font-display`, `--font-body`, `--motion-fast`, `--motion-normal`. Komponen membaca token: radius dari `--radius-md`, tinggi dari `--control-height`, warna dari `--color-primary`. Kalau brand berubah, ubah sistem, bukan ratusan halaman.

Konsistensi komponen: button di halaman A dan B punya radius, tinggi, dan hover yang sama kecuali ada variant yang didefinisikan.

## Dark mode

Jangan sekadar invert warna. Kontras tetap baik, hierarchy surface tetap terlihat, shadow disesuaikan, image tetap terbaca, state form tetap jelas. Ikuti system preference bila sesuai.

## Governance dan sinkron design-code

Tanpa aturan, design system balik jadi kumpulan komponen acak. Tulis: siapa boleh membuat komponen, kapan komponen baru diperlukan, penamaan, pembuatan variant, penanganan deprecated, review. Mapping design ke code harus 1:1 (`Button / Primary / Large` jadi `<Button variant="primary" size="lg">`), bukan `div class="random-button-final-v7"`.
