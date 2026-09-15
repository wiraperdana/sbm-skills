# Skill SBM: Standar Biaya Masukan (Kemenkeu RI dan Universitas Indonesia)

Tiga skill untuk Claude Code yang menjawab pertanyaan tarif **Standar Biaya Masukan**, langsung dari teks regulasinya, bukan dari ingatan model.

| Skill | Cakupan | Sumber |
|---|---|---|
| `/sbm` | Dana APBN **dan** UI, berdampingan | Ketiganya |
| `/sbm-kemenkeu` | Dana APBN saja | PMK 32/2025 + Kepmen Diktisaintek 87/M/KEP/2026 |
| `/sbm-ui` | Universitas Indonesia saja, tarif dan kelengkapan dokumen pembayaran | PR UI 24/2026 + PR UI 10/2026 |

`/sbm-ui` juga menjawab pertanyaan kedua yang selalu menyusul soal tarif: dokumen apa yang wajib dilampirkan supaya pembayaran di UI diproses. Sumbernya PR UI 10/2026 tentang Standar Kelengkapan Dokumen Pembayaran. Aturan ini khusus dibawa `/sbm-ui`, karena ia Peraturan Rektor UI. Skill gabungan `/sbm` tidak membawanya, jadi pertanyaan dokumen pembayaran UI diajukan lewat `/sbm-ui`.

Aturan UI lama, PR UI 16/2024, sudah dicabut. Teksnya disimpan sebagai arsip di `references/arsip/` pada skill `/sbm` dan `/sbm-ui`. Skill hanya membukanya bila Anda memintanya secara eksplisit. Ia tidak pernah dipakai sebagai jawaban default, cadangan, atau saran.

Nama `/sbm-kemenkeu` dipertahankan meski isinya kini dua regulasi dari dua kementerian. Sumber utamanya tetap PMK Kemenkeu, dan mengganti nama skill hanya memutus alamat yang sudah biasa diketik.

## Kenapa ini ada

Tanyakan tarif SBM ke model bahasa mana pun, dan ia akan menjawab dengan percaya diri memakai angka yang diingatnya dari entah tahun berapa. Angka itu sering salah. Di dokumen anggaran, angka salah berbiaya nyata: revisi RAB, temuan auditor, dana ditolak.

Skill ini menutup celah itu dengan cara yang membosankan tapi benar. Ia membawa teks regulasinya sendiri, mencari angkanya di sana, mengutip nomor barisnya, lalu menyuruh Anda memverifikasi ke PDF asli.

## Yang paling sering disalahpahami: tahun regulasi bukan tahun anggaran

| Regulasi | Terbit | **Mengatur Tahun Anggaran** |
|---|---|---|
| PMK Nomor 32 Tahun 2025 | 2025 | **2026** |
| Kepmen Diktisaintek Nomor 87/M/KEP/2026 | 2026 | **2026** dan sesudahnya |
| Peraturan Rektor UI Nomor 24 Tahun 2026 | 2026 | **Tidak disebut.** Berlaku sejak 1 September 2026 sampai dicabut atau diubah |
| Peraturan Rektor UI Nomor 10 Tahun 2026 | 2026 | **Tidak disebut.** Berlaku sejak 1 April 2026. Ketentuan TOR, RAB, dan Renkom bagi Fakultas, Sekolah, dan Program Pendidikan Vokasi baru berlaku 1 Januari 2027 |

PMK terbit 2025, tapi isinya SBM untuk TA 2026. Jadi kalau Anda mencari "SBM 2026", dokumennya adalah PMK 32/2025 ini. Ketiga skill selalu menyebut kedua tahun itu supaya Anda tidak tertukar. Kepmen 87 kebetulan terbit di tahun anggaran yang diaturnya, jadi di situ tidak ada jebakan.

PR UI 24/2026 punya jebakan yang berlawanan: judulnya tidak menyebut tahun anggaran sama sekali. Skill menyebutnya dengan tanggal mulai berlaku, 1 September 2026. Aturan ini mencabut PR UI 16/2024 beserta lima perubahannya.

## Mana yang berlaku untuk saya

**Ikuti sumber dananya, bukan lembaganya.**

- Dana APBN (hibah kementerian, BRIN, DIKTI) → **SBM Kemenkeu**
- Honorarium tim peneliti berdana **DIPA Kemdiktisaintek** → **Kepmen 87/M/KEP/2026**, bersama PMK 32/2025
- Dana UI dan dana bantuan pendanaan PTN-BH → **SB UI**

Peneliti UI yang memakai hibah APBN tunduk pada SBM Kemenkeu, bukan SB UI. Angkanya bisa berbeda jauh. Kalau ragu, pakai `/sbm` dan ia akan menyajikan keduanya.

Pos yang tidak diatur SB UI mengikuti PMK tentang Standar Biaya Masukan, menurut Pasal 4 ayat (2) PR UI 24/2026.

## Dokumen pembayaran UI: tarif yang sah pun bisa ditolak

