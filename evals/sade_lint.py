#!/usr/bin/env python3
"""Sade Türkçe kurallarını sayan belirlenimci denetleyici.

Düzenli ifadeyle yakalanabilen ihlalleri sayar: cümle uzunluğu, bürokratik kip,
yasak kip, adlaştırma, yardımcı fiil yığını, ulaç zinciri, dolgu kelimeleri,
noktalı virgül, uzun çizgi, ağır koşul kalıbı, eş anlamlı dönüşümü, hitap kipi
dönüşümü ve kesme işareti hataları.

Bilinen tavan: bu bir düzenli ifade taramasıdır, dil bilgisi çözümleyicisi
değildir. Eksik sayar (biçim bilgisi çözümlemesi yok) ve bazı örtüşen kalıpları
iki kez sayar. Sayılar, aynı sürümden geçen iki metin arasında karşılaştırılır.
Tek başına bir uygunluk kararı değildir.

Kullanım:
  python3 sade_lint.py --tur prosedurel dosya.md
  cat metin.md | python3 sade_lint.py --tur aciklayici -
  python3 sade_lint.py --oz-test
"""
import json
import re
import sys

SINIRLAR = {"prosedurel": 12, "aciklayici": 16}

# --- Türkçe küçük harfe çevirme -------------------------------------------
# Python'un varsayılan lower() işlevi "İ" harfini birleşik noktalı "i" yapar.
# Türkçe metinde bu, kalıp eşleşmesini bozar.
_BUYUK = str.maketrans({"İ": "i", "I": "ı"})


def tr_kucult(metin):
    return metin.translate(_BUYUK).lower()


# --- Ek yardımcıları ------------------------------------------------------
_FIIL_EKLERI = (
    r"(?:ın|in|un|ün|ınız|iniz|unuz|ünüz|ır|ir|ur|ür|dı|di|du|dü|"
    r"ecek|acak|me|ma|mek|mak|en|an|arak|erek|mış|miş|ılır|ilir|"
    r"ulur|ülür|ılmış|ilmiş|dığı|diği|er|ar|yın|yin)?"
)
# Uzun ek önce gelir: düzenli ifade alternatifleri sırayla denenir.
_ISIM_EKLERI = (
    r"(?:ları|leri|larını|lerini|sının|sinin|nın|nin|nun|nün|"
    r"ndan|nden|nda|nde|dan|den|tan|ten|lar|ler|sı|si|su|sü|"
    r"ın|in|un|ün|yı|yi|yu|yü|nı|ni|nu|nü|na|ne|ya|ye|"
    r"da|de|ta|te|lı|li|lu|lü|ı|i|u|ü|a|e)*"
)


def _fiil(*kokler):
    return re.compile(r"\b(?:" + "|".join(kokler) + r")" + _FIIL_EKLERI + r"\b")


def _isim(*kokler):
    return re.compile(r"\b(?:" + "|".join(kokler) + r")" + _ISIM_EKLERI + r"\b")


# --- Kalıplar (küçük harfe çevrilmiş metin üzerinde) ----------------------
BUROKRATIK_KIP = re.compile(r"\w{2,}(?:mekte|makta)(?:dir|dır)?\b")
YASAK_KIP = re.compile(
    r"\b\w{2,}(?:meli|malı)(?:dir|dır|sınız|siniz|yım|yim|sın|sin|yız|yiz)?\b")
YASAK_KIP_ISTISNA = {"temeli", "emeli", "kremalı", "yamalı", "kamalı",
                     "damalı", "hamalı", "amalı"}
MISTIR = re.compile(r"\w{2,}(?:mış|miş|muş|müş)(?:tır|tir|tur|tür)\b")
EDILGEN_OZNE = re.compile(r"\btarafından\b")
YARDIMCI_FIIL = re.compile(
    r"\bgerçekleştir\w*\b|\bsağlan\w*\b|\bsağlama\w*\b|\bsağlar\b|"
    r"\bsağlayan\b|\bsağlayarak\b|\bbulunmakta\w*\b")
