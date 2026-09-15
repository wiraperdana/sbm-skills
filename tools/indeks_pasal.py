#!/usr/bin/env python3
"""Bangun indeks per pasal untuk Peraturan Rektor UI yang tidak punya lampiran tarif.

Dokumen seperti PR UI 10/2026 tentang Standar Kelengkapan Dokumen Pembayaran
tidak berisi tabel. Isinya pasal demi pasal, dan tiap pasal kelengkapan dibuka
dengan kalimat "Kelengkapan dokumen pembayaran <jenis> ...". Karena itu indeks
dibangun dari judul BAB, judul Bagian, dan kalimat pembuka tiap pasal.

Kelengkapan indeks bisa diperiksa: nomor pasal harus bersambung dari 1 sampai
pasal terakhir. Nomor yang meloncat dilaporkan ke stderr, bukan dilewati
diam-diam.

Syaratnya, berkas teks dibuat dengan tools/pdf_ke_teks.py dari PDF yang punya
lapisan teks asli.

Pemakaian:
    python3 tools/indeks_pasal.py \\
        skills/sbm-ui/references/kelengkapan-pembayaran-ui-ta2026.md \\
        > skills/sbm-ui/references/indeks-kelengkapan-pembayaran-ui-ta2026.md
"""
import os
import re
import sys

PENGGAL = re.compile(r"\s+sebagaimana\s+dimaksud|,?\s+meliputi\b|\s+terdiri atas|[:;]")


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def penanda_halaman(t: str) -> bool:
    return t.startswith("[PDF hal") or bool(re.fullmatch(r"-\s*\d+\s*-", t))


def gabung(buf: list) -> str:
    """Gabungkan baris, dan sambung kata yang terpenggal tanda hubung di akhir baris."""
    hasil = ""
    for t in buf:
        hasil = f"{hasil}{t}" if hasil.endswith("-") else f"{hasil} {t}".strip()
    return hasil


def pokok(teks: list, mulai: int) -> str:
    """Kalimat pembuka pasal, dipotong sebelum rujukan pasal atau daftar butir.

    Baris kosong menandai akhir pasal, kecuali baris kosong di depan pergantian
    halaman, karena kalimat boleh menyeberang halaman.
    """
    buf = []
    for i in range(mulai, min(mulai + 12, len(teks))):
        t = norm(teks[i])
        if penanda_halaman(t):
            continue
        if not t:
            lanjut = next((norm(b) for b in teks[i + 1:] if norm(b)), "")
            if buf and not penanda_halaman(lanjut):
                break
            continue
        if buf and re.match(r"^(\(\d+\)|[a-z]\.)\s", t):
            break
        buf.append(t)
        if len(buf) == 6:
            break
    kalimat = re.sub(r"^\(\d+\)\s*", "", gabung(buf))
    kalimat = PENGGAL.split(kalimat, maxsplit=1)[0].rstrip(" ,.")
    return kalimat if len(kalimat) <= 130 else kalimat[:127].rstrip() + "..."


def main(berkas: str) -> None:
    teks = open(berkas, encoding="utf-8").read().split("\n")

    hal_pdf, kini = [], 0
    for b in teks:
        m = re.match(r"^\[PDF hal\. (\d+)\]$", b)
        if m:
            kini = int(m.group(1))
        hal_pdf.append(kini)

    def judul_setelah(i: int) -> str:
        """Judul BAB atau Bagian, termasuk judul yang terbelah dua baris."""
        buf = []
        for b in teks[i + 1:]:
            t = norm(b)
            if t:
                buf.append(t)
            elif buf:
                break
        return gabung(buf)

    bab, bagian = [], ""
    for i, b in enumerate(teks):
        t = norm(b)
        m = re.fullmatch(r"BAB ([IVXL]+)", t)
        if m:
            bab.append({"romawi": m.group(1), "judul": judul_setelah(i), "pasal": []})
            bagian = ""
            continue
        if re.fullmatch(r"Bagian [A-Z][a-z]+", t):
            bagian = judul_setelah(i)
            continue
        m = re.fullmatch(r"Pasal (\d+)", t)
        if m and bab:
            bab[-1]["pasal"].append((i + 1, hal_pdf[i], int(m.group(1)), bagian, pokok(teks, i + 1)))

    nomor = [p[2] for x in bab for p in x["pasal"]]
    loncat = [f"setelah Pasal {a}, ketemu Pasal {b}" for a, b in zip(nomor, nomor[1:]) if b != a + 1]

    nama = os.path.basename(berkas)
    out = [
        "# Indeks Pasal: Standar Kelengkapan Dokumen Pembayaran UI, berlaku sejak 1 April 2026",
        "",
        "**Regulasi:** Peraturan Rektor Universitas Indonesia Nomor 10 Tahun 2026 tentang Standar Kelengkapan Dokumen Pembayaran",
        "",
        f"**Berkas teks:** `{nama}` (kolom Baris menunjuk ke berkas itu)",
        "",
        "**Sumber PDF:** `sources/pr-ui-10-2026-standar-kelengkapan-pembayaran.pdf` (kolom Hal. PDF menunjuk ke halaman berkas PDF itu)",
        "",
        f"Indeks ini alat navigasi. Ia dibangun dari judul BAB, judul Bagian, dan kalimat pembuka tiap pasal. "
        f"Hasilnya: {len(bab)} BAB, {len(nomor)} pasal, nomor pasal {'bersambung tanpa loncatan' if not loncat else 'MELONCAT, lihat bagian akhir'}. "
        "Kolom Pokok hanya potongan kalimat pembuka. **Jangan pernah menyusun daftar dokumen dari indeks saja.** "
        "Lompat ke baris yang ditunjuk, baca seluruh butir pasalnya, lalu minta pengguna memverifikasi ke halaman PDF yang ditunjuk.",
        "",
    ]
    for x in bab:
        out += [
            f"## BAB {x['romawi']}: {x['judul'].title()}",
            "",
            "| Baris | Hal. PDF | Pasal | Bagian | Pokok |",
            "|---|---|---|---|---|",
        ]
        out += [f"| {b} | {h} | {n} | {g or '-'} | {k} |" for b, h, n, g, k in x["pasal"]]
        out.append("")
    if loncat:
        out += ["## Nomor pasal yang meloncat", ""] + [f"- {l}" for l in loncat] + [""]
    print("\n".join(out).rstrip())
    print(f"bab={len(bab)} pasal={len(nomor)} loncat={len(loncat)}", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1])
