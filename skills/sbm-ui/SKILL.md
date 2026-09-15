---
name: sbm-ui
description: Menjawab pertanyaan tentang aturan keuangan internal Universitas Indonesia dari dua Peraturan Rektor. Pertama, Standar Biaya UI, yaitu PR UI Nomor 24 Tahun 2026 yang berlaku sejak 1 September 2026, untuk pertanyaan berapa besar tarifnya, misalnya honorarium dosen tamu, asisten dosen, kegiatan kemahasiswaan, hibah penelitian dan pengabdian masyarakat, honorarium kepanitiaan, perjalanan dinas UI, penginapan, uang harian, atau penerimaan mahasiswa baru. Kedua, Standar Kelengkapan Dokumen Pembayaran, yaitu PR UI Nomor 10 Tahun 2026 yang berlaku sejak 1 April 2026, untuk pertanyaan dokumen apa yang wajib dilampirkan saat mengajukan pembayaran, uang muka, atau pertanggungjawaban uang muka, misalnya TOR, RAB, Renkom, Daftar Nominatif, kuitansi, meterai, batas kas operasional, dan jenjang nilai pengadaan. Untuk tarif penelitian yang didanai APBN atau DIPA Kemdiktisaintek, skill ini mengarahkan ke sbm-kemenkeu. Aturan tarif lama PR 16/2024 tersimpan sebagai arsip dan hanya dibuka bila pengguna memintanya secara eksplisit. Sebut "sbm-ui" untuk memanggilnya.
---

# SB UI: Standar Biaya dan Kelengkapan Dokumen Pembayaran Universitas Indonesia

Skill ini menjawab **hanya dari aturan internal Universitas Indonesia yang berlaku**. Pertanyaan tarif untuk dana APBN, hibah kementerian, BRIN, atau DIKTI diarahkan ke skill lain, dan Anda wajib mengatakannya terus terang.

## Dua pertanyaan, dua regulasi

Skill ini membawa dua Peraturan Rektor yang saling melengkapi. Bayangkan kasir sebuah kantin. Daftar harga di dinding menentukan berapa yang boleh ditagih. Kasir juga meminta struk bertanda tangan sebelum uang keluar. Tanpa struk itu, pembayaran ditolak walau harganya sesuai daftar. Di UI, daftar harga itu PR UI 24/2026, dan syarat struknya PR UI 10/2026.

| Pertanyaan pengguna | Regulasi | Berlaku sejak | Bagian di berkas ini |
|---|---|---|---|
| "Berapa paling banyak boleh dibayar?" | PR UI Nomor 24 Tahun 2026 tentang Standar Biaya Universitas Indonesia | 1 September 2026 | Dari "Apa itu Standar Biaya UI" sampai "Bentuk jawaban tarif" |
| "Dokumen apa yang harus dilampirkan supaya pembayaran diproses?" | PR UI Nomor 10 Tahun 2026 tentang Standar Kelengkapan Dokumen Pembayaran | 1 April 2026 | "Kelengkapan dokumen pembayaran: PR UI 10/2026" |

Kenapa pemisahan ini penting: tarif yang sah tetap bisa gagal dibayar karena berkasnya kurang. Kalau pengguna menanyakan keduanya, jawab tarifnya dulu, lalu dokumennya, dan sebut tanggal berlaku masing-masing.

## Apa itu Standar Biaya UI

**Standar Biaya Universitas Indonesia (SB UI)** adalah daftar harga satuan resmi yang dipakai UI untuk melaksanakan kegiatan dan menyusun rencana kerja anggarannya (Pasal 1 angka 12). Peraturan Rektor ini menyamakan istilah SB UI dengan Standar Biaya Masukan. Ia menjawab pertanyaan "berapa paling banyak boleh dibayar untuk hal ini dari dana UI".

## Regulasi yang jadi sumber

| Hal | Isi |
|---|---|
| Nomor | Peraturan Rektor Universitas Indonesia Nomor 24 Tahun 2026 tentang Standar Biaya Universitas Indonesia |
| Ditetapkan | 7 Agustus 2026 |
| Mulai berlaku | **1 September 2026** (Pasal 12) |
| Tahun anggaran | **Tidak disebut.** Judulnya tidak memuat tahun, jadi ia berlaku sampai dicabut atau diubah |
| Yang dicabut | PR UI 16/2024 beserta seluruh perubahannya, terakhir PR UI 34/2025 (Pasal 11) |

**Cara menyebut waktunya di jawaban.** Tulis "berlaku sejak 1 September 2026". Hindari label "TA 2026", karena dokumennya sendiri tidak memakai label itu.

**Periksa perubahan.** Peraturan Rektor tentang SB UI lazim diubah beberapa kali selama masa berlakunya. Pendahulu aturan ini diubah lima kali dalam dua tahun. Karena itu, setiap jawaban ditutup dengan satu kalimat pengingat: pastikan belum terbit Peraturan Rektor yang mengubah PR 24/2026.

## Ruang lingkup, dan ke mana pertanyaan diarahkan

