# Skill SBM: Standar Biaya Masukan (Kemenkeu RI dan Universitas Indonesia)

Tiga skill untuk Claude Code yang menjawab pertanyaan tarif **Standar Biaya Masukan**, langsung dari teks regulasinya, bukan dari ingatan model.

| Skill | Cakupan | Sumber |
|---|---|---|
| `/sbm` | Dana APBN **dan** UI, berdampingan | Ketiganya |
| `/sbm-kemenkeu` | Dana APBN saja | PMK 32/2025 + Kepmen Diktisaintek 87/M/KEP/2026 |
| `/sbm-ui` | Universitas Indonesia saja | PR UI 16/2024 |

Nama `/sbm-kemenkeu` dipertahankan meski isinya kini dua regulasi dari dua kementerian. Sumber utamanya tetap PMK Kemenkeu, dan mengganti nama skill hanya memutus alamat yang sudah biasa diketik.

## Kenapa ini ada

Tanyakan tarif SBM ke model bahasa mana pun, dan ia akan menjawab dengan percaya diri memakai angka yang diingatnya dari entah tahun berapa. Angka itu sering salah. Di dokumen anggaran, angka salah berbiaya nyata: revisi RAB, temuan auditor, dana ditolak.

Skill ini menutup celah itu dengan cara yang membosankan tapi benar. Ia membawa teks regulasinya sendiri, mencari angkanya di sana, mengutip nomor barisnya, lalu menyuruh Anda memverifikasi ke PDF asli.

## Yang paling sering disalahpahami: tahun regulasi bukan tahun anggaran

| Regulasi | Terbit | **Mengatur Tahun Anggaran** |
|---|---|---|
| PMK Nomor 32 Tahun 2025 | 2025 | **2026** |
| Kepmen Diktisaintek Nomor 87/M/KEP/2026 | 2026 | **2026** dan sesudahnya |
| Peraturan Rektor UI Nomor 16 Tahun 2024 | 2024 | **2024** |

PMK terbit 2025, tapi isinya SBM untuk TA 2026. Jadi kalau Anda mencari "SBM 2026", dokumennya adalah PMK 32/2025 ini. Ketiga skill selalu menyebut kedua tahun itu supaya Anda tidak tertukar. Kepmen 87 kebetulan terbit di tahun anggaran yang diaturnya, jadi di situ tidak ada jebakan.

## Mana yang berlaku untuk saya

**Ikuti sumber dananya, bukan lembaganya.**

- Dana APBN (hibah kementerian, BRIN, DIKTI) → **SBM Kemenkeu**
- Honorarium tim peneliti berdana **DIPA Kemdiktisaintek** → **Kepmen 87/M/KEP/2026**, bersama PMK 32/2025
- Dana internal UI → **SB UI**

Peneliti UI yang memakai hibah APBN tunduk pada SBM Kemenkeu, bukan SB UI. Angkanya bisa berbeda jauh. Kalau ragu, pakai `/sbm` dan ia akan menyajikan keduanya.

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
```

## Isi repo

```
skills/
  sbm/           SKILL.md + references/ (teks PMK + Kepmen 87 + UI, plus indeksnya)
  sbm-kemenkeu/  SKILL.md + references/ (teks PMK + Kepmen 87, plus indeksnya)
  sbm-ui/        SKILL.md + references/ (teks UI, plus indeksnya)
sources/
  pmk-32-2025-sbm-ta2026.pdf         PDF asli, ground truth
  salinan-87-m-kep-2026.pdf          PDF asli, ground truth
  pr-ui-16-2024-sb-ui-ta2024.pdf     PDF asli, ground truth
```

## Keterbatasan, baca ini sebelum memakai

**Teks regulasinya hasil OCR, dan tabelnya rusak sebagian.** Contoh nyata dari berkas UI:

```
| 7 | | Honor | Narasumber | | Pembekalan | | O/Pertemuan | | 400.000 |
```

Angkanya terbaca, kolomnya berantakan. Karena itu skill ini jujurnya adalah **pencari lokasi**, bukan kalkulator. Ia menemukan pos biayanya dan membaca angkanya, lalu menyuruh Anda mengecek ke PDF. Skill ini dirancang untuk mengaku tidak tahu, bukan menebak.

**PDF asli disertakan justru untuk itu.** Verifikasi bukan formalitas. Untuk dokumen resmi, angkanya harus Anda konfirmasi sendiri ke PDF.

**Kepmen 87 adalah pengecualian yang lebih baik.** Dokumennya hanya 3 halaman, dan seluruh isinya sudah dicocokkan ke gambar halaman aslinya, bukan sekadar dilewatkan OCR. Angkanya bisa dipercaya. Verifikasi ke PDF tetap disarankan sebelum masuk dokumen resmi.

**Data UI berumur.** SB UI di sini adalah TA 2024. Kalau UI sudah menerbitkan Peraturan Rektor yang lebih baru, angkanya kedaluwarsa. Skill `/sbm-ui` memperingatkan hal ini di setiap jawaban, tapi ia tidak punya cara mengetahui apakah aturan baru sudah ada. Itu tugas Anda.

**Ini bukan produk resmi Kemenkeu maupun UI.** Ia alat bantu tidak resmi. Keputusan anggaran tetap ada pada Anda dan unit keuangan Anda.

## Memperbarui ke regulasi baru

Saat PMK atau Peraturan Rektor baru terbit:

1. Taruh PDF barunya di `sources/`.
2. Ekstrak teksnya jadi markdown, taruh di `references/` skill yang relevan, dengan nama yang memakai **tahun anggaran**, bukan tahun regulasi.
3. Bangun ulang indeksnya dengan `tools/build_index.py`.
4. Perbarui tabel tahun di SKILL.md dan di README ini.

## Lisensi

Teks PMK dan Peraturan Rektor adalah dokumen resmi lembaga negara dan perguruan tinggi negeri, disertakan di sini apa adanya untuk keperluan rujukan.

Kerangka skill, indeks, dan perkakas di repo ini dilisensikan MIT. Lihat `LICENSE`.
