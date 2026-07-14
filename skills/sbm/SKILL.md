---
name: sbm
description: Menjawab pertanyaan tentang Standar Biaya Masukan (SBM), baik aturan Kemenkeu RI maupun Standar Biaya Universitas Indonesia, lengkap dengan tahun referensinya. Pakai saat ada pertanyaan soal SBM, standar biaya, honorarium narasumber, uang harian, biaya perjalanan dinas, tarif penginapan, paket meeting, uang lembur, sewa kendaraan, atau saat menyusun RAB dan mengecek apakah sebuah angka melampaui batas. Sebut "sbm" untuk memanggilnya.
---

# SBM: Standar Biaya Masukan (Kemenkeu RI + Universitas Indonesia)

Skill ini menjawab pertanyaan tarif standar biaya dari **dua rezim aturan sekaligus**, lalu menyebutkan tahun referensi masing-masing.

## Apa itu Standar Biaya Masukan

**Standar Biaya Masukan (SBM)** adalah daftar harga satuan resmi yang dipakai saat menyusun anggaran. Ia menjawab pertanyaan "berapa maksimal boleh saya bayar untuk hal ini". Contohnya honorarium narasumber per jam, uang harian perjalanan dinas per hari, atau tarif hotel per malam.

Istilah "masukan" (*input*) artinya ia mengatur harga **bahan** kegiatan, bukan harga hasilnya. Bandingkan dengan Standar Biaya Keluaran, yang mengatur biaya total sebuah output. SBM adalah yang Anda pakai saat mengisi baris-baris RAB.

## Dua rezim, dua kantong aturan

Ini hal pertama yang harus dipahami, dan sumber kebingungan paling sering.

| Rezim | Regulasi | Berlaku untuk Tahun Anggaran | Dipakai kapan |
|---|---|---|---|
| **Kemenkeu RI** | PMK Nomor 32 Tahun 2025 | **2026** | Dana APBN: hibah kementerian, BRIN, DIKTI, dana dekonsentrasi |
| **Universitas Indonesia** | Peraturan Rektor UI Nomor 16 Tahun 2024 | **2024** | Dana internal UI, dan dapat berlaku untuk dana Bantuan Pendanaan PTN-BH |

**Perhatikan tahun regulasi tidak sama dengan tahun anggaran.** PMK terbit tahun 2025, tetapi yang diaturnya adalah SBM Tahun Anggaran 2026. Orang yang bertanya "berapa SBM 2026" harus diarahkan ke PMK 32/2025 ini. Jangan pernah menyuruh dia mencari dokumen lain.

**Mana yang dipakai?** Ikuti sumber dananya, bukan lembaganya. Peneliti UI yang memakai hibah APBN tunduk pada SBM Kemenkeu. Peneliti UI yang memakai dana internal UI tunduk pada SB UI. Kalau sumber dana tidak disebut dalam pertanyaan, **tanyakan dulu**, karena angkanya bisa jauh berbeda.

## Aturan keras

1. **Jangan pernah menjawab dari ingatan.** Setiap angka wajib dibaca langsung dari berkas di `references/`. Model bahasa mengingat tarif SBM tahun-tahun lama dan akan mencampurnya dengan percaya diri. Angka salah di dokumen anggaran berbiaya nyata: revisi RAB, temuan auditor, dana ditolak.
2. **Selalu sebut dua tahun**: nomor regulasi beserta tahun terbitnya, dan tahun anggaran yang diaturnya.
3. **Selalu sebut sifat tarifnya**: batas tertinggi, atau dapat dilampaui. Beda ini menentukan boleh tidaknya angka dinaikkan.
4. **Selalu cantumkan nomor baris** tempat angka itu dibaca, plus perintah verifikasi ke PDF asli.
5. **Kalau OCR ambigu, katakan ambigu.** Jangan menambal tebakan.

## Sumber data dan keterbatasannya

Di `references/`:

| Berkas | Isi |
|---|---|
| `sbm-kemenkeu-ta2026.md` | Teks penuh PMK 32/2025 |
| `indeks-kemenkeu-ta2026.md` | Peta pos biaya Kemenkeu beserta nomor barisnya |
| `sb-ui-ta2024.md` | Teks penuh Peraturan Rektor UI 16/2024 |
| `indeks-ui-ta2024.md` | Peta pos biaya UI beserta nomor barisnya |

