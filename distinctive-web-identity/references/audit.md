# Audit

Isi: tiga test identitas, skor 12 dimensi, checklist slop, checklist publish, checklist design system.

- [Tiga test identitas](#tiga-test-identitas)
- [Skor identitas](#skor-identitas)
- [Checklist slop](#checklist-slop)
- [Checklist design system](#checklist-design-system)
- [Checklist publish](#checklist-publish)

## Tiga test identitas

**Blind brand recognition.** Bayangkan screenshot tanpa logo, nama brand, favicon, dan URL. Jawab: masih terasa seperti brand tertentu? Apa tiga karakter paling mudah dikenali? Konsisten di halaman lain? Bisakah kompetitor memakai desain ini tanpa mengubah apa pun? Signature-nya membantu UX atau cuma dekorasi?

**Remove the logo.** Tanpa logo, typography, color relationship, layout, image treatment, motion, dan content voice masih terasa khas. Tujuannya bukan orang selalu menebak brand dengan benar, tapi pengalaman keseluruhan yang membangun pengenalan.

**Competitor swap.** Ganti logo, nama, dan warna utama. Kalau hasilnya masih cocok untuk kompetitor, design system terlalu generik. Landing page yang jadi SaaS lain cuma dengan ganti gradient dan logo berarti diferensiasinya lemah.

## Skor identitas

Skor 0-5 per dimensi: brand specificity, typography, color system, layout identity, image direction, iconography, motion language, content voice, component consistency, accessibility, performance, signature experience.

Interpretasi total (maks 60): 0-20 sangat generik, 21-35 mulai punya identitas, 36-50 cukup kuat, 51-60 sangat kuat. Ini framework praktis, bukan benchmark industri resmi. Bilang begitu kalau dilaporkan ke user.

## Checklist slop

Jawaban "ya" pada banyak butir negatif berarti harus disederhanakan.

- Terlihat seperti template generik?
- Headline bisa dipakai 1.000 brand lain?
- Semua section pakai card?
- Terlalu banyak gradient atau glow?
- Semua elemen dianimasikan?
- Ada informasi yang sebenarnya tidak perlu?
- Ada fake testimonial atau statistik?
- Konten terasa seperti parafrase AI tanpa insight?
- Ada klaim tanpa bukti?
- CTA terlalu banyak?
- Desain lebih menonjol daripada produk?
- JavaScript yang dipakai benar-benar perlu?

Butir positif yang harus lolos: mobile diuji, keyboard navigation jalan, kontras cukup, loading cepat.

## Checklist design system

Brand personality, design principles, typography system, color tokens, spacing tokens, radius tokens, shadow/elevation, grid, iconography rules, image art direction, motion rules, component rules, accessibility rules, content voice, navigation rules, responsive rules, performance rules, signature elements, governance, dokumentasi. Tandai mana yang ada dan mana yang belum.

## Checklist publish

- Setiap halaman punya tujuan jelas; tidak ada section yang cuma dekorasi
- Identitas konsisten; tidak ada fake claim
- Semua CTA berfungsi; semua form tervalidasi; error dan loading state ada
- Responsive di mobile, tablet, desktop; tidak ada overflow
- Keyboard navigation diuji; focus state terlihat; alt text ada; kontras diperiksa; reduced motion dihormati
- Core Web Vitals diperiksa; image dioptimasi; third-party script minimal
- Secret tidak di frontend; HTTPS aktif; dependency diperiksa
- SEO dasar benar; konten ditulis untuk manusia