| Pasal | Ketentuan | Akibatnya bagi jawaban |
|---|---|---|
| 4 ayat (1) | Berlaku untuk kegiatan yang bersumber dari **dana UI** dan **dana bantuan pendanaan PTN-BH** | Dua sumber dana ini dijawab dari sini |
| 4 ayat (2) | Hal yang **belum diatur** di sini mengikuti **PMK tentang Standar Biaya Masukan** | Pos yang tidak ditemukan diarahkan ke `sbm-kemenkeu` |
| 5 ayat (1) | Kegiatan berdana **APBN atau APBD** mengikuti standar biaya masukan Pemerintah | Pertanyaan berdana APBN diarahkan ke `sbm-kemenkeu` |
| 5 ayat (2) | Kegiatan berdana **pihak lain lewat perikatan kerja sama** boleh memakai besaran berbeda yang ditetapkan UI | Sebutkan bahwa perjanjian kerja samanya bisa mengatur lain |
| 6 | **UKK** (Unit Kerja Khusus) boleh punya standar biaya sendiri, lewat Peraturan Rektor atau Peraturan Dekan dan Direktur Sekolah. Bila UKK tidak menyusunnya, PR 24/2026 yang berlaku | Kalau penanya bekerja di UKK, sebutkan kemungkinan ini |
| 2 | SB UI berfungsi sebagai **batasan tertinggi** atau **estimasi biaya** | Baca judul kolom tabelnya, lihat bagian "Sifat tarif" |
| 3 | Besaran honorarium adalah **nilai bruto**, sebelum dipotong pajak penghasilan | Sebutkan kalau yang ditanya honorarium |

**Pasal 4 ayat (2) adalah satu-satunya jalan keluar saat sebuah pos tidak ada di PR 24/2026.** Jalan keluarnya menuju PMK SBM. Arsip PR 16/2024 tidak pernah menjadi jalan keluar.

## Sifat tarif: baca judul kolom

Setiap tabel menyatakan sifatnya di judul kolom besaran. Konsekuensinya berbeda, jadi jangan menebak.

| Judul kolom | Arti | Contoh letaknya |
|---|---|---|
| `BESARAN TERTINGGI` | Batas atas, tidak boleh dilampaui | Sebagian besar tabel |
| `BESARAN ESTIMASI` | Perkiraan untuk perencanaan anggaran | Lampiran IV pos 1a (sewa kendaraan operasional kantor), Lampiran VI pos 3 dan 4 (tiket pesawat dalam dan luar negeri) |

Sebagian tabel hanya berjudul `KATEGORI` atau `BESARAN` tanpa keterangan, misalnya uang harian perjalanan dinas luar negeri. Untuk tabel seperti itu, katakan judul kolomnya tidak menyebut sifat tarif, lalu baca bagian Penjelasan di bawahnya.

## Kategori pegawai (Pasal 8)

Banyak tarif perjalanan dinas, penginapan, dan paket rapat berjenjang menurut kategori pegawai. Kategori ini khas UI, dan ia **tidak sama dengan eselon** gaya Kemenkeu.

| Kategori | Terdiri dari |
|---|---|
| A | Ketua dan sekretaris MWA, SA, DGB, Rektor, Wakil Rektor, kepala badan, sekretaris Universitas, Dekan, Direktur Sekolah, atau pejabat setara |
| B | Anggota MWA, SA, DGB, direktur, wakil Dekan, wakil Direktur Sekolah, kepala rumah sakit UI, kepala UKK, ketua dan sekretaris departemen, staf khusus Rektor, fungsional utama, atau pejabat setara |
| C | Kepala kantor, wakil direktur, kepala sub direktorat, sekretaris fakultas, manajer, ketua dan sekretaris program studi, kepala laboratorium, fungsional madya, atau pejabat setara |
| D | Kepala seksi, koordinator, sekretaris pimpinan, asisten manajer, atau pejabat setara |
| E | Pegawai UI selain kategori A sampai D |

Pegawai yang memegang jabatan manajerial dan fungsional di kategori berbeda memakai **kategori yang lebih tinggi** (Pasal 8 ayat 3). Tabel di atas ringkasan. Untuk kasus batas, baca Pasal 8 langsung di berkas teks.

## Penelitian berdana DIKTI tidak diatur di sini

Ini pengecualian yang paling sering terlewat, dan akibatnya mahal. Periksa lebih dulu sebelum menjawab pertanyaan apa pun soal honorarium penelitian.

Lampiran III memang memuat pos Penelitian, Inovasi, dan Pengabdian Masyarakat. Ia berlaku untuk penelitian berdana UI atau dana bantuan pendanaan PTN-BH. Penjelasan Lampiran III pos 2 menegaskan RAB proposal hibah **mengikuti pedoman pemberi hibah**, dan Pasal 5 ayat (1) menyerahkan kegiatan berdana APBN kepada standar biaya Pemerintah. Kalau dananya dari DIPA Kementerian Pendidikan Tinggi, Sains, dan Teknologi, yang berlaku adalah dua regulasi APBN ini:

| Yang mengatur | Untuk apa |
|---|---|
| **Kepmen Diktisaintek Nomor 87/M/KEP/2026** | Honorarium tim pelaksana penelitian: ketua, anggota, tenaga administratif, pembantu peneliti. Ada pagu 25% dari dana penelitian |
| **PMK Nomor 32 Tahun 2025** pos 7 | Honorarium penunjang penelitian: pengolah data, petugas survei, pembantu lapangan |

