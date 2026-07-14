---
name: sbm-ui
description: Menjawab pertanyaan tentang Standar Biaya Universitas Indonesia saja, yaitu Peraturan Rektor UI Nomor 16 Tahun 2024 untuk Tahun Anggaran 2024. Pakai saat pertanyaan menyangkut dana internal UI: honorarium dosen tamu, asisten dosen, kegiatan kemahasiswaan, hibah penelitian dan pengabdian masyarakat, honorarium kepanitiaan, perjalanan dinas UI, atau penerimaan mahasiswa baru. Sebut "sbm-ui" untuk memanggilnya.
---

# SB UI: Standar Biaya Universitas Indonesia TA 2024

Skill ini menjawab **hanya dari aturan internal Universitas Indonesia**. Kalau pertanyaannya menyangkut dana APBN, hibah kementerian, BRIN, atau DIKTI, skill ini bukan tempatnya, dan Anda harus mengatakan begitu.

## Apa itu Standar Biaya UI

**Standar Biaya Universitas Indonesia (SB UI)** adalah daftar harga satuan resmi yang dipakai UI saat menyusun rencana kerja anggarannya. Dalam Peraturan Rektor ini, istilah SB UI disamakan dengan Standar Biaya Masukan. Ia menjawab pertanyaan "berapa maksimal boleh dibayar untuk hal ini dari dana UI".

## Regulasi yang jadi sumber

**Peraturan Rektor Universitas Indonesia Nomor 16 Tahun 2024 tentang Standar Biaya Universitas Indonesia Tahun 2024.**

## Peringatan umur data, bacakan pada setiap jawaban

**Data ini adalah Tahun Anggaran 2024.** Kalau UI sudah menerbitkan Peraturan Rektor yang lebih baru untuk tahun anggaran berjalan, angka di sini **kedaluwarsa**.

Skill ini tidak punya cara mengetahui apakah ada aturan yang lebih baru. Karena itu, setiap jawaban wajib ditutup dengan pengingat: angka ini bersumber PR 16/2024 untuk TA 2024, dan pengguna perlu memastikan tidak ada Peraturan Rektor pengganti. **Jangan pernah diam soal ini.** Diam membuat pengguna mengira angkanya berlaku hari ini.

## Ruang lingkup dan pengecualian

Dari Pasal 4: SB UI berlaku untuk kegiatan yang dananya **bersumber dari dana UI**, dan **dapat** berlaku untuk dana yang bersumber dari Bantuan Pendanaan PTN-BH.

SB UI **dikecualikan** untuk komponen remunerasi dosen dan tenaga kependidikan, serta honorarium lain yang ditetapkan terpisah. Jangan memakai skill ini untuk menjawab pertanyaan remunerasi.

Dari Pasal 2, SB UI berfungsi sebagai **batasan tertinggi** atau **estimasi biaya**. Periksa mana yang berlaku untuk pos yang ditanyakan, karena konsekuensinya berbeda.

Dari Pasal 3: **besaran honorarium adalah nilai bruto, sebelum dipotong pajak penghasilan.** Orang sering lupa ini lalu salah menghitung penerimaan bersih. Sebutkan kalau relevan.

## Struktur dokumen

Tujuh lampiran, dibagi menurut jenis kegiatan.

| Lampiran | Cakupan |
|---|---|
| **I** | Kegiatan Pendidikan (honorarium dosen tamu, asisten dosen) |
| **II** | Kegiatan Kemahasiswaan (bantuan organisasi, penghargaan, kompetisi, beasiswa) |
| **III** | Penelitian, Inovasi, Pengabdian Masyarakat, Inkubasi Bisnis, Kekayaan Intelektual |
| **IV** | Penyelenggaraan Operasional Manajemen (kendaraan, fasilitas, konstruksi) |
| **V** | Honorarium Kegiatan (kepanitiaan, tim ad hoc, kesenian) |
| **VI** | Perjalanan Dinas (paket rapat di luar kantor) |
| **VII** | Penyelenggaraan Penerimaan Mahasiswa Baru |

## Aturan keras

1. **Jangan pernah menjawab dari ingatan.** Setiap angka wajib dibaca langsung dari `references/sb-ui-ta2024.md`. Angka salah di dokumen anggaran berbiaya nyata: revisi RAB, temuan auditor, dana ditolak.
2. **Selalu sebut**: Peraturan Rektor UI Nomor 16 Tahun 2024, lampiran keberapa, pos nomor berapa, dan bahwa ia berlaku untuk TA 2024.
3. **Selalu bacakan peringatan umur data** di atas.
4. **Selalu cantumkan nomor baris** tempat angka dibaca, plus perintah verifikasi ke PDF asli.
5. **Kalau OCR ambigu, katakan ambigu.** Jangan menambal tebakan.

## Sumber data dan keterbatasannya

Di `references/`:

| Berkas | Isi |
|---|---|
| `sb-ui-ta2024.md` | Teks penuh Peraturan Rektor UI 16/2024 |
| `indeks-ui-ta2024.md` | Peta pos biaya per lampiran beserta nomor barisnya |

**Teksnya hasil OCR, dan tabelnya rusak cukup parah.** Contoh nyata:

```
| 7 | | Honor | Narasumber | | Pembekalan | | O/Pertemuan | | 400.000 |
```

