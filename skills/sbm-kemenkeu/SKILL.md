---
name: sbm-kemenkeu
description: Menjawab pertanyaan tentang Standar Biaya Masukan (SBM) Kementerian Keuangan RI saja, yaitu PMK Nomor 32 Tahun 2025 untuk Tahun Anggaran 2026. Pakai saat pertanyaan menyangkut dana APBN, hibah kementerian, BRIN, atau DIKTI: honorarium narasumber, uang harian perjalanan dinas, tarif penginapan, paket meeting, uang lembur, sewa kendaraan, konsumsi rapat. Sebut "sbm-kemenkeu" untuk memanggilnya.
---

# SBM Kemenkeu: Standar Biaya Masukan TA 2026

Skill ini menjawab **hanya dari aturan Kementerian Keuangan RI**. Kalau pertanyaannya menyangkut dana internal Universitas Indonesia, skill ini bukan tempatnya, dan Anda harus mengatakan begitu.

## Apa itu Standar Biaya Masukan

**Standar Biaya Masukan (SBM)** adalah daftar harga satuan resmi yang dipakai saat menyusun anggaran negara. Ia menjawab pertanyaan "berapa maksimal boleh saya bayar untuk hal ini". Contohnya honorarium narasumber per jam, uang harian perjalanan dinas per hari, atau tarif hotel per malam.

Istilah "masukan" (*input*) artinya ia mengatur harga **bahan** kegiatan, bukan harga hasilnya. SBM adalah yang Anda pakai saat mengisi baris-baris RAB.

## Regulasi yang jadi sumber

**Peraturan Menteri Keuangan Nomor 32 Tahun 2025 tentang Standar Biaya Masukan Tahun Anggaran 2026.** Ditetapkan di Jakarta pada 14 Mei 2025.

**Tahun regulasi bukan tahun anggaran.** PMK ini terbit tahun 2025, tetapi yang diaturnya adalah SBM untuk **Tahun Anggaran 2026**. Orang yang bertanya "berapa SBM 2026" harus diarahkan ke dokumen ini. Jangan pernah menyuruh dia mencari dokumen lain. Sebutkan kedua tahun itu di setiap jawaban.

## Struktur dokumen

PMK ini punya dua lampiran, dan bedanya menentukan boleh tidaknya angka dinaikkan.

| Lampiran | Sifat | Artinya |
|---|---|---|
| **Lampiran I** (39 pos biaya) | **Batas tertinggi** | Tidak boleh dilampaui, titik. |
| **Lampiran II** (19 pos biaya) | **Dapat dilampaui** | Boleh lebih tinggi sepanjang dapat dipertanggungjawabkan. |

Menyebut angka Lampiran II sebagai "batas maksimal" adalah kesalahan yang membuat orang menahan diri secara tidak perlu. Selalu periksa pos itu ada di lampiran mana.

Di dalam tiap lampiran, **tabel tarif dan penjelasan terpisah letaknya**. Penjelasan memuat syarat yang menentukan boleh tidaknya honor dibayarkan. Tarif tanpa syarat adalah setengah jawaban.

## Aturan keras

1. **Jangan pernah menjawab dari ingatan.** Setiap angka wajib dibaca langsung dari `references/sbm-kemenkeu-ta2026.md`. Model bahasa mengingat tarif SBM tahun-tahun lama dan akan mencampurnya dengan percaya diri. Angka salah di dokumen anggaran berbiaya nyata: revisi RAB, temuan auditor, dana ditolak.
2. **Selalu sebut**: PMK 32/2025, lampiran keberapa, pos nomor berapa, dan bahwa ia berlaku untuk TA 2026.
3. **Selalu sebut sifatnya**: batas tertinggi (Lampiran I) atau dapat dilampaui (Lampiran II).
4. **Selalu cantumkan nomor baris** tempat angka dibaca, plus perintah verifikasi ke PDF asli.
5. **Kalau OCR ambigu, katakan ambigu.** Jangan menambal tebakan.

## Sumber data dan keterbatasannya

Di `references/`:

| Berkas | Isi |
|---|---|
| `sbm-kemenkeu-ta2026.md` | Teks penuh PMK 32/2025 |
| `indeks-kemenkeu-ta2026.md` | Peta 58 pos biaya beserta nomor barisnya |

**Teksnya hasil OCR, dan sebagian tabel rusak.** Skill ini jujurnya adalah **pencari lokasi**, bukan kalkulator. Ia menemukan pos biayanya, membaca angkanya, lalu menyuruh Anda memverifikasi ke PDF asli di `sources/pmk-32-2025-sbm-ta2026.pdf`.

## Cara menjawab, langkah demi langkah

**Langkah 1. Orientasi lewat indeks.** Buka `indeks-kemenkeu-ta2026.md`, temukan pos biaya dan nomor barisnya. Indeks dibangun otomatis dari OCR, jadi tidak lengkap. **Jangan berhenti di sini.**

**Langkah 2. Cari dengan resep tahan-OCR.** Selalu lakukan ini, bahkan kalau indeks sudah menunjukkan sesuatu.

**Jangan pakai `grep` polos.** Ia bisa gagal diam-diam: nol hasil, seolah posnya tidak ada, padahal ada. Penyebabnya, OCR menyelipkan pipa tabel dan spasi ganda di tengah frasa.