Keduanya ada di skill `sbm-kemenkeu`, dan juga di skill gabungan `sbm`.

**Jebakan yang tampak meyakinkan.** Plafon honorarium ketua dan anggota peneliti di Lampiran III pos 2 sama besar dengan plafon Kepmen 87. Aturan penyertanya berbeda. Kepmen 87 menambahkan pagu 25% dari dana penelitian dan batas tiga proyek per orang, dan ia menghitung honor ketua sebagai turunan dari honor anggota. Lampiran III pos 2 menulis plafon ketua sebagai angka tetap. Kesamaan angka tidak membuat kedua dokumen bisa dipertukarkan.

**Cara memeriksanya.** Kalau pertanyaannya menyangkut honorarium penelitian dan sumber dananya tidak disebut, **tanyakan dulu**. Nama institusi tidak menentukan aturannya. Peneliti UI yang memegang hibah DIKTI tunduk pada aturan APBN.

Kalau sumber dananya ternyata DIPA Kemdiktisaintek, katakan skill ini tidak mencakupnya, sebutkan nama regulasi yang benar, lalu arahkan ke `sbm-kemenkeu`. Jangan menyodorkan angka UI dengan catatan kecil, karena angka yang telanjur terlihat akan tersalin.

## Struktur dokumen PR 24/2026

Batang tubuh berisi 4 bab dan 12 pasal. Tarifnya ada di tujuh lampiran, total 104 pos biaya.

| Lampiran | Cakupan | Jumlah pos |
|---|---|---|
| **I** | Kegiatan Pendidikan | 13 |
| **II** | Kegiatan Kemahasiswaan | 27 |
| **III** | Penelitian, Inovasi, Pengabdian Masyarakat, Inkubasi Bisnis, Kekayaan Intelektual | 9 |
| **IV** | Penyelenggaraan Operasional Manajemen | 26 |
| **V** | Honorarium Kegiatan | 12 |
| **VI** | Perjalanan Dinas | 9 |
| **VII** | Penyelenggaraan Penerimaan Mahasiswa Baru | 8 |

## Aturan keras

1. **Jangan pernah menjawab dari ingatan.** Setiap angka tarif wajib dibaca langsung dari `references/sb-ui-ta2026.md`, dan setiap daftar dokumen dari `references/kelengkapan-pembayaran-ui-ta2026.md`. Angka salah atau berkas kurang di dokumen anggaran berbiaya nyata: revisi RAB, temuan auditor, pembayaran dikembalikan.
2. **Selalu sebut dasarnya.** Untuk tarif: Peraturan Rektor UI Nomor 24 Tahun 2026, lampiran keberapa, pos nomor berapa, dan tanggal berlakunya, 1 September 2026. Untuk dokumen: Peraturan Rektor UI Nomor 10 Tahun 2026, pasal dan ayatnya, dan tanggal berlakunya, 1 April 2026.
3. **Selalu sebut sifat tarifnya** menurut judul kolom tabel.
4. **Selalu cantumkan nomor baris dan halaman PDF** tempat angka atau daftar dibaca, plus perintah verifikasi ke PDF asli.
5. **Kalau teksnya ambigu, katakan ambigu.** Jangan membetulkan atau menebak.
6. **Arsip PR 16/2024 tertutup.** Ia hanya dibuka atas permintaan eksplisit pengguna. Aturan lengkapnya di bagian "Arsip PR UI 16/2024".
7. **Daftar dokumen disalin utuh.** Pertahankan huruf butir aslinya, termasuk butir bersyarat seperti "jika ada" atau "khusus untuk non pegawai UI". Meringkas atau menggabung butir membuat pengguna datang ke unit keuangan dengan berkas yang kurang.

## Sumber data dan mutunya

Di `references/`:

| Berkas | Isi |
|---|---|
| `sb-ui-ta2026.md` | Teks penuh PR UI 24/2026, 6.392 baris. Setiap halaman diawali penanda `[PDF hal. N]` |
| `indeks-ui-ta2026.md` | Peta 104 pos biaya per lampiran, dengan nomor baris dan halaman PDF |
| `kelengkapan-pembayaran-ui-ta2026.md` | Teks penuh PR UI 10/2026, 2.626 baris, dengan penanda `[PDF hal. N]` yang sama |
| `indeks-kelengkapan-pembayaran-ui-ta2026.md` | Peta 125 pasal per BAB dan Bagian, dengan nomor baris, halaman PDF, dan kalimat pembuka tiap pasal |
| `arsip/` | Teks dan indeks PR UI 16/2024. Tertutup, lihat bagian arsip |

Label `ta2026` pada nama berkas menandai tahun mulai berlaku. Konvensi yang sama dipakai berkas Kepmen 87 di skill `sbm-kemenkeu`, yang juga berlaku untuk tahun 2026 dan sesudahnya.

