#!/usr/bin/env python3
"""Ubah PDF regulasi yang punya lapisan teks asli jadi berkas teks referensi.

Pakai ini hanya untuk PDF yang teksnya bisa diseleksi, misalnya dokumen yang
diekspor dari Word. PDF hasil pindaian tidak punya lapisan teks, dan untuk itu
tetap perlu OCR plus verifikasi visual.

Pemakaian:
    python3 tools/pdf_ke_teks.py sources/x.pdf skills/<skill>/references/x.md

Yang dilakukannya:
1. Menjalankan `pdftotext -layout`, supaya kolom tabel tetap sejajar.
2. Menyisipkan penanda `[PDF hal. N]` di awal tiap halaman. Nomor ini adalah
   halaman berkas PDF, bukan nomor yang tercetak di dokumen, jadi pengguna
   bisa langsung melompat ke halaman itu di penampil PDF mana pun.
3. Membuang catatan kaki tanda tangan elektronik BSrE yang berulang di tiap
   halaman, karena ia hanya menambah derau pencarian.
4. Meringkas baris kosong beruntun jadi satu.

Nomor baris berkas keluaran menjadi rujukan indeks. Karena itu, bangun ulang
indeks setiap kali berkas ini dibuat ulang.
"""
import re
import subprocess
import sys

BSRE = re.compile(
    r"^\s*(Dokumen ini telah ditandatangani secara elektronik"
    r"|Balai Besar Sertifikasi Elektronik)"
)


def main(pdf: str, keluaran: str) -> None:
    teks = subprocess.run(
        ["pdftotext", "-layout", pdf, "-"],
        check=True, capture_output=True, text=True,
    ).stdout
    out = []
    for nomor, isi in enumerate(teks.split("\f"), 1):
        baris = [b.rstrip() for b in isi.split("\n") if not BSRE.match(b)]
        if not any(b.strip() for b in baris):
            continue
        out.append(f"[PDF hal. {nomor}]")
        kosong = 0
        for b in baris:
            if b.strip():
                kosong = 0
                out.append(b)
            else:
                kosong += 1
                if kosong == 1:
                    out.append("")
    with open(keluaran, "w", encoding="utf-8") as f:
        f.write("\n".join(out).rstrip() + "\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
