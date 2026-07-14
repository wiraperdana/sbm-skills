#!/usr/bin/env python3
"""Render TSV indeks jadi markdown yang enak dibaca agent."""
import sys
from collections import OrderedDict

JUDUL = {
    "kemenkeu": (
        "Indeks Pos Biaya: SBM Kemenkeu TA 2026",
        "PMK Nomor 32 Tahun 2025 tentang Standar Biaya Masukan Tahun Anggaran 2026",
        "sbm-kemenkeu-ta2026.md",
    ),
    "ui": (
        "Indeks Pos Biaya: Standar Biaya UI TA 2024",
        "Peraturan Rektor UI Nomor 16 Tahun 2024 tentang Standar Biaya "
        "Universitas Indonesia Tahun 2024",
        "sb-ui-ta2024.md",
    ),
}

KETERANGAN_BAGIAN = {
    "L1-TARIF": "Lampiran I, tabel tarif. Sifat: **batas tertinggi**, tidak boleh dilampaui.",
    "L1-PENJELASAN": "Lampiran I, penjelasan tiap pos. Baca ini untuk syarat dan definisi.",
    "L2-TARIF": "Lampiran II, tabel tarif. Sifat: **dapat dilampaui** sepanjang dapat dipertanggungjawabkan.",
    "L2-PENJELASAN": "Lampiran II, penjelasan tiap pos.",
}


def main(tsv: str, kunci: str) -> None:
    judul, regulasi, sumber = JUDUL[kunci]
    rows = OrderedDict()
    with open(tsv, encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            bag, ln, no, teks = line.rstrip("\n").split("\t", 3)
            rows.setdefault(bag, []).append((int(ln), no, teks))

    out = [f"# {judul}", ""]
    out.append(f"**Regulasi:** {regulasi}")
    out.append("")
    out.append(f"**Berkas teks:** `{sumber}` (rujukan baris di bawah menunjuk ke berkas itu)")
    out.append("")
    out.append(
        "Indeks ini alat navigasi, bukan sumber angka. Ia dibangun otomatis dari "
        "teks hasil OCR, jadi sebagian judul bisa terpotong dan sebagian pos bisa "
        "terlewat. **Jangan pernah menjawab dari indeks saja.** Pakai nomor baris "
        "untuk melompat ke berkas teks, baca tarif di sana, lalu verifikasi ke PDF asli."
    )
    out.append("")

    for bag, items in rows.items():
        out.append(f"## {bag}")
        ket = KETERANGAN_BAGIAN.get(bag)
        if ket:
            out.append("")
            out.append(ket)
        out.append("")
        out.append("| Baris | No. | Pos biaya |")
        out.append("|---|---|---|")
        for ln, no, teks in items:
            out.append(f"| {ln} | {no} | {teks} |")
        out.append("")

    print("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