ADLASTIRMA = re.compile(
    r"\w{2,}(?:mesi|ması|mesini|masını|mesinin|masının)\s+"
    r"(?:gerek|sağlan|yapıl|gerçekleş|zorunlu|öneril|tavsiye)\w*")
BIR_SEKILDE = re.compile(r"\bbir\s+(?:şekilde|biçimde|surette)\b")
ULAC = re.compile(r"\b\w{3,}(?:arak|erek)\b")
ULAC_ISTISNA = {"olarak"}
KISALTMA_DOLGU = re.compile(r"\b(?:vb|vs|örn)\.")
VE_VEYA = re.compile(r"\bve\s*/\s*veya\b")
DOLGU = re.compile(
    r"\b(?:oldukça|son\s+derece|bir\s+hayli|epeyce|kolayca|zahmetsizce|"
    r"sorunsuz|kusursuz|kapsamlı|güçlü|esnek|"
    r"kritik\s+önem\w*|büyük\s+önem\w*|önem\s+arz\w*|önemlidir|"
    r"dikkat\s+çekici\w*|unutulmamalı\w*|belirtmek\s+gerekir|"
    r"bu\s+bağlamda|bu\s+doğrultuda|bu\s+noktada|bu\s+kapsamda|"
    r"söz\s+konusu|herhangi\s+bir|başarıyla|başarılı\s+bir|"
    r"hayata\s+geçir\w*|ele\s+alın\w*|göz\s+at\w*)\b")
OLANAK_KALIBI = re.compile(
    r"\b(?:olanak|olanağ|imkân|imkan|fırsat)\w*\s+(?:tanı|sağla|ver|sun)\w*")
AGIR_KOSUL = re.compile(r"\b(?:durumunda|hâlinde|halinde|takdirde)\b")
INGILIZCE_FIIL = re.compile(
    r"\b(?:implemente|handle|check|deploy|optimize|refactor|debug|trigger|"
    r"fetch|render|validate|update)\s+(?:et|ed)\w*")
UZUN_CIZGI = re.compile(r"[—–]")  # Kural 8.7
SONDAKI_KOSUL = re.compile(
    r",\s*(?:eğer\s+)?[^,]*?\w(?:ursa|ürse|ırsa|irse|arsa|erse)\b[^.!?]*[.!?]?$")

ROTASYON = [
    ("ayar", _isim("ayar", "yapılandırma", "konfigürasyon", "konfigurasyon")),
    ("dogrulama", _fiil("doğrula", "kontrol\\s+et", "denetle", "teyit\\s+et")),
    ("silme", _fiil("sil", "kaldır", "temizle")),
    ("calistirma", _fiil("çalıştır", "yürüt", "koştur")),
    ("hata", _isim("hata", "sorun", "problem", "arıza")),
]

HITAP = [
    ("kisa-emir", re.compile(r"\w{2,}(?:yın|yin|yun|yün|ın|in|un|ün)\s*[.!?]")),
    # "-sınız/-siniz" kişi ekidir ("yapabilirsiniz"), nazik emir değildir.
    ("nazik-emir", re.compile(r"\w{2,}(?<!s)(?:ınız|iniz|unuz|ünüz)\s*[.!?]")),
    ("gereklilik", re.compile(r"\w{2,}(?:malısınız|melisiniz)\s*[.!?]")),
    ("edilgen", re.compile(r"\w{2,}(?:ılır|ilir|ulur|ülür)\s*[.!?]")),
    ("birinci-cogul", re.compile(r"\w{2,}(?:alım|elim)\s*[.!?]")),
]

