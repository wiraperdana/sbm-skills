#!/usr/bin/env python3
"""Bangun indeks pos biaya SB UI dari Daftar Lampiran dokumen itu sendiri.

Berbeda dari build_index.py, yang menebak judul pos dari teks OCR, alat ini
memakai Daftar Lampiran sebagai daftar induk. Setiap entri daftar lalu dicari
baris judulnya di badan lampiran. Hasilnya bisa diperiksa kelengkapannya:
entri yang tidak ketemu dilaporkan, bukan dilewati diam-diam.

Syaratnya, berkas teks dibuat dengan tools/pdf_ke_teks.py dari PDF yang punya
lapisan teks asli.

Pemakaian:
    python3 tools/indeks_dari_daftar_lampiran.py \\
        skills/sbm-ui/references/sb-ui-ta2026.md > skills/sbm-ui/references/indeks-ui-ta2026.md
"""
import os
import re
import sys

ROMAWI = ["I", "II", "III", "IV", "V", "VI", "VII"]
KETERANGAN = {
    "I": "Kegiatan Pendidikan",
    "II": "Kegiatan Kemahasiswaan",
    "III": "Penelitian, Inovasi, Pengabdian Masyarakat, Inkubasi Bisnis, Kekayaan Intelektual",
    "IV": "Penyelenggaraan Operasional Manajemen",
    "V": "Honorarium Kegiatan",
    "VI": "Perjalanan Dinas",
    "VII": "Penyelenggaraan Penerimaan Mahasiswa Baru",
}


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def main(berkas: str) -> None:
    teks = open(berkas, encoding="utf-8").read().split("\n")
    lamp = {r: next(i for i, b in enumerate(teks) if norm(b) == f"LAMPIRAN {r}") for r in ROMAWI}
    akhir = {r: lamp[ROMAWI[k + 1]] if k + 1 < len(ROMAWI) else len(teks) for k, r in enumerate(ROMAWI)}

    # Halaman PDF untuk tiap baris, dari penanda [PDF hal. N]
    hal_pdf, kini = [], 0
    for b in teks:
        m = re.match(r"^\[PDF hal\. (\d+)\]$", b)
        if m:
            kini = int(m.group(1))
        hal_pdf.append(kini)

    awal_daftar = next(
        i for i, b in enumerate(teks) if norm(b).startswith("Daftar") and norm(b).endswith("Lampiran")
    )
    entri, buf = [], ""
    for b in teks[awal_daftar + 1 : lamp["I"]]:
        t = norm(b)
        if not t or t.startswith("[PDF hal"):
            continue
        buf = f"{buf} {t}".strip()
        if re.search(r"\.{2,}\s*\d+$", buf):
            entri.append(buf)
            buf = ""

    bagian, pos = -1, []
    for e in entri:
        judul = re.sub(r"\s*\.{2,}\s*\d+$", "", e)
        m = re.match(r"^(\d{1,2})\.\s+(.*)$", judul)
        if not m:
            bagian += 1
            continue
        pos.append((ROMAWI[bagian], int(m.group(1)), norm(m.group(2))))

    hilang = []
    per_lampiran = {r: [] for r in ROMAWI}
    for r, no, judul in pos:
        kunci = judul.upper()[:18]
        baris = None
        for i in range(lamp[r], akhir[r]):
            m = re.match(rf"^{no}\.\s+(.*)$", norm(teks[i]))
            if m and norm(m.group(1)).upper()[:18] == kunci:
                baris = i + 1
                break
        if baris is None:
            hilang.append(f"Lampiran {r} pos {no}: {judul}")
            continue
        per_lampiran[r].append((baris, hal_pdf[baris - 1], no, judul))

    nama = os.path.basename(berkas)
    out = [
        "# Indeks Pos Biaya: Standar Biaya UI, berlaku sejak 1 September 2026",
        "",
        "**Regulasi:** Peraturan Rektor Universitas Indonesia Nomor 24 Tahun 2026 tentang Standar Biaya Universitas Indonesia",
        "",
        f"**Berkas teks:** `{nama}` (kolom Baris menunjuk ke berkas itu)",
        "",
        "**Sumber PDF:** `sources/pr-ui-24-2026-sb-ui-ta2026.pdf` (kolom Hal. PDF menunjuk ke halaman berkas PDF itu)",
        "",
        "Indeks ini alat navigasi, bukan sumber angka. Ia dibangun dari Daftar Lampiran dokumen, "
        f"lalu tiap entri dicocokkan ke baris judulnya. Hasil pencocokan: {len(pos) - len(hilang)} dari {len(pos)} pos ketemu. "
        "**Jangan pernah menjawab dari indeks saja.** Lompat ke baris yang ditunjuk, baca tabel dan penjelasannya, "
        "lalu minta pengguna memverifikasi ke halaman PDF yang ditunjuk.",
        "",
    ]
    for r in ROMAWI:
        out += [
            f"## Lampiran {r}: {KETERANGAN[r]}",
            "",
            f"Mulai baris {lamp[r] + 1}.",
            "",
            "| Baris | Hal. PDF | No. | Pos biaya |",
            "|---|---|---|---|",
        ]
        out += [f"| {b} | {h} | {n} | {j} |" for b, h, n, j in per_lampiran[r]]
        out.append("")
    if hilang:
        out += ["## Entri Daftar Lampiran yang tidak ketemu judulnya", ""]
        out += [f"- {h}" for h in hilang]
        out.append("")
    print("\n".join(out))
    print(f"pos={len(pos)} tidak_ketemu={len(hilang)}", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1])