Tarif yang sesuai SB UI tetap dikembalikan unit keuangan kalau berkasnya kurang. PR UI 10/2026 mengatur berkas itu per jenis pembayaran, dari honorarium, hibah, dan perjalanan dinas sampai pengadaan dan uang muka. Berbeda dari SB UI, ruang lingkupnya tidak dipilah menurut sumber dana: ia berlaku untuk setiap Pengeluaran di seluruh Unit Kerja UI.

Dua ketentuan waktu paling sering terlewat:

1. **Pasal 123.** Ketentuan dokumen TOR, RAB, dan Renkom bagi Fakultas, Sekolah, dan Program Pendidikan Vokasi baru berlaku 1 Januari 2027.
2. **Pasal 122.** Pembayaran yang masih dalam proses pada 1 April 2026 diselesaikan menurut aturan lama, PR UI 17/2019. Teks aturan lama itu tidak dibawa skill ini.

## Honorarium tim peneliti: perlu dua dokumen, bukan satu

PMK 32/2025 pos nomor 7 mengatur honorarium **penunjang** penelitian, yaitu pembantu peneliti, pengolah data, petugas survei, dan pembantu lapangan. PMK itu tidak mengatur honorarium untuk penelitinya sendiri.

Lubang itu ditutup Kepmen Diktisaintek Nomor 87/M/KEP/2026, yang menetapkan Satuan Biaya Masukan Lainnya berupa honorarium tim pelaksana penelitian. Persetujuan Menteri Keuangan atas tarif ini tercantum di dokumennya, yaitu surat Nomor S-807/MK03/2025 tanggal 8 Desember 2025.

| Peran | Batas honorarium | Satuan |
|---|---|---|
| Ketua | 150% dari honorarium anggota | per bulan |
| Anggota | Rp2.400.000,00 | per bulan |
| Tenaga administratif | Rp820.000,00 | per bulan |
| Pembantu peneliti | Rp25.000,00 | per jam |

Tiga hal yang sering salah dipahami, dan ketiganya diingatkan skill di setiap jawaban:

1. **Ada pagu 25%.** Total honorarium seluruh tim paling banyak 25% dari dana penelitian yang disetujui. Dua batas ini berlaku bersamaan, dan yang lebih ketat yang menang.
2. **Honorarium tidak menambah dana.** Ia diambil dari dalam dana penelitian, bukan tambahan di luarnya.
3. **Honorarium ketua adalah angka turunan.** Ia 150% dari honorarium anggota yang dipakai di RAB, bukan 150% dari plafonnya.

Aturan ini hanya berlaku untuk penelitian berdana DIPA Kemdiktisaintek, sejak Tahun Anggaran 2026.

## Pasang

Salin folder skill ke direktori skill Claude Code Anda.

**Untuk semua project (global):**

```bash
git clone https://github.com/wiraperdana/sbm-skills.git
cd sbm-skills
./install.sh
```

**Manual, kalau Anda ingin memilih:**

```bash
mkdir -p ~/.claude/skills
cp -R skills/sbm            ~/.claude/skills/
cp -R skills/sbm-kemenkeu   ~/.claude/skills/
cp -R skills/sbm-ui         ~/.claude/skills/
```

**Untuk satu project saja**, salin ke `.claude/skills/` di dalam project itu.

Tiap folder skill sudah berdiri sendiri: teks regulasi dan indeksnya ikut di dalam `references/`. Anda boleh memasang hanya satu skill tanpa yang lain.

Setelah terpasang, panggil dengan `/sbm`, `/sbm-kemenkeu`, atau `/sbm-ui`.

## Contoh pertanyaan

```
/sbm berapa honorarium narasumber untuk pejabat eselon I?
/sbm-kemenkeu uang harian perjalanan dinas ke Papua berapa?
/sbm-ui honor dosen tamu bergelar guru besar berapa per jam?
/sbm saya bikin RAB hibah BRIN, tarif fullboard di Bandung berapa?
/sbm-kemenkeu honor ketua dan anggota tim peneliti hibah DIKTI berapa?
/sbm-ui dokumen apa saja untuk membayar honor narasumber dari luar UI lewat LS?
```

## Isi repo

```
skills/
  sbm/           SKILL.md + references/ (teks PMK + Kepmen 87 + UI 2026, plus indeksnya)
                 references/arsip/ (teks UI 2024 yang sudah dicabut)
  sbm-kemenkeu/  SKILL.md + references/ (teks PMK + Kepmen 87, plus indeksnya)
  sbm-ui/        SKILL.md + references/ (teks UI 2026 dan kelengkapan dokumen pembayaran UI, plus indeksnya)
                 references/arsip/ (teks UI 2024 yang sudah dicabut)
sources/
  pmk-32-2025-sbm-ta2026.pdf                         PDF asli, ground truth
  salinan-87-m-kep-2026.pdf                          PDF asli, ground truth
  pr-ui-24-2026-sb-ui-ta2026.pdf                     PDF asli, ground truth
  pr-ui-10-2026-standar-kelengkapan-pembayaran.pdf   PDF asli, ground truth
  pr-ui-16-2024-sb-ui-ta2024.pdf                     PDF asli, arsip, sudah dicabut
tools/
  build_index.py, render_index.py    Indeks dari teks OCR (PMK, arsip UI 2024)
  pdf_ke_teks.py                     Teks referensi dari PDF yang punya lapisan teks asli
  indeks_dari_daftar_lampiran.py     Indeks SB UI dari Daftar Lampiran dokumennya
  indeks_pasal.py                    Indeks per pasal untuk Peraturan Rektor tanpa lampiran tarif
```

