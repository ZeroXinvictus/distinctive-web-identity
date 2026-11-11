# Stack Mapping

Isi: cara menyambungkan `tokens.css` ke stack yang umum dipakai, supaya token tetap jadi satu-satunya sumber kebenaran dan bukan disalin ke mana-mana.

- [Next.js (App Router)](#nextjs-app-router)
- [Tailwind v4](#tailwind-v4)
- [Tailwind v3](#tailwind-v3)
- [shadcn/ui](#shadcnui)
- [HTML statis / panel dengan CSS injeksi](#html-statis--panel-dengan-css-injeksi)
- [Retrofit proyek yang sudah ada](#retrofit-proyek-yang-sudah-ada)

## Next.js (App Router)

- Taruh token di `app/tokens.css`, impor sekali di `app/layout.tsx` sebelum `globals.css`.
- Font lewat `next/font` (self-host, tanpa layout shift), lalu isi `--font-display` dan `--font-body` dari variable-nya: `style={{ ['--font-display' as string]: display.style.fontFamily }}` atau pakai opsi `variable` dan sambungkan di `:root`.
- Komponen berbagi satu `Button`, `Field`, `Surface`. Jangan buat `PrimaryButtonV2`; tambah `variant`.

## Tailwind v4

Token CSS langsung jadi utility lewat `@theme`, jadi tidak perlu duplikasi nilai:

```css
@import "tailwindcss";
@import "./tokens.css";
@theme inline {
  --color-bg: var(--color-bg);
  --color-primary: var(--color-primary);
  --radius-md: var(--radius-md);
  --font-display: var(--font-display);
}
```

Hasilnya `bg-primary`, `rounded-md`, `font-display` membaca token. Hindari arbitrary value seperti `bg-[#3d7bff]` atau `rounded-[10px]`; itu hardcode yang melewati sistem.

## Tailwind v3

Di `tailwind.config`, isi `theme.extend.colors` dengan `'var(--color-primary)'` dan seterusnya. Prinsip sama: config hanya menunjuk ke variable, nilainya tetap di `tokens.css`.

## shadcn/ui

shadcn memakai variable seperti `--background`, `--foreground`, `--primary`, `--radius`. Buat alias di `:root`: `--background: var(--color-bg)`, `--primary: var(--color-primary)`, `--radius: var(--radius-md)`. Setelah itu seluruh komponen shadcn ikut brand tanpa diedit satu-satu. Jangan biarkan tema default shadcn (netral abu + radius 0.5rem) apa adanya kalau itu tujuan skill ini: itu salah satu tampilan yang paling sering dikenali sebagai template.

## HTML statis / panel dengan CSS injeksi

Untuk tema yang cuma bisa lewat satu file CSS (misalnya tema panel pihak ketiga): tulis token di blok `:root` paling atas file, semua rule di bawahnya memakai `var(--...)`. Selector pihak ketiga bisa berubah antar versi, jadi kelompokkan override per komponen dan beri komentar versi yang diuji.

## Retrofit proyek yang sudah ada

1. Jalankan `scripts/lint_identity.py <proyek>` untuk melihat hardcode dan default yang belum diganti.
2. Kumpulkan nilai yang benar-benar dipakai (warna, radius, spacing paling sering) dan jadikan token awal; jangan mendesain ulang dari nol kecuali user minta.
3. Ganti hardcode ke token per komponen, mulai dari yang paling sering muncul (Button, Field, Surface, Navbar).
4. Baru setelah sistem rapi, pilih signature element.