# --- Kalıplar (özgün büyük/küçük harf üzerinde) ---------------------------
KESMESIZ_EK = re.compile(r"\b[A-ZÇĞİÖŞÜ]{2,}[a-zçğıöşü]{1,4}\b")
YANLIS_KESME = re.compile(
    r"\b(?:API'ı|API'ın|API'a|API'da|SQL'yi|SQL'ya|JSON'ı|JSON'i|URL'yi|"
    r"URL'ı|ID'ı|XML'yi|HTTP'nın|HTTP'ya|SDK'yi|SDK'nin|UI'yi|CPU'yi|"
    r"GitHub'da|Docker'ta)\b")


def kodu_ayikla(metin):
    metin = re.sub(r"```.*?```", " ", metin, flags=re.S)
    metin = re.sub(r"`[^`\n]+`", " KOD ", metin)      # Kural 8.2: tek kelime
    metin = re.sub(r"^#+\s.*$", " ", metin, flags=re.M)  # başlıklar muaf
    metin = re.sub(r"https?://\S+", " ADRES ", metin)
    return metin


def cumleler(metin):
    metin = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", metin, flags=re.M)
    parcalar = []
    for paragraf in re.split(r"\n\s*\n", metin):  # paragraf sonu cümleyi bitirir
        parcalar += re.split(r"(?<=[.!?:])\s+", paragraf)
    return [p.strip() for p in parcalar if len(p.strip().split()) >= 2]


def _say(kalip, metin, istisna=None):
    if istisna is None:
        return len(kalip.findall(metin))
    return sum(1 for m in kalip.finditer(metin) if m.group(0) not in istisna)


def denetle(metin, tur):
    ozgun = kodu_ayikla(metin)
    govde = tr_kucult(ozgun)
    sinir = SINIRLAR[tur]
    cumle_listesi = cumleler(govde)
    uzunluklar = [len(c.split()) for c in cumle_listesi]

    s = {}
    s["cumle_uzun"] = sum(1 for n in uzunluklar if n > sinir)
    s["burokratik_kip"] = _say(BUROKRATIK_KIP, govde)
    s["yasak_kip"] = _say(YASAK_KIP, govde, YASAK_KIP_ISTISNA)
    s["mistir_kalibi"] = _say(MISTIR, govde)
    s["edilgen_ozne"] = _say(EDILGEN_OZNE, govde)
    s["yardimci_fiil"] = _say(YARDIMCI_FIIL, govde)
    s["adlastirma"] = _say(ADLASTIRMA, govde)
    s["bir_sekilde"] = _say(BIR_SEKILDE, govde)
    s["noktali_virgul"] = govde.count(";")
    s["uzun_cizgi"] = _say(UZUN_CIZGI, govde)
    s["kisaltma_dolgu"] = _say(KISALTMA_DOLGU, govde)
    s["ve_veya"] = _say(VE_VEYA, govde)
    s["dolgu"] = _say(DOLGU, govde)
    s["olanak_kalibi"] = _say(OLANAK_KALIBI, govde)
    s["agir_kosul"] = _say(AGIR_KOSUL, govde)
    s["ingilizce_fiil"] = _say(INGILIZCE_FIIL, govde)

    # Ulaç zinciri: bir cümlede birden çok "-arak/-erek" varsa fazlası ihlaldir.
    ulac = 0
    for c in cumle_listesi:
        n = sum(1 for m in ULAC.finditer(c) if m.group(0) not in ULAC_ISTISNA)
        if n > 1:
            ulac += n - 1
    s["ulac_zinciri"] = ulac

    # Koşul cümlenin başında durur (Kural 4.3).
    sondaki = 0
    for c in cumle_listesi:
        if SONDAKI_KOSUL.search(c):
            sondaki += 1
        elif "eğer" in c and not c.startswith("eğer"):
            sondaki += 1
    s["sondaki_kosul"] = sondaki

    # Eş anlamlı dönüşümü: bir kümeden birden çok kök geçerse fazlası ihlaldir.
    rotasyon = 0
    for _, kalip in ROTASYON:
        kokler = {m.group(0)[:5] for m in kalip.finditer(govde)}
        if len(kokler) > 1:
            rotasyon += len(kokler) - 1
    s["es_anlamli_rotasyon"] = rotasyon

    # Hitap kipi tektir (Kural 10.1).
    siniflar = [ad for ad, kalip in HITAP if kalip.search(govde)]
    s["hitap_rotasyon"] = max(0, len(siniflar) - 1)

    # Kesme işareti denetimleri özgün büyük/küçük harf ister (Kural 9.4).
    s["kesme_hatasi"] = _say(KESMESIZ_EK, ozgun) + _say(YANLIS_KESME, ozgun)

    kelime = max(1, len(govde.split()))
    toplam = sum(s.values())
    return {
        "tur": tur,
        "kelime": kelime,
        "cumle": len(cumle_listesi),
        "ortalama_cumle_kelime": round(sum(uzunluklar) / max(1, len(uzunluklar)), 1),
        "en_uzun_cumle": max(uzunluklar, default=0),
        "hitap_siniflari": siniflar,
        "ihlaller": s,
        "ihlal_toplam": toplam,
        "ihlal_100_kelime": round(100.0 * toplam / kelime, 2),
    }