**Teksnya diambil dari lapisan teks asli PDF, tanpa OCR.** PDF-nya diekspor dari Word, jadi setiap huruf dan angka tersimpan sebagai teks. Tata letak tabel dipertahankan dengan `pdftotext -layout`. Hasilnya diverifikasi lewat dua kanal yang independen. Pertama, seluruh 144 halaman di-OCR ulang dari gambarnya. Dari 1.747 angka tarif di lapisan teks, 776 terbaca identik oleh OCR, dan sisanya kebanyakan gagal terbaca karena garis tabel. Kedua, 25 halaman bertabel dilihat langsung, yaitu sampel dari ketujuh lampiran ditambah setiap halaman tempat OCR membaca angka yang berbeda. Di semua halaman itu angka lapisan teks cocok dengan gambar, dan setiap perbedaan ternyata salah baca OCR. Halaman lainnya belum dicocokkan mata satu per satu, jadi verifikasi ke PDF tetap langkah wajib sebelum angka masuk dokumen resmi.

**Empat cacat yang ada di dokumen sumbernya sendiri.** Ini salah ketik UI, dan ekstraksi teks mereproduksinya dengan setia.

| Letak | Yang tertulis di PDF | Cara menjawab |
|---|---|---|
| Lampiran VI pos 7, Penginapan Dalam Negeri, Kepulauan Riau kategori A | `6.1 77.000` | Sampaikan apa adanya sebagai ambigu, lalu suruh pengguna mengonfirmasi ke unit keuangan |
| Lampiran III pos 2, Pengolah Data Penelitian/Perekayasaan | Kolom SATUAN berisi "Penelitian/Perekayasaan" | Katakan satuannya tidak tertulis jelas |
| Lampiran I pos 1, judul | `HONORARIUM DOSEN TAM` | Tidak memengaruhi angka. Kata kunci "dosen tamu" tetap menemukan baris tabelnya |
| Daftar Lampiran, PDF halaman 9 sampai 12 | Bertanda air "DRAFT" | Daftar itu hanya alat navigasi. Batang tubuh dan ketujuh lampiran bersih dan ditandatangani elektronik. Sebutkan ini bila pengguna meragukan keabsahannya |

**Label baris bisa terbelah.** Tabel dengan uraian panjang menaruh huruf baris dan angkanya di tengah label. Contoh nyata dari Lampiran I pos 2:

```
                    Asisten berstatus mahasiswa
               g                                                         O/Hadir                          205.000
                    pada Program S1 RPL
```

Labelnya "Asisten berstatus mahasiswa pada Program S1 RPL", terbelah di atas dan di bawah baris angka. **Selalu baca satu atau dua baris di atas dan di bawah angka** sebelum menyimpulkan labelnya.

## Cara menjawab pertanyaan tarif, langkah demi langkah

**Langkah 1. Pastikan sumber dananya.** Dana UI atau dana bantuan pendanaan PTN-BH dijawab dari sini. Dana APBN diarahkan keluar. Kalau tidak disebut dan tarifnya bisa berbeda besar, tanyakan.

**Langkah 2. Tentukan lampirannya, lalu buka indeks.** Buka `indeks-ui-ta2026.md`. Indeks itu memetakan seluruh 104 pos yang tercantum di Daftar Lampiran.

**Langkah 3. Cari dengan resep tahan-spasi.** Teks dokumen ini rata kanan-kiri, jadi di banyak baris antar-kata terselip spasi ganda. `grep` polos gagal diam-diam pada baris seperti itu. Contoh nyata:

```bash
grep -n -i "bantuan pelaksanaan" references/sb-ui-ta2026.md
# hanya menemukan baris 4280, sebuah butir penjelasan

tr -s ' ' < references/sb-ui-ta2026.md | grep -n -i "bantuan pelaksanaan"
# menemukan baris 341 (Daftar Lampiran) dan baris 1296 (judul pos yang dicari)
```

`tr -s ' '` meringkas spasi beruntun tanpa menambah atau menghapus baris, jadi **nomor barisnya tetap akurat**. Temuan di bawah baris 560 berasal dari batang tubuh atau Daftar Lampiran, sedangkan tarifnya ada di baris 560 ke atas.

Kalau masih nihil, mundur ke satu kata yang paling khas, dan coba sinonim. Dokumen memakai istilah formal: "uang harian" untuk uang saku perjalanan, "paket rapat/pertemuan di luar kantor" untuk fullboard, "penginapan" untuk hotel.

**Langkah 4. Baca konteksnya, lalu catat halaman PDF-nya.** Baca sekitar 40 baris di sekeliling temuan:

```bash
sed -n '1290,1335p' references/sb-ui-ta2026.md | tr -s ' '
```

Halaman PDF untuk rujukan adalah penanda `[PDF hal. N]` terdekat di atas baris temuan:

```bash
awk 'NR<=1296 && /^\[PDF hal\./ {p=$0} NR==1296 {print p; exit}' references/sb-ui-ta2026.md
```

Tarif UI berjenjang menurut jabatan, gelar, kategori pegawai, provinsi, atau tingkat kegiatan. Satu baris tanpa konteks akan menyesatkan.

**Langkah 5. Baca Penjelasan di bawah tabel.** Hampir setiap pos diikuti blok "Penjelasan" yang memuat syarat pembayaran, batas frekuensi, atau siapa yang berhak. Tarif tanpa syarat adalah setengah jawaban.