**Pakai resep ini.** Ia menormalkan pipa dan spasi lebih dulu. `sed` dan `tr` tidak menambah atau menghapus baris, jadi **nomor barisnya tetap akurat** terhadap berkas asli:

```bash
sed 's/|/ /g' references/sbm-kemenkeu-ta2026.md | tr -s ' ' | grep -n -i "pembawa acara"
```

Kalau nihil, mundur ke satu kata yang paling khas. Pakai juga beberapa sinonim, karena dokumen memakai istilah formal yang mungkin bukan istilah si penanya: "uang harian" bukan "uang saku", "paket rapat/pertemuan di luar kantor" bukan "fullboard", "penginapan" bukan "hotel", "satuan biaya tiket" bukan "harga tiket".

**Langkah 3. Baca konteksnya, jangan cuma barisnya.** Baca sekitar 30 baris di sekelilingnya, dengan normalisasi yang sama supaya tabelnya terbaca:

```bash
sed -n '350,380p' references/sbm-kemenkeu-ta2026.md | sed 's/|/ /g' | tr -s ' '
```

Tarif SBM hampir selalu berjenjang: menurut eselon, golongan, provinsi, atau tingkat kegiatan. Satu baris tanpa konteks akan menyesatkan. Tarif provinsi khususnya panjang, ada 38 provinsi berderet.

**Langkah 4. Baca penjelasan posnya.** Lihat kolom bagian di indeks: cari pos yang sama di `L1-PENJELASAN` atau `L2-PENJELASAN`. Di sanalah syaratnya, misalnya batasan jumlah jam, atau syarat narasumber harus berasal dari luar unit penyelenggara.

**Langkah 5. Susun jawabannya** memakai template di bawah.

## Kamus satuan

Dari Lampiran I (baris 4072 sampai 4081):

| Kode | Arti |
|---|---|
| OJ | Orang/Jam |
| OH | Orang/Hari |
| OB | Orang/Bulan |
| OT | Orang/Tahun |
| OP | Orang/Paket |
| OK | Orang/Kegiatan |
| OR | Orang/Responden |
| Oter | Orang/Terbitan |
| OJP | Orang/Jam Pelajaran |

## Jebakan yang harus Anda hindari

**Toleransi kabupaten tertentu.** Catatan Umum Lampiran I (sekitar baris 3995) memuat tabel toleransi. Sejumlah kabupaten boleh melampaui satuan biaya provinsinya, dengan rentang 115% sampai 303%. Contohnya Puncak Jaya di Papua Tengah (267%), Kepulauan Mentawai di Sumatra Barat (125%), dan Sabu Raijua di Nusa Tenggara Timur (137%).

Toleransi ini **hanya berlaku untuk pos tertentu**: pengadaan kendaraan operasional bus, sewa kendaraan, pengadaan kendaraan operasional roda 2 dan roda 4, pengadaan pakaian dinas, dan konsumsi rapat. Kalau pertanyaannya menyangkut daerah terpencil dan salah satu pos itu, **periksa tabel ini sebelum menjawab.**

**Efisiensi anggaran itu perintah, bukan saran.** Catatan Umum Lampiran I memerintahkan kegiatan seminar, rapat, sosialisasi, bimtek, dan perjalanan dinas dilakukan **secara selektif dan diarahkan ke daring**. Tarif yang tersedia bukan berarti tarif yang wajib dipakai.

**Transportasi dipertanggungjawabkan at cost.** Catatan Umum menyatakan biaya transportasi perjalanan dinas pada prinsipnya memakai bukti riil, bukan lumpsum sebesar tarif.

**Tarif luar negeri memakai satuan mata uang asing.** Pos tiket dan uang harian luar negeri diberi angka tanpa "Rp", dan besarannya dalam ribuan. Baca kepala tabelnya, jangan asumsikan rupiah.

## Bentuk jawaban

Sajikan seperti ini. Bahasa Indonesia, kalimat pendek, angka di depan.

> **Uang harian perjalanan dinas dalam negeri ke DKI Jakarta: Rp‹BESARAN› per orang per hari (OH).**
>
> Dasar: PMK Nomor 32 Tahun 2025, **Lampiran I** pos nomor 28 (Satuan Biaya Uang Harian dan Uang Representasi Perjalanan Dinas Dalam Negeri). Berlaku untuk **Tahun Anggaran 2026**. Sifatnya **batas tertinggi**, tidak boleh dilampaui.
>
> Syarat yang menyertainya: ‹ringkas dari bagian penjelasan›
>
> Dibaca dari `references/sbm-kemenkeu-ta2026.md` baris ‹N› sampai ‹M›. Verifikasi ke `sources/pmk-32-2025-sbm-ta2026.pdf` sebelum dipakai di dokumen resmi.

Tanda `‹...›` di atas adalah **tempat kosong yang wajib Anda isi dari berkas**. Template ini sengaja tidak memuat angka rupiah satu pun, supaya tidak ada angka contoh yang tanpa sadar tersalin jadi jawaban.

Kalau angkanya tidak ketemu, katakan tidak ketemu. Sebutkan kata kunci apa saja yang sudah dicoba, dan sarankan pengguna membuka PDF-nya. **Jangan mengarang.**

Kalau pertanyaannya ternyata menyangkut dana internal UI, katakan skill ini hanya mencakup aturan Kemenkeu, lalu arahkan ke `sbm-ui` atau `sbm`.
