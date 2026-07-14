# Skill SBM: Standar Biaya Masukan (Kemenkeu RI dan Universitas Indonesia)

Tiga skill untuk Claude Code yang menjawab pertanyaan tarif **Standar Biaya Masukan**, langsung dari teks regulasinya, bukan dari ingatan model.

| Skill | Cakupan | Sumber |
|---|---|---|
| `/sbm` | Kemenkeu **dan** UI, berdampingan | Keduanya |
| `/sbm-kemenkeu` | Kemenkeu RI saja | PMK 32/2025 |
| `/sbm-ui` | Universitas Indonesia saja | PR UI 16/2024 |

## Kenapa ini ada

Tanyakan tarif SBM ke model bahasa mana pun, dan ia akan menjawab dengan percaya diri memakai angka yang diingatnya dari entah tahun berapa. Angka itu sering salah. Di dokumen anggaran, angka salah berbiaya nyata: revisi RAB, temuan auditor, dana ditolak.

Skill ini menutup celah itu dengan cara yang membosankan tapi benar. Ia membawa teks regulasinya sendiri, mencari angkanya di sana, mengutip nomor barisnya, lalu menyuruh Anda memverifikasi ke PDF asli.

## Yang paling sering disalahpahami: tahun regulasi bukan tahun anggaran

| Regulasi | Terbit | **Mengatur Tahun Anggaran** |
|---|---|---|
| PMK Nomor 32 Tahun 2025 | 2025 | **2026** |
| Peraturan Rektor UI Nomor 16 Tahun 2024 | 2024 | **2024** |

PMK terbit 2025, tapi isinya SBM untuk TA 2026. Jadi kalau Anda mencari "SBM 2026", dokumennya adalah PMK 32/2025 ini. Ketiga skill selalu menyebut kedua tahun itu supaya Anda tidak tertukar.

## Mana yang berlaku untuk saya

**Ikuti sumber dananya, bukan lembaganya.**

- Dana APBN (hibah kementerian, BRIN, DIKTI) → **SBM Kemenkeu**
- Dana internal UI → **SB UI**

Peneliti UI yang memakai hibah APBN tunduk pada SBM Kemenkeu, bukan SB UI. Angkanya bisa berbeda jauh. Kalau ragu, pakai `/sbm` dan ia akan menyajikan keduanya.

## Pasang

Salin folder skill ke direktori skill Claude Code Anda.

**Untuk semua project (global):**

```bash
git clone https://github.com/<user>/sbm.git
cd sbm
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
```

## Isi repo

```
skills/
  sbm/           SKILL.md + references/ (teks Kemenkeu + UI, plus indeksnya)
  sbm-kemenkeu/  SKILL.md + references/ (teks Kemenkeu)
  sbm-ui/        SKILL.md + references/ (teks UI)
sources/
  pmk-32-2025-sbm-ta2026.pdf         PDF asli, ground truth
  pr-ui-16-2024-sb-ui-ta2024.pdf     PDF asli, ground truth
```

## Keterbatasan, baca ini sebelum memakai

**Teks regulasinya hasil OCR, dan tabelnya rusak sebagian.** Contoh nyata dari berkas UI:

```
| 7 | | Honor | Narasumber | | Pembekalan | | O/Pertemuan | | 400.000 |
```

Angkanya terbaca, kolomnya berantakan. Karena itu skill ini jujurnya adalah **pencari lokasi**, bukan kalkulator. Ia menemukan pos biayanya dan membaca angkanya, lalu menyuruh Anda mengecek ke PDF. Skill ini dirancang untuk mengaku tidak tahu, bukan menebak.

**PDF asli disertakan justru untuk itu.** Verifikasi bukan formalitas. Untuk dokumen resmi, angkanya harus Anda konfirmasi sendiri ke PDF.

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
