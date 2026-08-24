#!/usr/bin/env python3
"""sade_lint için kural bazlı testler. Ek bağımlılık istemez.

Çalıştır:  python3 evals/test_sade_lint.py
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sade_lint import denetle, tr_kucult  # noqa: E402

BASARISIZ = []


def esittir(ad, gercek, beklenen):
    if gercek != beklenen:
        BASARISIZ.append(f"{ad}: beklenen {beklenen!r}, gelen {gercek!r}")


def en_az(ad, metin, kural, sayi=1, tur="prosedurel"):
    g = denetle(metin, tur)["ihlaller"][kural]
    if g < sayi:
        BASARISIZ.append(f"{ad}: {kural} en az {sayi} olmalıydı, {g} geldi — {metin!r}")


def temiz(ad, metin, kural, tur="prosedurel"):
    g = denetle(metin, tur)["ihlaller"][kural]
    if g != 0:
        BASARISIZ.append(f"{ad}: {kural} 0 olmalıydı, {g} geldi — {metin!r}")


# Türkçe küçük harf: Python'un lower() işlevi "İ" harfini bozar.
esittir("tr_kucult büyük İ", tr_kucult("İSTANBUL"), "istanbul")
esittir("tr_kucult noktasız I", tr_kucult("IŞIK"), "ışık")

# Kural 3.2 — bürokratik geniş zaman
en_az("3.2 mektedir", "Sistem her istekte günlüğe yazmaktadır.", "burokratik_kip")
temiz("3.2 temiz", "Sistem her istekte günlüğe yazar.", "burokratik_kip")

# Kural 3.1 — yasak kip, ve isim istisnası
en_az("3.1 malıdır", "Servis yeniden başlatılmalıdır.", "yasak_kip")
temiz("3.1 isim istisnası", "Bu yapının temeli sağlamdır.", "yasak_kip")

# Kural 3.8 — rivayet birleşimi
en_az("3.8 mıştır", "Dosya sunucuya yüklenmiştir.", "mistir_kalibi")

# Kural 3.4 — edilgen özne
en_az("3.4 tarafından", "Kuyruk, işçi tarafından tüketilir.", "edilgen_ozne")

# Kural 1.4 ve 3.7 — yardımcı fiil yığını
en_az("1.4 gerçekleştir", "Kurulum işlemini gerçekleştirin.", "yardimci_fiil")
temiz("1.4 kod muaf", "`gerçekleştir` komutunu çalıştırın.", "yardimci_fiil")

# Kural 1.8 — adlaştırma
en_az("1.8 adlaştırma", "Yapılandırmanın doğrulanması gerekir.", "adlastirma")

# Kural 3.5 — ulaç zinciri
en_az("3.5 ulaç zinciri", "Dosyayı okuyarak ve ayrıştırarak yükler.", "ulac_zinciri")
temiz("3.5 tek ulaç", "Dosyayı okuyarak başlar.", "ulac_zinciri")
temiz("3.5 olarak istisnası", "Bunu yedek olarak tutar.", "ulac_zinciri")

# Kural 4.3 — koşul cümlenin başında durur
en_az("4.3 sondaki koşul", "Günlüğü okuyun, derleme başarısız olursa.", "sondaki_kosul")
temiz("4.3 baştaki koşul", "Derleme başarısız olursa, günlüğü okuyun.", "sondaki_kosul")

# Kural 9.4 — kesme işareti
en_az("9.4 kesme yok", "APIyi çağırın.", "kesme_hatasi")
en_az("9.4 yanlış ek", "API'ı çağırın.", "kesme_hatasi")
temiz("9.4 doğru", "API'yi çağırın.", "kesme_hatasi")
temiz("9.4 doğru SQL", "SQL'i çalıştırın.", "kesme_hatasi")

# Kurallar 1.1 ve 10.2 — eş anlamlı dönüşümü
en_az("1.1 rotasyon", "Ayarları açın. Yapılandırmayı düzenleyin.", "es_anlamli_rotasyon")
temiz("1.1 tek terim", "Ayarları açın. Ayarları kaydedin.", "es_anlamli_rotasyon")

# Kural 10.1 — hitap kipi tektir
en_az("10.1 hitap", "Servisi kurun. Sonra yapılandırmayı açınız.", "hitap_rotasyon")
temiz("10.1 tek kip", "Servisi kurun. Sonra ayarları açın.", "hitap_rotasyon")
temiz("10.1 kişi eki", "Bunu yapabilirsiniz.", "hitap_rotasyon")

# Kural 8.1 ve 8.2 — noktalama ve kod sayımı
en_az("8.1 noktalı virgül", "Servisi kurun; sonra başlatın.", "noktali_virgul")
esittir(
    "8.2 kod tek kelime",
    denetle("Şu komutu çalıştırın: `docker compose up --build --force-recreate -d`.",
            "prosedurel")["ihlaller"]["cumle_uzun"],
    0,
)

# Kural 4.1 — cümle uzunluğu
en_az(
    "4.1 uzun cümle",
    "Kullanıcı hesabını kapatmadan önce fatura bilgilerini indirin ve "
    "aboneliğinizi iptal edin ve verilerinizi dışa aktarın lütfen.",
    "cumle_uzun",
)

# Şişkinlik sözlüğü
en_az("dolgu", "Bu ayar kritik öneme sahiptir.", "dolgu")
en_az("bir şekilde", "Servis hızlı bir şekilde açılır.", "bir_sekilde")
en_az("ağır koşul", "Hata olması durumunda yeniden deneyin.", "agir_kosul")
en_az("olanak kalıbı", "Bu ayar size esneklik olanağı tanır.", "olanak_kalibi")
en_az("İngilizce fiil", "Servisi deploy edin.", "ingilizce_fiil")
en_az("kısaltma dolgusu", "Ayarlar zaman aşımı vb. değerleri tutar.", "kisaltma_dolgu")
en_az("ve/veya", "Tabloyu ve/veya görünümü kopyalar.", "ve_veya")

if BASARISIZ:
    print(f"{len(BASARISIZ)} test başarısız:")
    for s in BASARISIZ:
        print("  -", s)
    sys.exit(1)
print("bütün testler geçti")