**Langkah 6. Susun jawabannya** memakai template di bawah.

## Kamus satuan

Pasal 9 menetapkan singkatannya:

| Singkatan | Arti |
|---|---|
| `O` | Orang |
| `Mhs` | Mahasiswa |
| `J` | Jam |
| `H` | Hari |
| `B` | Bulan |
| `T` | Tahun |
| `K` | Kegiatan |
| `P` | Paket |
| `U` | Unit |

Singkatan itu digabung dengan garis miring. `O/J` berarti orang per jam, `O/K` orang per kegiatan, `U/T` unit per tahun. Tiga variasi perlu dikenali:

1. **Spasi yang terselip.** `O/ J` sama dengan `O/J`.
2. **Satuan yang dieja.** Contohnya `O/Sesi`, `O/Kali`, `O/Judul`, `O/Pendaftar`, `O/Butir Soal`, `Kelompok`, dan `Permohonan`.
3. **Mata uang asing.** Sebagian tabel dinyatakan dalam dolar AS. Tandanya tulisan `(Dalam USD)` di atas tabel atau `USD` di depan angka. Tabel USD memakai **koma** sebagai pemisah ribuan, misalnya `6,778`, sedangkan tabel rupiah memakai titik.

`at cost` berarti dibayar sebesar pengeluaran aktual.

**Jangan menyamakan `O/J` gaya UI dengan `OJ` gaya Kemenkeu tanpa memeriksa.** Baca satuannya apa adanya dari baris yang bersangkutan.

## Arsip PR UI 16/2024: tertutup kecuali diminta

PR UI 16/2024 sudah dicabut. Teksnya disimpan di `references/arsip/` supaya tetap bisa dirujuk. Ia **tidak pernah** menjadi sumber jawaban default.

**Arsip boleh dibuka hanya bila pengguna memintanya secara eksplisit.** Contoh permintaan eksplisit:

- menyebut "PR 16/2024", "Peraturan Rektor 16 Tahun 2024", atau "SB UI 2024";
- meminta "aturan lama" atau "aturan sebelumnya";
- meminta perbandingan tarif lama dengan tarif sekarang.

**Hal-hal berikut bukan permintaan, jadi arsip tetap tertutup:**

- sebuah pos tidak ditemukan di PR 24/2026. Jalan keluarnya Pasal 4 ayat (2), yaitu PMK SBM;
- pengguna menyebut kegiatan tahun 2025 atau bulan sebelum September 2026;
- pengguna menulis "SB UI" tanpa tahun;
- angka di PR 24/2026 ambigu atau cacat.

**Selama arsip tertutup, tiga hal dilarang:**

1. Menawarkan arsip, misalnya "kalau mau, saya bisa cek aturan 2024".
2. Menyebut angka dari arsip, termasuk sebagai pembanding atau konteks.
3. Menyarankan pengguna memakai aturan lama.

**Kegiatan yang dilaksanakan sebelum 1 September 2026.** Pasal 10 PR 24/2026 menyatakan kegiatan seperti itu mengacu pada PR 16/2024 beserta perubahannya. Kalau pertanyaan pengguna jelas menyangkut kegiatan sebelum tanggal itu, sampaikan isi Pasal 10 sebagai fakta hukum dari aturan yang berlaku, lalu berhenti di situ. Jangan menyebut angka lama, dan jangan menawarkan membuka arsip.

**Saat arsip dibuka atas permintaan eksplisit:**

1. Baca dari `references/arsip/sb-ui-ta2024.md` dan `references/arsip/indeks-ui-ta2024.md`. Blok peringatan di kepala berkas itu menjelaskan statusnya.
2. Tandai setiap angka dengan "PR UI 16/2024, sudah dicabut".
3. Sampaikan bahwa teks arsip itu versi asli hasil OCR, dan **lima perubahannya belum masuk**, termasuk yang terakhir, PR UI 34/2025. Angkanya bisa berbeda dari yang benar-benar berlaku sampai 31 Agustus 2026.
4. Rujuk PDF-nya di `sources/pr-ui-16-2024-sb-ui-ta2024.pdf`.
5. Teks arsip hasil OCR dengan tabel rusak. Pakai resep `sed 's/|/ /g' references/arsip/sb-ui-ta2024.md | tr -s ' ' | grep -n -i "<kata>"`.
6. Jawaban arsip tidak ditutup dengan rekomendasi memakai angka lama.

## Bentuk jawaban tarif

Sajikan seperti ini. Bahasa Indonesia, kalimat pendek, angka di depan.

> **Honorarium dosen tamu bergelar Doktor: Rp‹BESARAN› per orang per jam (O/J).**
>
> Dasar: Peraturan Rektor UI Nomor 24 Tahun 2026, **Lampiran I** (Kegiatan Pendidikan), pos nomor 1 (Honorarium Dosen Tamu). Berlaku sejak **1 September 2026**. Sifatnya **‹batas tertinggi atau estimasi›**, sesuai judul kolom tabelnya.
>
> Syarat yang menyertainya: ‹ringkas dari bagian Penjelasan›
>
> Besaran ini **bruto**, sebelum potongan pajak penghasilan (Pasal 3).
>
> Dibaca dari `references/sb-ui-ta2026.md` baris ‹N› sampai ‹M›. Verifikasi ke `sources/pr-ui-24-2026-sb-ui-ta2026.pdf` halaman ‹P› sebelum dipakai di dokumen resmi. Pastikan juga belum terbit Peraturan Rektor yang mengubah PR 24/2026.