**Kedua teks adalah hasil OCR, dan tabelnya rusak sebagian.** Contoh nyata dari berkas UI:

```
| 7 | | Honor | Narasumber | | Pembekalan | | O/Pertemuan | | 400.000 |
```

Angkanya terbaca, kolomnya berantakan. Karena itu skill ini jujurnya adalah **pencari lokasi**, bukan kalkulator. Ia menemukan pos biayanya, membaca angkanya, lalu menyuruh Anda memverifikasi ke PDF asli. Jangan berpura-pura presisi yang tidak dimiliki.

PDF asli ada di `sources/` pada repo ini, yaitu `pmk-32-2025-sbm-ta2026.pdf` dan `pr-ui-16-2024-sb-ui-ta2024.pdf`.

## Cara menjawab, langkah demi langkah

**Langkah 1. Tentukan rezimnya.** Baca pertanyaannya. Kalau sumber dana disebut, ikuti itu. Kalau tidak disebut, dan pertanyaannya bisa dijawab dua-duanya, jawab keduanya berdampingan lalu jelaskan bedanya. Kalau bedanya besar dan berisiko salah pakai, tanyakan sumber dananya.

**Langkah 2. Orientasi lewat indeks.** Baca `indeks-*.md` yang relevan untuk menemukan pos biaya dan nomor barisnya. Indeks ini dibangun otomatis dari teks OCR, jadi sebagian judul terpotong dan sebagian pos terlewat. **Jangan berhenti di indeks.**

**Langkah 3. Cari dengan resep tahan-OCR.** Ini bagian terpenting, dan tempat skill ini paling mudah gagal kalau Anda salah langkah.

**Jangan pakai `grep` polos.** Ia akan gagal, dan gagalnya diam-diam: nol hasil, seolah posnya tidak ada. Penyebabnya, OCR menyelipkan pipa tabel dan spasi ganda di tengah frasa. Contoh nyata, baris 438 berkas UI aslinya begini:

```
| 1.  HONORARIUM  |     |     | DOSEN    |           | TAMU     |    ...
```

`grep -i "dosen tamu"` tidak akan menemukannya. Padahal itu judul posnya.

**Pakai resep ini.** Ia menormalkan pipa dan spasi lebih dulu. `sed` dan `tr` tidak menambah atau menghapus baris, jadi **nomor barisnya tetap akurat** terhadap berkas asli:

```bash
sed 's/|/ /g' references/sbm-kemenkeu-ta2026.md | tr -s ' ' | grep -n -i "pembawa acara"
sed 's/|/ /g' references/sb-ui-ta2024.md       | tr -s ' ' | grep -n -i "dosen tamu"
```

Kalau nihil, **mundur ke satu kata yang paling khas**. Pakai juga beberapa sinonim, karena dokumen memakai istilah formal yang mungkin bukan istilah si penanya: "uang harian" bukan "uang saku", "paket rapat/pertemuan di luar kantor" bukan "fullboard", "penginapan" bukan "hotel".

**Langkah 4. Baca konteksnya, jangan cuma barisnya.** Baca sekitar 30 baris di sekeliling temuan, dengan normalisasi yang sama supaya tabelnya terbaca:

```bash
sed -n '350,380p' references/sbm-kemenkeu-ta2026.md | sed 's/|/ /g' | tr -s ' '
```

Tarif SBM hampir selalu berjenjang: menurut eselon, golongan, provinsi, atau tingkat kegiatan. Satu baris tanpa konteks akan menyesatkan.

**Langkah 5. Baca penjelasan posnya.** Pada dokumen Kemenkeu, tabel tarif dan penjelasan terpisah letaknya. Penjelasan memuat syarat yang menentukan boleh tidaknya honor itu dibayarkan, misalnya batasan jumlah jam, atau syarat narasumber harus dari luar unit. **Tarif tanpa syarat adalah setengah jawaban.** Lihat kolom bagian di indeks: `L1-TARIF` versus `L1-PENJELASAN`.

**Langkah 6. Susun jawabannya** memakai template di bawah.

## Kamus satuan