## Keterbatasan, baca ini sebelum memakai

**Teks PMK 32/2025 hasil OCR, dan tabelnya rusak sebagian.** Angkanya terbaca, tetapi pipa tabel dan spasi ganda berserakan di tengah baris, jadi kolomnya berantakan. Karena itu skill ini jujurnya adalah **pencari lokasi**, bukan kalkulator. Ia menemukan pos biayanya dan membaca angkanya, lalu menyuruh Anda mengecek ke PDF. Skill ini dirancang untuk mengaku tidak tahu, bukan menebak.

**PDF asli disertakan justru untuk itu.** Verifikasi bukan formalitas. Untuk dokumen resmi, angkanya harus Anda konfirmasi sendiri ke PDF.

**Kepmen 87 adalah pengecualian yang lebih baik.** Dokumennya hanya 3 halaman, dan seluruh isinya sudah dicocokkan ke gambar halaman aslinya, bukan sekadar dilewatkan OCR. Angkanya bisa dipercaya. Verifikasi ke PDF tetap disarankan sebelum masuk dokumen resmi.

**Teks PR UI 24/2026 jauh lebih bersih.** PDF-nya diekspor dari Word, jadi teksnya diambil langsung dari lapisan teks asli, tanpa OCR. Verifikasinya memakai dua kanal. Seluruh 144 halaman di-OCR ulang, dan 776 dari 1.747 angka tarif terbaca identik. Lalu 25 halaman bertabel dilihat langsung, termasuk setiap halaman tempat OCR membaca angka berbeda, dan semua perbedaan itu ternyata salah baca OCR. Empat cacat berasal dari PDF-nya sendiri, misalnya tarif penginapan Kepulauan Riau kategori A yang tertulis `6.1 77.000`. Skill menyebutkan keempatnya dan melaporkannya sebagai ambigu.

**Teks PR UI 10/2026 juga diambil dari lapisan teks asli.** Dokumennya 63 halaman tanpa tabel, dan hanya 11 halaman yang memuat angka rupiah, tanggal, atau jangka waktu. Kesebelas halaman itu sudah dicocokkan ke gambarnya, ditambah halaman judul dan halaman 17, dan semuanya cocok. Indeksnya memuat 125 dari 125 pasal dengan nomor bersambung. Tanda tangan elektroniknya terbaca valid oleh `pdfsig`, tetapi rantai sertifikatnya belum bisa diperiksa di mesin pembuatnya. Empat cacat rumusan dari dokumen sumbernya dicatat di SKILL.md, misalnya negasi ganda di Pasal 110 ayat (2) huruf c.

**Aturan UI bisa berubah.** PR UI 24/2026 berlaku sejak 1 September 2026, dan pendahulunya diubah lima kali dalam dua tahun. Skill `/sbm-ui` mengingatkan hal ini di setiap jawaban, tapi ia tidak punya cara mengetahui apakah perubahan sudah terbit. Itu tugas Anda.

**Ini bukan produk resmi Kemenkeu maupun UI.** Ia alat bantu tidak resmi. Keputusan anggaran tetap ada pada Anda dan unit keuangan Anda.

## Memperbarui ke regulasi baru

Saat PMK atau Peraturan Rektor baru terbit:

1. Taruh PDF barunya di `sources/`.
2. Periksa apakah PDF-nya punya lapisan teks asli. Coba `pdftotext -f 1 -l 3 -layout <pdf> -`. Kalau teksnya terbaca rapi, pakai `tools/pdf_ke_teks.py`. Kalau kosong atau acak, PDF itu hasil pindaian dan perlu OCR.
3. Taruh teksnya di `references/` skill yang relevan, dengan nama yang memakai **tahun anggaran**, bukan tahun regulasi. Bila regulasinya tidak menyebut tahun anggaran, pakai tahun mulai berlakunya.
4. Bangun ulang indeksnya. Pakai `tools/indeks_dari_daftar_lampiran.py` untuk dokumen UI yang punya Daftar Lampiran, `tools/indeks_pasal.py` untuk Peraturan Rektor yang isinya pasal tanpa lampiran tarif, atau `tools/build_index.py` untuk teks OCR.
5. Verifikasi angkanya ke gambar halaman PDF.
6. Kalau regulasi baru mencabut yang lama, pindahkan teks lama ke `references/arsip/` dengan `git mv`, pasang blok peringatan di kepala berkasnya, dan tulis aturan buka-arsip di SKILL.md.
7. Perbarui tabel tahun di SKILL.md dan di README ini.

## Lisensi

Teks PMK dan Peraturan Rektor adalah dokumen resmi lembaga negara dan perguruan tinggi negeri, disertakan di sini apa adanya untuk keperluan rujukan.

Kerangka skill, indeks, dan perkakas di repo ini dilisensikan MIT. Lihat `LICENSE`.