SISKIN = """Kullanıcının iptal akışında karşılaşabileceği uyarıların gösterilmesi
işleminin, taahhüt veya gecikme durumunun kontrol edilmesi sonrasında
gerçekleştirilmesi gerekmektedir. Bu bağlamda ilgili denetimin APIdan dönen yanıt
üzerinden yapılması kritik öneme sahip olup, hata olması durumunda kullanıcıların
hatalı bir şekilde iptal işlemini tamamlayabilmesi söz konusu olabilmektedir.
Yapılandırma dosyası — ekip tarafından — kontrol edilerek doğrulanarak yüklenmiştir;
bu ayarlar zaman aşımı vb. değerleri içermektedir. Servisin deploy edilmesi ve
kayıtların silinmesi sağlanmalıdır. Sistem, kullanıcılara geniş bir esneklik
olanağı tanımaktadır ve/veya yeni seçenekler sunar."""

SADE = """Uyarı kutularını taahhüt denetiminden sonra gösterin.

Denetimi sunucunun döndüğü yanıt üzerinden yapın.

Denetim atlanırsa kullanıcı iptali yanlışlıkla tamamlar."""


def oz_test():
    siskin = denetle(SISKIN, "prosedurel")
    sade = denetle(SADE, "prosedurel")
    i = siskin["ihlaller"]
    beklenen = [
        "cumle_uzun", "burokratik_kip", "yasak_kip", "mistir_kalibi",
        "edilgen_ozne", "yardimci_fiil", "adlastirma", "bir_sekilde",
        "noktali_virgul", "uzun_cizgi", "kisaltma_dolgu", "ve_veya", "dolgu",
        "olanak_kalibi", "agir_kosul", "ingilizce_fiil", "ulac_zinciri",
        "es_anlamli_rotasyon", "kesme_hatasi",
    ]
    eksik = [ad for ad in beklenen if i[ad] < 1]
    assert not eksik, f"şişkin metinde yakalanmayan kural: {eksik}\n{json.dumps(i, ensure_ascii=False, indent=2)}"
    assert sade["ihlal_toplam"] == 0, json.dumps(sade, ensure_ascii=False, indent=2)
    print(f"öz test tamam: şişkin metinde {siskin['ihlal_toplam']} ihlal, "
          f"sade metinde 0 ihlal, {len(beklenen)} kural doğrulandı")


def main():
    arg = sys.argv[1:]
    if "--oz-test" in arg:
        oz_test()
        return
    tur = "aciklayici"
    if "--tur" in arg:
        tur = arg[arg.index("--tur") + 1]
    if tur not in SINIRLAR:
        sys.exit(f"bilinmeyen tür: {tur}. Seçenekler: {', '.join(SINIRLAR)}")
    kaynak = arg[-1]
    metin = sys.stdin.read() if kaynak == "-" else open(kaynak, encoding="utf-8").read()
    print(json.dumps(denetle(metin, tur), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
