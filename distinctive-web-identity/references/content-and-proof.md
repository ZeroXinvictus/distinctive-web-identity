# Content and Proof

Isi: hero, microcopy, state halaman, trust, SEO, security, dependency.

- [Hero](#hero)
- [Content voice](#content-voice)
- [Microcopy](#microcopy)
- [Empty, error, loading state](#empty-error-loading-state)
- [Form](#form)
- [Trust dan proof](#trust-dan-proof)
- [Content density dan footer](#content-density-dan-footer)
- [SEO](#seo)
- [Security dan dependency](#security-dan-dependency)

## Hero

Dalam beberapa detik hero harus menjawab: siapa, menawarkan apa, untuk siapa, manfaat utama, tindakan apa yang diminta. Urutan: eyebrow kecil, headline spesifik, penjelasan singkat, primary CTA, secondary CTA hanya kalau perlu, lalu visual produk atau data nyata.

Headline generik yang harus dihindari: "Revolutionize Your Business", "Powering the Future", "Build Something Amazing", "Your Success Starts Here". Tes: kalau headline bisa dipakai 1.000 brand lain, tulis ulang.

Buruk: "Unlock the power of next-generation digital transformation."
Lebih baik: "Terima pembayaran QRIS melalui satu API."

## Content voice

Tentukan tone (profesional, ramah, teknis, percaya diri, tenang, berani), kosakata yang sering dan yang dihindari, cara menyebut produk dan user, serta gaya kalimat (pendek, editorial, conversational, teknis). Konten harus spesifik, faktual, berguna, mudah diverifikasi, dan ditulis untuk manusia.

## Microcopy

Button menjelaskan hasil aksi. Pakai "Mulai integrasi", "Salin API Key", "Periksa transaksi", "Simpan perubahan". Hindari "Unlock Your Potential Today!".

## Empty, error, loading state

Empty state: jelaskan dan tawarkan aksi. Contoh: "Belum ada transaksi. Transaksi yang berhasil akan muncul di sini." plus tombol "Lakukan transaksi pertama".

Error state minimal berisi penjelasan, penyebab bila diketahui, dan aksi berikutnya. Contoh: "Koneksi ke server gagal. Periksa koneksi internet Anda lalu coba lagi." Jangan tampilkan stack trace, SQL error, path internal, atau token.

Loading: skeleton hanya kalau membantu memahami struktur; aksi singkat pakai loading di button; jangan bikin loading screen panjang untuk proses cepat.

## Form

State minimal: empty, focus, typing, loading, success, error. Pesan error menjelaskan apa yang salah dan cara memperbaikinya. Buruk: "Something went wrong." Baik: "Email belum diisi. Masukkan alamat email untuk melanjutkan." Setiap input punya label, error bisa dibaca screen reader.

## Trust dan proof

Tampilkan bukti nyata: client yang boleh dipublikasikan, case study, screenshot, metrik yang bisa dibuktikan, dokumentasi, pricing jelas, kontak, identitas brand, terms dan privacy bila perlu.

Dilarang: fake testimonial, fake user count, fake review, fake logo client, fake security badge, fake statistik. Statistik tanpa sumber dan klaim kosong juga dibuang. Kalau data nyata belum ada, tulis placeholder yang jelas atau kosongkan section-nya, lalu kasih tahu user apa yang perlu diisi.

## Content density dan footer

Kalau info bisa disampaikan dengan satu paragraf, tiga bullet, atau satu screenshot, jangan bikin sepuluh card. Pakai progressive disclosure untuk info kompleks. Footer cukup: brand, navigasi penting, kontak, legal, social bila relevan, copyright.

## SEO

Boleh dan perlu, tanpa slop: title dan meta description relevan, semantic HTML, heading deskriptif, internal linking, structured data bila relevan, sitemap, robots, canonical bila perlu, konten people-first. Jangan bikin halaman cuma untuk mengejar keyword, keyword stuffing, FAQ palsu, atau artikel massal berstruktur identik. Penggunaan AI bukan masalah; yang jadi masalah adalah output generik tanpa nilai tambah.

## Security dan dependency

Jangan taruh secret key atau credential di frontend, jangan biarkan endpoint admin tanpa proteksi. Pakai HTTPS, secure cookies, validasi input, authN/authZ, rate limiting, CSRF bila relevan, CSP bila cocok.

Sebelum memasang library: apakah browser API sudah cukup, apakah ukuran bundle sepadan, apakah masih dirawat, apakah menambah risiko. Jangan pasang library untuk fitur kecil yang bisa dibuat native.