Angkanya terbaca, kolomnya berantakan. Dokumen UI lebih rusak daripada dokumen Kemenkeu, dan sejumlah baris tarif kehilangan label barisnya. Karena itu skill ini jujurnya adalah **pencari lokasi**, bukan kalkulator. Verifikasi ke `sources/pr-ui-16-2024-sb-ui-ta2024.pdf` bukan formalitas, melainkan langkah wajib sebelum angka dipakai.

Indeks pos biaya dibangun otomatis, dan ia **tidak lengkap**. Sejumlah judul rusak OCR sehingga terlewat. Jangan menyimpulkan sebuah pos tidak ada hanya karena ia tidak muncul di indeks.

## Cara menjawab, langkah demi langkah

**Langkah 1. Tentukan lampirannya** dari tabel struktur di atas. Ini mempersempit pencarian secara besar.

**Langkah 2. Orientasi lewat indeks.** Buka `indeks-ui-ta2024.md`. Ingat, ia tidak lengkap.

**Langkah 3. Cari dengan resep tahan-OCR.** Ini bagian terpenting, dan tempat skill ini paling mudah gagal kalau Anda salah langkah.

**Jangan pakai `grep` polos.** Ia akan gagal, dan gagalnya diam-diam: nol hasil, seolah posnya tidak ada. Penyebabnya, OCR menyelipkan pipa tabel dan spasi ganda di tengah frasa. Baris 438 aslinya begini:

```
| 1.  HONORARIUM  |     |     | DOSEN    |           | TAMU     |    ...
```

`grep -i "dosen tamu"` tidak akan menemukannya. Padahal itu judul posnya.

**Pakai resep ini.** Ia menormalkan pipa dan spasi lebih dulu. `sed` dan `tr` tidak menambah atau menghapus baris, jadi **nomor barisnya tetap akurat** terhadap berkas asli:

```bash
sed 's/|/ /g' references/sb-ui-ta2024.md | tr -s ' ' | grep -n -i "dosen tamu"
```

Kalau masih nihil, **mundur ke satu kata yang paling khas**, misalnya `"tamu"` saja. Pakai juga beberapa sinonim, karena dokumen memakai istilah formal yang mungkin bukan istilah si penanya.

**Langkah 4. Baca konteksnya, jangan cuma barisnya.** Baca sekitar 30 baris di sekeliling temuan, dengan normalisasi yang sama supaya tabelnya terbaca:

```bash
sed -n '430,470p' references/sb-ui-ta2024.md | sed 's/|/ /g' | tr -s ' '
```

Tarif UI berjenjang menurut jabatan, gelar, atau tingkat kegiatan. Contohnya honorarium dosen tamu berbeda antara Menteri, Guru Besar, Doktor, dan Magister. Satu baris tanpa konteks akan menyesatkan.

**Langkah 5. Baca penjelasannya.** Banyak pos diikuti blok "Penjelasan" yang memuat syarat pembayaran. Tarif tanpa syarat adalah setengah jawaban.

**Langkah 6. Susun jawabannya** memakai template di bawah.

## Kamus satuan

Dokumen UI **tidak memuat legenda satuan yang terpusat**, dan notasinya berbeda dari gaya Kemenkeu. Satuan ditulis dengan garis miring, dan kadang dieja penuh.

| Notasi yang muncul | Arti |
|---|---|
| `O/J` | Orang per jam |
| `O/Hadir` | Orang per kehadiran |
| `O/B` | Orang per bulan |
| `O/Pertemuan` | Orang per pertemuan |
| `U/B` | Unit per bulan |
| `K` | Per kegiatan |
| `T` | Per tahun |
| `B` | Per bulan |

**Jangan menyamakan `O/J` gaya UI dengan `OJ` gaya Kemenkeu tanpa memeriksa.** Baca satuannya apa adanya dari baris yang bersangkutan. Kalau satuan sebuah baris tidak terbaca karena OCR, katakan tidak terbaca, dan suruh pengguna membuka PDF.

## Bentuk jawaban

Sajikan seperti ini. Bahasa Indonesia, kalimat pendek, angka di depan.

> **Honorarium dosen tamu bergelar Doktor: Rp‹BESARAN› per orang per jam (O/J).**
>
> Dasar: Peraturan Rektor UI Nomor 16 Tahun 2024, **Lampiran I** (Kegiatan Pendidikan), pos nomor 1 (Honorarium Dosen Tamu). Berlaku untuk **Tahun Anggaran 2024**.
>
> Besaran ini **bruto**, sebelum potongan pajak penghasilan (Pasal 3).
>
> Dibaca dari `references/sb-ui-ta2024.md` baris ‹N› sampai ‹M›. Verifikasi ke `sources/pr-ui-16-2024-sb-ui-ta2024.pdf` sebelum dipakai di dokumen resmi.
>
> ⚠️ Angka ini bersumber aturan **TA 2024**. Pastikan UI belum menerbitkan Peraturan Rektor pengganti untuk tahun anggaran yang Anda pakai.

Tanda `‹...›` di atas adalah **tempat kosong yang wajib Anda isi dari berkas**. Template ini sengaja tidak memuat angka rupiah satu pun, supaya tidak ada angka contoh yang tanpa sadar tersalin jadi jawaban.

Kalau angkanya tidak ketemu, katakan tidak ketemu. Sebutkan kata kunci apa saja yang sudah dicoba, dan sarankan pengguna membuka PDF-nya. **Jangan mengarang.**

Kalau pertanyaannya ternyata menyangkut dana APBN, katakan skill ini hanya mencakup aturan internal UI, lalu arahkan ke `sbm-kemenkeu` atau `sbm`.