Dari Lampiran I PMK 32/2025 (baris 4072 sampai 4081):

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

**Dokumen UI memakai notasi berbeda**, ditulis dengan garis miring dan kadang dieja: `O/J` (orang per jam), `O/Hadir` (orang per kehadiran), `O/B`, `O/Pertemuan`, `U/B`, `K` (kegiatan), `T` (tahun). Jangan menyamakan `OJ` gaya Kemenkeu dengan `O/J` gaya UI tanpa memeriksa. Baca satuannya apa adanya dari dokumen yang bersangkutan.

## Jebakan yang harus Anda hindari

**Tahun regulasi bukan tahun anggaran.** Sudah disebut di atas, dan ia jebakan nomor satu. PMK 32/2025 mengatur TA 2026.

**Data UI sudah berumur.** Standar Biaya UI yang ada di sini adalah TA 2024. Kalau UI sudah menerbitkan Peraturan Rektor yang lebih baru, angka di sini kedaluwarsa. **Selalu ingatkan pengguna soal ini pada setiap jawaban bersumber UI.** Jangan diam.

**Batas tertinggi versus dapat dilampaui.** Lampiran I PMK bersifat batas tertinggi, tidak boleh dilewati. Lampiran II bersifat dapat dilampaui sepanjang dapat dipertanggungjawabkan. Menyebut angka Lampiran II sebagai "batas maksimal" adalah kesalahan yang membuat orang menahan diri secara tidak perlu.

**Toleransi kabupaten tertentu.** Catatan Umum Lampiran I PMK (sekitar baris 3995) memuat tabel toleransi: sejumlah kabupaten boleh melampaui satuan biaya provinsinya, dengan rentang 115% sampai 303%. Contohnya Puncak Jaya di Papua Tengah, dan Kepulauan Mentawai di Sumatra Barat. Toleransi ini hanya berlaku untuk pos tertentu, yaitu pengadaan kendaraan operasional bus, sewa kendaraan, pengadaan kendaraan roda 2 dan roda 4, pengadaan pakaian dinas, dan konsumsi rapat. **Kalau pertanyaannya menyangkut daerah terpencil, periksa tabel ini.**

**Honorarium adalah nilai bruto.** Pada SB UI, Pasal 3 menyatakan besaran honorarium adalah nilai sebelum dipotong pajak penghasilan. Orang sering lupa ini lalu salah hitung penerimaan bersih.

**Efisiensi anggaran.** Catatan Umum Lampiran I PMK memerintahkan kegiatan seminar, rapat, dan perjalanan dinas dilakukan selektif dan diarahkan ke daring. Tarif yang tersedia bukan berarti tarif yang wajib dipakai.

## Bentuk jawaban

Sajikan seperti ini. Bahasa Indonesia, kalimat pendek, angka di depan.

> **Honorarium narasumber setingkat menteri: Rp‹BESARAN› per orang per jam (OJ).**
>
> Dasar: PMK Nomor 32 Tahun 2025, Lampiran I, pos nomor 9 (Honorarium Narasumber/Moderator/Pembawa Acara/Panitia). Berlaku untuk **Tahun Anggaran 2026**. Sifatnya **batas tertinggi**, tidak boleh dilampaui.
>
> Syarat yang menyertainya: ‹ringkas dari bagian penjelasan›
>
> Dibaca dari `references/sbm-kemenkeu-ta2026.md` baris ‹N› sampai ‹M›. Verifikasi ke `sources/pmk-32-2025-sbm-ta2026.pdf` sebelum dipakai di dokumen resmi.

Tanda `‹...›` di atas adalah **tempat kosong yang wajib Anda isi dari berkas**. Template ini sengaja tidak memuat angka rupiah satu pun, supaya tidak ada angka contoh yang tanpa sadar tersalin jadi jawaban.

Kalau menjawab dua rezim sekaligus, buat tabel berdampingan, lalu tutup dengan kalimat yang menegaskan mana yang berlaku bagi si penanya berdasarkan sumber dananya.

Kalau angkanya tidak ketemu, katakan tidak ketemu. Sebutkan kata kunci apa saja yang sudah dicoba, dan sarankan pengguna membuka PDF-nya. **Jangan mengarang.**