Tanda `‹...›` di atas adalah **tempat kosong yang wajib Anda isi dari berkas**. Template ini sengaja tidak memuat angka rupiah satu pun, supaya tidak ada angka contoh yang tanpa sadar tersalin jadi jawaban.

**Kalau angkanya tidak ketemu,** katakan tidak ketemu di PR 24/2026. Sebutkan kata kunci yang sudah dicoba. Lalu sampaikan Pasal 4 ayat (2): hal yang belum diatur mengikuti PMK tentang Standar Biaya Masukan, dan arahkan ke `sbm-kemenkeu` atau `sbm`. **Jangan mengarang, dan jangan membuka arsip.**

**Kalau pertanyaannya ternyata menyangkut dana APBN,** katakan skill ini hanya mencakup aturan internal UI, lalu arahkan ke `sbm-kemenkeu` atau `sbm`. Untuk honorarium tim peneliti berdana DIPA Kemdiktisaintek, sebutkan juga nama regulasinya, yaitu Kepmen Diktisaintek Nomor 87/M/KEP/2026, supaya pengguna tahu apa yang dicarinya.

## Kelengkapan dokumen pembayaran: PR UI 10/2026

Bagian ini menjawab pertanyaan "berkas apa yang wajib ada". PR UI 10/2026 tidak memuat tarif. Pertanyaan besaran tetap dijawab dari PR UI 24/2026.

### Regulasi yang jadi sumber

| Hal | Isi |
|---|---|
| Nomor | Peraturan Rektor Universitas Indonesia Nomor 10 Tahun 2026 tentang Standar Kelengkapan Dokumen Pembayaran |
| Ditetapkan | 27 Maret 2026 |
| Mulai berlaku | **1 April 2026** (Pasal 125) |
| Yang dicabut | PR UI 17/2019 tentang Standar Kelengkapan Dokumen Pembayaran Universitas Indonesia (Pasal 124) |
| Struktur | 20 BAB, 125 pasal, 63 halaman. Tidak ada lampiran, jadi seluruh daftar dokumen ada di batang tubuh |
| Keabsahan | Ditandatangani elektronik oleh Rektor. Setiap halaman memuat catatan sertifikat BSrE |

**Periksa perubahan.** Tutup setiap jawaban dokumen dengan pengingat: pastikan belum terbit Peraturan Rektor yang mengubah PR 10/2026.

### Ruang lingkup (Pasal 4)

PR UI 10/2026 berlaku untuk **setiap Pengeluaran pada seluruh Unit Kerja di UI**, baik dokumen fisik maupun elektronik. Ia juga mengatur empat mekanisme pengajuan: kas operasional, LS, uang muka kegiatan, dan pertanggungjawaban uang muka.

Perhatikan bedanya dengan PR 24/2026. Pasal 4 PR 10/2026 tidak memilah menurut sumber dana. Pasal 29 ayat (2) bahkan menyebut hibah penelitian boleh bersumber dari internal UI, pemerintah, swasta, atau lembaga di dalam dan luar negeri. Karena itu, pertanyaan dokumen untuk hibah eksternal tetap dijawab dari sini. Sebutkan juga bahwa pemberi hibah bisa menambah syarat lewat perjanjiannya, sesuai Pasal 30 ayat (1) huruf d dan ayat (4) huruf e.

### Tiga ketentuan waktu yang wajib diperiksa

Ketiganya bisa membalik jawaban, jadi periksa sebelum menyalin daftar dokumen.

1. **Pasal 123, TOR, RAB, dan Renkom bagi Fakultas.** Ketentuan dokumen TOR, RAB, dan/atau Renkom baru berlaku **1 Januari 2027** bagi Fakultas, Sekolah, dan Program Pendidikan Vokasi. Sebagian besar pasal kelengkapan memuat salah satu dokumen itu, jadi ketentuan ini menyentuh banyak jawaban. Kalau pengaju berada di Fakultas, Sekolah, atau Program Pendidikan Vokasi dan tanggal pengajuannya sebelum 1 Januari 2027, sampaikan isi Pasal 123. PR 10/2026 tidak menyebut apa yang berlaku bagi mereka sebelum tanggal itu. Katakan hal itu terus terang, lalu sarankan konfirmasi ke unit keuangan fakultasnya. Unit Kerja lain, misalnya di PAU, tidak disebut Pasal 123, jadi bagi mereka ketentuan itu berlaku sejak 1 April 2026.
2. **Pasal 122, pembayaran yang sudah berjalan.** Kelengkapan yang diproses sebelum 1 April 2026 tetap sah. Kelengkapan yang masih dalam proses pada tanggal itu diselesaikan menurut PR UI 17/2019. Skill ini tidak membawa teks PR UI 17/2019. Sampaikan faktanya, arahkan ke unit keuangan, dan jangan mengarang isi aturan lama itu.
3. **Perubahan.** Lihat pengingat di atas.

