#!/usr/bin/env python3
"""Bangun indeks pos biaya SBM dari teks OCR. Keluaran TSV.

Penyaring bertingkat:
1. Baris kandidat diawali nomor urut, dan TIDAK memuat token tarif
   (Rp, OH/OB, Per hari, dst). Baris provinsi dan baris tarif tersaring.
2. Hanya diambil yang nomornya MELANJUTKAN urutan (1, 2, 3, ...).
   Sub-daftar di dalam penjelasan mengulang dari 1, jadi tertolak.
3. Judul harus lolos uji bentuk: untuk Kemenkeu, diawali kata benda pos
   biaya; untuk UI, mayoritas huruf kapital (gaya judul dokumen UI).
"""
import re
import sys

TARIF = re.compile(
    r"(Rp[\d.]|\b\d[\d.,]{2,}\b|\bO[HBJKPT]\b|Orang/Kali|Per hari|Per bulan|"
    r"Pegawai/Tahun|Unit/Tahun|O/[HBJ]|\.{4,})"
)
JUDUL = re.compile(r"^\s*(\d{1,3})\.\s+(\S.*?)\s*$")

HEAD_KEMENKEU = re.compile(
    r"^(Honorarium|Honorararium|Satuan Biaya|Uang)\b", re.IGNORECASE
)


def bersih(teks: str) -> str:
    teks = teks.replace("|", " ")
    return re.sub(r"\s{2,}", " ", teks).strip()


def bentuk_ui(teks: str) -> bool:
    """Judul pos di dokumen UI ditulis kapital seluruhnya."""
    huruf = [c for c in teks if c.isalpha()]
    if len(huruf) < 10:
        return False
    return sum(c.isupper() for c in huruf) / len(huruf) >= 0.85


def bagian(baris, nama, awal, akhir, uji, monoton):
    """monoton=True menuntut nomor berurutan rapat. Dipakai untuk Kemenkeu,
    yang OCR-nya bersih. Untuk UI, OCR merusak sebagian judul, dan aturan
    monoton akan memutus seluruh urutan sesudah judul yang rusak. Di sana
    kita utamakan cakupan: terima setiap judul yang lolos uji bentuk.
    """
    keluar = []
    harap = 1
    for i in range(awal - 1, min(akhir, len(baris))):
        m = JUDUL.match(bersih(baris[i].rstrip("\n")))
        if not m:
            continue
        no, teks = int(m.group(1)), m.group(2)
        if TARIF.search(teks) or len(teks) < 12 or not uji(teks):
            continue
        if monoton:
            if no != harap:
                continue
            harap += 1
        keluar.append((nama, i + 1, no, teks))
    return keluar


BATAS = {
    "kemenkeu": (
        lambda t: bool(HEAD_KEMENKEU.match(t)),
        [
            ("L1-TARIF", 109, 2774),
            ("L1-PENJELASAN", 2775, 4090),
            ("L2-TARIF", 4091, 5900),
            ("L2-PENJELASAN", 5901, 7640),
        ],
    ),
    "ui": (
        bentuk_ui,
        [
            ("L1 KEGIATAN PENDIDIKAN", 428, 1140),
            ("L2 KEGIATAN KEMAHASISWAAN", 1141, 2234),
            ("L3 PENELITIAN/PENGABDIAN/INOVASI/KI", 2235, 2881),
            ("L4 OPERASIONAL MANAJEMEN", 2882, 4270),
            ("L5 HONORARIUM KEGIATAN", 4271, 5037),
            ("L6 PERJALANAN DINAS", 5038, 5988),
            ("L7 PENERIMAAN MAHASISWA BARU", 5989, 6287),
        ],
    ),
}

if __name__ == "__main__":
    berkas = sys.argv[1]
    kunci = "kemenkeu" if "kemenkeu" in berkas else "ui"
    uji, batas = BATAS[kunci]
    with open(berkas, encoding="utf-8") as f:
        baris = f.readlines()
    for b in batas:
        for row in bagian(baris, *b, uji):
            print("\t".join(str(x) for x in row))
