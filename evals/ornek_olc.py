#!/usr/bin/env python3
"""examples/once-sonra.md içindeki önce/sonra çiftlerini ölçer.

Bu ölçüm, örnek metinlerin kendisini ölçer. Bir model karşılaştırması değildir.
Model karşılaştırması için senaryolar.json dosyasını kullan ve README'yi oku.

Çalıştır:  python3 evals/ornek_olc.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sade_lint import denetle  # noqa: E402

TURLER = {
    "1": "aciklayici", "2": "prosedurel", "3": "prosedurel",
    "4": "aciklayici", "5": "prosedurel", "6": "aciklayici",
}
KOK = pathlib.Path(__file__).resolve().parent.parent


def alintiyi_ayikla(blok):
    satirlar = [s.strip()[1:].strip() for s in blok.splitlines()
                if s.strip().startswith(">")]
    while satirlar and not satirlar[0]:
        satirlar.pop(0)
    while satirlar and not satirlar[-1]:
        satirlar.pop()
    return "\n".join(satirlar)  # aradaki boş satır paragraf sınırıdır


def cozumle(metin):
    for bolum in re.split(r"^## ", metin, flags=re.M)[1:]:
        baslik = bolum.splitlines()[0].strip()
        no = baslik.split(".")[0].strip()
        if no not in TURLER:
            continue
        once = re.search(r"\*\*Önce\*\*(.*?)\*\*Sonra\*\*", bolum, re.S)
        sonra = re.search(r"\*\*Sonra\*\*(.*?)(?:\nKurallar:|\n---|\Z)", bolum, re.S)
        if not (once and sonra):
            continue
        yield baslik, TURLER[no], alintiyi_ayikla(once.group(1)), alintiyi_ayikla(sonra.group(1))


def main():
    kaynak = (KOK / "examples" / "once-sonra.md").read_text(encoding="utf-8")
    satirlar = []
    o_ihlal = o_kelime = s_ihlal = s_kelime = 0
    for baslik, tur, once, sonra in cozumle(kaynak):
        a = denetle(once, tur)
        b = denetle(sonra, tur)
        o_ihlal += a["ihlal_toplam"]; o_kelime += a["kelime"]
        s_ihlal += b["ihlal_toplam"]; s_kelime += b["kelime"]
        satirlar.append((baslik, tur, a, b))

    print(f"| Örnek | Tür | Önce (ihlal/100 kelime) | Sonra | En uzun cümle: önce → sonra |")
    print(f"|---|---|---|---|---|")
    for baslik, tur, a, b in satirlar:
        print(f"| {baslik} | {tur} | {a['ihlal_100_kelime']} | {b['ihlal_100_kelime']} | "
              f"{a['en_uzun_cumle']} → {b['en_uzun_cumle']} |")
    o = round(100.0 * o_ihlal / max(1, o_kelime), 2)
    s = round(100.0 * s_ihlal / max(1, s_kelime), 2)
    dusus = round(100.0 * (o - s) / o, 1) if o else 0.0
    print(f"| **Toplam** | | **{o}** | **{s}** | **%{dusus} düşüş** |")
    print(f"\nÖnce: {o_ihlal} ihlal / {o_kelime} kelime. "
          f"Sonra: {s_ihlal} ihlal / {s_kelime} kelime.")


if __name__ == "__main__":
    main()