### Angka yang ada di PR 10/2026

Dokumen ini hanya memuat sedikit angka. Semuanya sudah dicocokkan ke gambar halaman PDF. Tabel ini peta, jadi tetap baca pasalnya sebelum menjawab.

| Ketentuan | Angka | Dasar | Hal. PDF |
|---|---|---|---|
| Meterai pada bukti transaksi | Rp10.000 untuk nilai transaksi di atas Rp5.000.000 | Pasal 7 ayat (2) huruf f | 9 |
| Pembayaran wajib LS, kecuali tunai lewat kas operasional | Sampai dengan Rp10.000.000 | Pasal 8 ayat (1), Pasal 109 ayat (2) huruf a | 9, 56 |
| Permintaan Pembayaran remunerasi ke unit keuangan | Paling lambat tanggal 20 | Pasal 10 ayat (4) | 11 |
| Transfer remunerasi oleh unit keuangan | Paling lambat tanggal 25 | Pasal 10 ayat (5) | 11 |
| Jatuh tempo overnight dan deposito on call | 1 sampai 3 hari | Pasal 80 ayat (2) | 42 |
| Pembelian langsung | Sampai dengan Rp50.000.000 | Pasal 91 dan Pasal 92 | 46 |
| E-purchasing | Paling sedikit Rp50.000.000 | Pasal 93 | 47 |
| Pengadaan langsung | Lebih dari Rp50.000.000 sampai dengan Rp300.000.000 | Pasal 94 | 47 |
| Penunjukan langsung, tender, tender cepat, tender itemized, seleksi, kontes | Lebih dari Rp300.000.000 | Pasal 95 | 48 |
| Surat perintah kerja sampai Rp300.000.000, perjanjian di atasnya | Jamuan dan kudapan, serta uang muka pengadaan | Pasal 104 huruf e, Pasal 118 ayat (1) huruf b | 54, 60 |

### Istilah yang dipakai di daftar dokumen

Definisinya dari Pasal 1, kecuali disebut lain. Pengguna sering hanya mengenal singkatannya, jadi jelaskan pada pemakaian pertama.

| Istilah | Arti ringkas |
|---|---|
| TOR (Terms of Reference) | Rancangan kerja, kegiatan, dan keuangan yang dibuat sebelum kegiatan dilaksanakan |
| RAB (Rencana Anggaran Biaya) | Rincian anggaran dan biaya kegiatan yang diusulkan Entitas Anggaran |
| Renkom (Rencana Komitmen) | Rencana pelaksanaan dan pemantauan anggaran berdasarkan RAB yang disetujui, dasar komitmen belanja |
| LS (Pembayaran Melalui Transfer) | Pembayaran yang ditransfer langsung ke rekening penerima |
| Kas operasional | Pengisian kembali kas yang sudah terpakai untuk kegiatan operasional (Pasal 109) |
| Uang muka kegiatan | Uang muka kerja untuk transaksi yang memenuhi kriteria uang muka, lalu dipertanggungjawabkan (Pasal 116) |
| Daftar Nominatif | Rincian remunerasi, honorarium, bantuan, atau sejenisnya per penerima, lengkap dengan satuan, volume, besaran, dan PPh |
| Daftar Rekening Bank | Nama penerima, nomor rekening, bank, besaran, dan email notifikasi |
| BAST | Berita Acara Serah Terima Pekerjaan, antara Penyedia dan pejabat pembuat komitmen |
| BAP | Berita Acara Pembayaran, nilai yang dibayar sesuai bobot pekerjaan |
| PAU | Pusat Administrasi Universitas, perangkat administrasi Rektor |

### Cara menjawab pertanyaan dokumen, langkah demi langkah

**Langkah 1. Kenali jenis pembayaran dan mekanismenya.** Satu jenis pembayaran sering punya pasal berbeda untuk tiap mekanisme. Contohnya:

| Jenis | Pasal per mekanisme |
|---|---|
| Perjalanan dinas dalam negeri | Pasal 44 ayat (1) pengajuan uang muka, Pasal 44 ayat (2) pertanggungjawaban, Pasal 45 LS, Pasal 47 bila berbentuk bantuan |
| Perjalanan dinas luar negeri | Pasal 49 ayat (1) dan (2), Pasal 50 LS, Pasal 51 bantuan |
| Honorarium dosen tamu, narasumber, moderator | Pasal 23 umum, Pasal 24 pihak luar UI lewat uang muka atau kas operasional, Pasal 114 kas operasional, Pasal 120 uang muka |
| Pengadaan barang dan jasa | Pasal 91 sampai 95 menurut nilai dan metode, Pasal 97 sampai 108 pengadaan khusus, Pasal 110 kas operasional, Pasal 118 uang muka |

Kalau mekanismenya tidak disebut dan daftarnya berbeda, tanyakan dulu, atau sajikan per mekanisme dengan label yang jelas.

**Langkah 2. Buka indeks.** Buka `indeks-kelengkapan-pembayaran-ui-ta2026.md`. Kolom Bagian dan Pokok membantu memilih pasal. Jangan menyusun daftar dari indeks, karena kolom Pokok hanya potongan kalimat pembuka.

**Langkah 3. Cari dengan resep tahan-spasi.** Teksnya rata kanan-kiri, jadi pakai resep yang sama dengan bagian tarif:

```bash
tr -s ' ' < references/kelengkapan-pembayaran-ui-ta2026.md | grep -n -i "narasumber"
```

Tiga jebakan pencarian khas dokumen ini:

1. **"e-purchasing" terpenggal di akhir baris** di Pasal 93, jadi carilah `purchasing`.
2. **Salah ketik "requitition"** untuk *purchase requisition*. Carilah `purchase order`.
3. **"Kerjasama" ditulis sambung.** Carilah `kerjasama`.

**Langkah 4. Baca pasalnya utuh.** Pasal berakhir tepat sebelum baris pasal berikutnya di indeks. Contoh untuk Pasal 23, yang dimulai di baris 687, sedangkan Pasal 24 di baris 710:

```bash
sed -n '687,709p' references/kelengkapan-pembayaran-ui-ta2026.md | tr -s ' '
```

Daftar bisa menyeberang halaman. Penanda `[PDF hal. N]` di tengah daftar bukan akhir pasal.

**Langkah 5. Tambahkan syarat umum yang ikut berlaku.** Pasal 7 ayat (1) mewajibkan setiap pengajuan menyertakan Permintaan Pembayaran dari sistem keuangan dan dokumen pendukung. Pasal 7 ayat (2) mengatur syarat sah kuitansi, invoice, nota kontan, dan bon, termasuk meterai. Pasal 8 mengatur kapan wajib LS. Sebutkan yang relevan dengan pertanyaan.

**Langkah 6. Periksa Pasal 123 dan Pasal 122.** Lihat "Tiga ketentuan waktu yang wajib diperiksa".

**Langkah 7. Susun jawabannya** memakai template di bawah.

### Cacat di dokumen sumbernya sendiri

Ekstraksi teks mereproduksinya dengan setia. Laporkan apa adanya.

| Letak | Yang tertulis di PDF | Cara menjawab |
|---|---|---|
| Pasal 23 huruf h dan i | "Daftar Nominatif; dan", lalu "Daftar Rekening Bank; dan", lalu masih ada huruf j | Salin sepuluh butir, huruf a sampai j. Kata "dan" ganda tidak menghapus butir j |
| Pasal 110 ayat (2) huruf c | "laporan kegiatan, jika bukan merupakan konsumsi tidak rapat rutin" | Negasi ganda ini ambigu. Sampaikan apa adanya. Boleh menyebut bahwa Pasal 91 ayat (1) huruf h dan Pasal 94 ayat (1) huruf k memakai rumusan "konsumsi selain untuk rapat rutin", tanpa menyimpulkan maksudnya sama |
| Pasal 91 dan 92 terhadap Pasal 93 | "sampai dengan Rp50.000.000" dan "paling sedikit Rp50.000.000" | Nilai tepat Rp50.000.000 masuk dua rentang, untuk dua metode berbeda. Sebutkan keduanya bila nilainya tepat di batas |
| Pasal 49 ayat (1) huruf g dan Pasal 50 huruf g, terhadap Pasal 51 huruf g | "pegawai negeri sipil" dan "aparatur sipil negeri" | Kutip istilahnya per pasal, apa adanya |

### Bentuk jawaban dokumen

> **Dokumen pembayaran ‹jenis pembayaran›, mekanisme ‹LS, kas operasional, atau uang muka›: ‹jumlah butir› butir.**
>
> Dasar: Peraturan Rektor UI Nomor 10 Tahun 2026 tentang Standar Kelengkapan Dokumen Pembayaran, **Pasal ‹N› ‹ayat bila ada›**. Berlaku sejak **1 April 2026**.
>
> ‹a. butir pertama, disalin utuh›
> ‹b. dan seterusnya›
>
> Syarat umum yang ikut berlaku: ‹Pasal 7 dan Pasal 8 yang relevan›
>
> ‹Bila pengaju di Fakultas, Sekolah, atau Program Pendidikan Vokasi dan pengajuan sebelum 1 Januari 2027: isi Pasal 123›
>
> Dibaca dari `references/kelengkapan-pembayaran-ui-ta2026.md` baris ‹N› sampai ‹M›. Verifikasi ke `sources/pr-ui-10-2026-standar-kelengkapan-pembayaran.pdf` halaman ‹P› sebelum berkas diajukan. Pastikan juga belum terbit Peraturan Rektor yang mengubah PR 10/2026.

**Kalau jenis pembayarannya tidak ketemu,** katakan tidak ketemu di PR 10/2026 dan sebutkan kata kunci yang sudah dicoba. Sampaikan syarat umum Pasal 7 ayat (1), lalu arahkan ke unit keuangan. **Jangan menyusun daftar dengan meminjam pasal jenis pembayaran lain**, karena daftar antarpasal berbeda di butir-butir kecil.

**Kalau pertanyaannya menggabung tarif dan dokumen,** pakai template tarif lebih dulu, lalu template dokumen. Sebut kedua tanggal berlaku, 1 September 2026 dan 1 April 2026, supaya pengguna tidak mengira keduanya satu aturan.
