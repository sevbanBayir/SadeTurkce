---
name: sade-turkce
version: 1.0.0
description: |
  Türkçe metinleri sade, tek anlamlı ve yapay zekâ şişkinliğinden arınmış
  biçimde yaz veya yeniden yaz. Doküman, README, runbook, hata mesajı, sürüm
  notu, olay raporu, commit mesajı, PR açıklaması ve arayüz metni için kullan.
  Kullanıcı "sade Türkçe", "duru Türkçe", "Türkçeleştir", "sadeleştir",
  "bürokratik dili at", "resmî dili at", "daha anlaşılır yaz" dediğinde de
  kullan. Kuralları uygular: kısa cümle, tek kavram tek kelime, emir kipi,
  koşul önce emir sonra, adlaştırma yasağı, -mektedir yasağı, TDK yazım
  denetimi (de/da, ki, mi, kesme işareti).
license: MIT
compatibility: claude-code cursor codex gemini-cli opencode
metadata:
  kaynak: ASD-STE100 Issue 9 mantığından Türkçeye yeniden türetilmiştir
  yazim-kaynagi: TDK Yazım Kuralları
---

# Sade Türkçe: Bakım Kılavuzu Gibi Yaz

Türkçe teknik metni bu kurallarla yaz. Kurallar, ASD-STE100 Basitleştirilmiş Teknik İngilizce'nin mantığından türer. Ama çeviri değildir: Türkçe eklemeli ve sonuncul yüklemli bir dildir, bu yüzden kurallar yeniden türetilmiştir.

Hedef okur yorgundur, acelesi vardır ve metni bir kez okur. Her cümle bu tek okumada anlaşılmalıdır. Kurallar aynı zamanda yapay zekâ metinlerinin tipik izlerini siler: uzun cümle, eş anlamlı dönüşümü, dolgu, bürokratik kip ve süsleme.

## Görevin

Türkçe metin yazarken veya düzeltirken:

1. **Modu seç.** Pratik (varsayılan) veya katı.
2. **Metni sınıflandır.** Prosedürel mü, açıklayıcı mı? Diğer bütün kurallar buna bağlıdır.
3. **Terimleri önceden seç.** Ayar mı yapılandırma mı? Doğrula mı denetle mi? Birini seç, belgenin sonuna kadar koru.
4. **Kuralları uygula.** Katalog aşağıdadır.
5. **Öz denetimi yap.** Bu adım isteğe bağlı değildir.
6. **Koda dokunma.** Kod, tanımlayıcı, komut ve alıntılanan hata metni değişmez.

Metni yazmak yerine **denetlemen** istendiğinde her ihlali şu biçimde bildir: kural numarası, hatalı metin, kurala uygun karşılığı. Yalnızca bu dosyada bulunan kural numaralarını kullan. Numarayı ezberden uydurma.

## İki Mod

| Mod | Ne zaman | Ne uygularsın |
|---|---|---|
| **Pratik** (varsayılan) | Doküman, README, hata mesajı, sohbet | Bütün yapı kuralları. Alan terimleri kalır ("webhook", "idempotent", "coroutine"). |
| **Katı** | Kullanıcı "katı", "TDK'ya tam uygun" veya "kurum standardı" dediğinde | Yapı kuralları + tam kelime disiplini + Bölüm 9 yazım denetiminin tamamı. |

## Adım 1: Metni Sınıflandır

| | Prosedürel (yönerge) | Açıklayıcı (anlatım) |
|---|---|---|
| Amaç | Okura ne yapacağını söyler | Bir şeyin ne olduğunu anlatır |
| Kip | Emir: "Bağımlılıkları kurun." | Geniş zaman, görülen geçmiş, gelecek |
| Cümle sınırı | **12 kelime** (Kural 4.1) | **16 kelime** (Kural 6.2) |
| Birim | Bir cümle, bir işlem (5.1) | Bir paragraf, bir konu (6.3) |

İkisini tek bölümde karıştırma. "Kurulum" bölümü prosedüreldir. "Mimari" bölümü açıklayıcıdır. Prosedürün içindeki not açıklayıcıdır: 16 kelime sınırına girer ve emir kipi almaz.

**Kelime sınırları neden İngilizce'den düşük:** Türkçe eklemelidir. "yapılandırabilirsiniz" tek kelimedir, İngilizcesi dört kelimedir. 12 kelimelik bir Türkçe cümle, 20 kelimelik bir İngilizce cümleye denktir.

## KURAL KATALOĞU

### Bölüm 1. Kelimeler

| Kural | Yönerge |
|---|---|
| 1.1 | Tek kavram, tek kelime. Belgenin tamamında geçerlidir. |
| 1.2 | Alan terimleri serbesttir. "Webhook", "commit", "endpoint", "derleyici" teknik addır. |
| 1.3 | Teknik adı fiil yapma. "Deploy etmek", "webhook'lamak" yerine gerçek fiil kullan. |
| 1.4 | Yardımcı fiil yığını kurma. "Gerçekleştirmek", "sağlamak", "bulunmak" bir eylemi anlatmaz. |
| 1.5 | Kısa ve yaygın kelimeyi seç. "Kullanıma sunmak" yerine "yayınlamak". |
| 1.6 | Ağız, argo ve gereksiz eski kelime kullanma. Ama yerleşmiş terimi zorla Türkçeleştirme. |
| 1.7 | Gereksiz İngilizce fiil kurma. "Handle etmek" yerine "işlemek", "check etmek" yerine "denetlemek". |
| 1.8 | Fiili ada çevirme. Bu kural, Türkçe şişkinliğin bir numaralı kaynağıdır. |

**Önce:** Doğrulama işleminin gerçekleştirilmesi kullanıcı tarafından sağlanır.
**Sonra:** Kullanıcı, veriyi doğrular.

**Önce:** Servisin deploy edilmesi ve konfigürasyonun handle edilmesi gerekmektedir.
**Sonra:** Servisi yayına alın. Sonra ayarları işleyin.

### Bölüm 2. Tamlamalar

Zincirleme isim tamlaması, Türkçenin en tehlikeli yapısıdır. Her ek bir anlam katmanı ekler ve okur hangi kelimenin hangisine bağlandığını kaybeder.

| Kural | Yönerge |
|---|---|
| 2.1 | Bir tamlama en fazla üç kelimedir. |
| 2.2 | Daha uzunsa "için", "ile", "-deki", "-e ait" ile kır. |
| 2.3 | Uzun tamlamayı bir kez açık yaz, sonra kısa adını kullan. |

**Önce:** veritabanı bağlantı havuzu zaman aşımı ayarı değeri
**Sonra:** bağlantı havuzundaki zaman aşımı değeri

**Önce:** kullanıcı oturum bilgileri saklama süresi sınırı
**Sonra:** oturum bilgileri için saklama süresi

### Bölüm 3. Fiiller ve Kipler

| Kural | Yönerge |
|---|---|
| 3.1 | Prosedürde emir kipi kullan, ikinci çoğul: "Kurun." Belgenin tamamında tek kip. |
| 3.2 | "-mektedir" ve "-maktadır" kullanma. Geniş zaman yeter: "çalışmaktadır" → "çalışır". |
| 3.3 | Edilgen çatıyı yalnızca açıklayıcı metinde ve özne gerçekten bilinmiyorsa kullan. |
| 3.4 | "Tarafından" kullanma. Etken cümle kur. |
| 3.5 | Bir cümlede en fazla bir yan cümle. "-arak", "-ıp", "-ınca", "-dığında" zinciri kurma. |
| 3.6 | Sıfat-fiilleri üst üste yığma. "-an", "-dık", "-acak" bir cümlede bir kez geçer. |
| 3.7 | Eylemi fiille anlat, adla değil. "Sıkıştırma işlemi uygula" → "sıkıştır". |
| 3.8 | Rivayet kipi ("-miş") kullanma. Görülen geçmiş kullan ("-dı"). |

**Onaylı kipler: geniş zaman (-ır), görülen geçmiş (-dı), gelecek (-acak), olanak (-ebilir), emir (-ın).**
**Yasak: -mektedir, -maktadır, -meli, -malı, -miş, "-mesi gerekmektedir", "olabilmektedir".**

"-meli" özellikle tehlikelidir: okur bunu isteğe bağlı sanır. Zorunluluksa emir kipi kullan.

**Önce:** Kurulum tamamlandıktan sonra servis yeniden başlatılmalıdır.
**Sonra:** Kurulum bitince servisi yeniden başlatın.

**Önce:** Bağlantı, istemci tarafından kapatılmaktadır.
**Sonra:** İstemci, bağlantıyı kapatır.

**Önce:** Yapılandırmayı okuyarak doğrulayıp önbelleğe alarak servisi başlatır.
**Sonra:** Yapılandırmayı okur. Doğrular ve önbelleğe alır. Sonra servisi başlatır.

### Bölüm 4. Cümle

| Kural | Yönerge |
|---|---|
| 4.1 | Prosedürde en fazla 12 kelime. Uyarılar dâhildir. |
| 4.2 | Kelime yutma. Ek atma. "Dosya var mı bak" değil, "Dosyanın olduğunu doğrulayın". |
| 4.3 | Koşul başta durur, virgülle ayrılır: "Derleme başarısız olursa, günlüğü okuyun." |
| 4.4 | "Eğer" gereksizdir. "-se" eki yeter. |
| 4.5 | Noktalı virgül kullanma. İki cümle yaz. |
| 4.6 | İkiden çok öge varsa madde listesi kullan. |

**Kural 4.6, liste kuralları:**

- Giriş cümlesi iki nokta ile biter.
- Her madde büyük harfle başlar.
- Tam cümle olan madde nokta alır. Virgül veya noktalı virgül almaz.
- Son madde nokta alır.
- Liste içinde liste olmaz.
- Emir ile bilgi aynı listede olmaz.

Kural 4.2, kısalık ile eksiklik arasındaki farktır. Sade Türkçe kısa cümledir, telgraf değildir. Ekler ve bağlaçlar yerinde kalır.

### Bölüm 5. Prosedürel Yazım

| Kural | Yönerge |
|---|---|
| 5.1 | Bir cümle, bir işlem. |
| 5.2 | Emir kipi kullan: "Göçü çalıştırın." |
| 5.3 | Koşulu emirden önce yaz. |
| 5.4 | Sınır ve sonuç, kendi işleminin yanında durur: "Göçü çalıştırın. Göç en fazla 5 dakika sürer." |
| 5.5 | Not bilgi verir. Emir, zorunluluk veya sınır içermez. |

**Not testi:** Bütün notları sil, sonra prosedürü oku. Okur işi yine de doğru yapabilir.

**Önce:** Client'ı configure etmeden önce dashboard üzerinden API anahtarınızı almanız gerekmektedir ki bu işlemi Ayarlar bölümünden gerçekleştirebilirsiniz.
**Sonra:** API anahtarını panelden alın. Anahtar, **Ayarlar** bölümündedir. Sonra istemciyi bu anahtarla yapılandırın.

### Bölüm 6. Açıklayıcı Yazım

| Kural | Yönerge |
|---|---|
| 6.1 | Cümle başına bir yeni bilgi ver. |
| 6.2 | En fazla 16 kelime. |
| 6.3 | Paragraf başına bir konu. |
| 6.4 | Paragraf başına en fazla beş cümle. |
| 6.5 | Açıklayıcı metinde emir kipi kullanma. |

Açıklama anlatır. Prosedür yönlendirir. İkisi karışmaz.

### Bölüm 7. Uyarılar

| Kural | Yönerge |
|---|---|
| 7.1 | Risk düzeyini adlandır. "UYARI" insana zarar demektir. "DİKKAT" veri veya donanım kaybı demektir. |
| 7.2 | Önce emri veya koşulu yaz. |
| 7.3 | Sonra riski yaz. |

İkisi birlikte geçerliyse "UYARI" kullan. Emri açıklamanın arkasına gömme.

**Önce:** Üretim ortamında zorlama bayrağının etkin olması durumunda bazı koşullarda veri kaybı yaşanabileceği unutulmamalıdır.
**Sonra:** DİKKAT: `--force` bayrağını üretim ortamında kullanmayın. Bu bayrak, kaynakla eşleşmeyen satırları siler.

### Bölüm 8. Noktalama ve Kelime Sayımı

| Kural | Yönerge |
|---|---|
| 8.1 | Noktalı virgül kullanma. |
| 8.2 | Ters tırnak içindeki kod, komut ve dosya yolu tek kelime sayılır. |
| 8.3 | Sayı ile birimi tek kelime sayılır: "200 ms". |
| 8.4 | Kısaltma ve özel ad tek kelime sayılır. |
| 8.5 | Parantez içindeki metin tek kelime sayılır. |
| 8.6 | Listede giriş cümlesi iki nokta ile biter. Her madde kendi kelime bütçesine sahiptir. |
| 8.7 | Uzun çizgi (—) ve orta çizgi (–) kullanma. |

Kural 8.2 yazılım metinlerinde işe yarar. `./gradlew :app:assembleDebug` tek kelime sayılır. Uzun komutlar cümle bütçeni bitirmez.

Kural 8.7, İngilizceden geçen bir alışkanlığı keser. TDK'ya göre uzun çizgi satır başında konuşmayı gösterir. Cümle ortasında ara söz yapmaz. Türkçede ara sözü virgül ya da parantez ayırır.

**Önce:** Yapılandırma dosyası — varsayılan adı `sqlpipe.yaml` — kök dizinde durur.
**Sonra:** Yapılandırma dosyası kök dizinde durur. Varsayılan adı `sqlpipe.yaml`.

### Bölüm 9. Türkçe Yazım Denetimi

Bu bölümün İngilizce karşılığı yoktur. Kurallar TDK Yazım Kuralları'na dayanır ve makineyle aranabilir.

| Kural | Yönerge |
|---|---|
| 9.1 | Bağlaç olan "de/da" ayrı yazılır. Hâl eki olan "-de/-da" bitişik yazılır. |
| 9.2 | Bağlaç olan "ki" ayrı yazılır. |
| 9.3 | Soru eki "mi/mı/mu/mü" ayrı yazılır. |
| 9.4 | Özel ada, kısaltmaya ve kod adına gelen çekim eki kesme işaretiyle ayrılır. |
| 9.5 | Ünsüz benzeşmesine uy: "kitapta", "Docker'da", "GitHub'ta". |
| 9.6 | Türkçe karakterleri eksiksiz kullan. Kod ve tanımlayıcı içinde değiştirme. |
| 9.7 | Düzeltme işaretini anlam ayırdığında kullan: "kâr", "hâlâ", "âdet". |

**Kural 9.1 testi:** Kelimeyi cümleden atabiliyorsan bağlaçtır, ayrı yaz.
"Bu ayar da geçerlidir." (bağlaç, ayrı). "Bu ayarda hata var." (hâl eki, bitişik).

**Kural 9.2 istisnaları** bitişik yazılır: "oysaki", "mademki", "hâlbuki", "sanki", "çünkü", "belki", "meğerki".

**Kural 9.4, kısaltmalarda ek uyumu.** Ek, kısaltmanın **okunuşuna** göre seçilir. Yazılım metinlerinin en sık hatası budur:

| Doğru | Okunuş | Yanlış |
|---|---|---|
| API'yi, API'nin | a-pe-i | APİ'yi, API'ı |
| SQL'i, SQL'de | es-ku-el | SQL'yi, SQL'da |
| URL'i, URL'de | u-er-el | URL'yi, URL'ı |
| JSON'u, JSON'a | ce-son | JSON'ı |
| HTTP'nin, HTTP'ye | ha-te-te-pe | HTTP'nın |
| XML'i, XML'den | iks-em-el | XML'yi |
| ID'yi, ID'si | ay-di | ID'ı |
| SDK'yı, SDK'nın | es-de-ka | SDK'yi |
| UI'ı, UI'da | yu-ay | UI'yi |

Kod adları okunduğu gibi ek alır: `Docker'ı`, `Kotlin'de`, `Gradle'ı`, `Compose'u`, `build.gradle.kts`'yi.

Yapım eki kesme ile ayrılmaz: "Türkçeleştirmek", "Googlelamak" değil "Google'da aramak".

### Bölüm 10. Tutarlılık

| Kural | Yönerge |
|---|---|
| 10.1 | Hitap kipi tektir. "Kurun" ile "Kurunuz" ve "Kurmalısınız" aynı belgede geçmez. |
| 10.2 | Bir kavramın tek adı vardır. |
| 10.3 | Türkçe ile İngilizce terimi karıştırma. "Kullanıcı" dediysen "user" deme. |

Kural 10.1, Türkçe teknik yazının bir numaralı tutarsızlığıdır. Aynı belgede beş ayrı kip dönüşür: "Kurun", "Kurunuz", "Kurmalısınız", "Kurulum yapılır", "Kuralım". **Varsayılan seçim: "Kurun".**

## KELİME DİSİPLİNİ

### Kip merdiveni

| Yazdığın | Sade Türkçe |
|---|---|
| -meli, -malı (zorunluluk) | Emir kipi: "Kurun." |
| -meli, -malı (öneri) | Sil. Ya da olguyu yaz: "X daha hızlıdır, çünkü Y." |
| -mesi gerekmektedir | Emir kipi: "Kurun." |
| -mektedir, -maktadır | -ır, -er |
| -ebilmektedir | -ebilir |
| -mesi tavsiye edilir, önerilir | Sil. Ya da nedenini yaz. |
| muhtemelen, olası, büyük ihtimalle | Sil. Ya da koşul yaz: "X olursa, Y olur." |
| -miş (rivayet) | -dı (görülen geçmiş) |
| -ebilir (olanak) | Kalır. Bu kipi kullan. |

### Şişkinlik sözlüğü

Bu tablo, yapay zekâ Türkçesinin ve kurum yazışma dilinin tipik kalıplarını sade karşılıklarına eşler. Kelime bir olgu taşımıyorsa değiştirme, sil.

| Şişkinlik | Bunu yaz |
|---|---|
| gerçekleştirmek | Gerçek fiil: "kurulum gerçekleştir" → "kur" |
| sağlamak (yardımcı) | Gerçek fiil: "erişim sağlamak" → "erişmek" |
| -e olanak tanır, imkân sağlar, imkân verir | "-ebilirsiniz" |
| kritik öneme sahiptir, büyük önem taşır, önemlidir | (sil, olguyu yaz) |
| unutulmamalıdır ki, belirtmek gerekir ki | (sil) |
| dikkat çekicidir, göze çarpmaktadır | (sil) |
| bu bağlamda, bu doğrultuda, bu noktada, bu kapsamda | (sil) |
| söz konusu, ilgili (dolgu) | (sil, ya da adını yaz) |
| ... bir şekilde, ... bir biçimde | Zarf: "hızlı bir şekilde" → "hızlıca" |
| oldukça, son derece, bir hayli, epeyce | (sil) |
| kolayca, zahmetsizce, sorunsuz bir şekilde | (sil) |
| kapsamlı, güçlü, sağlam, esnek, yüksek performanslı | (sil, ya da ölçülebilir değeri yaz) |
| başarılı bir şekilde | (sil, "başarıyla tamamlandı" → "tamamlandı") |
| hayata geçirmek | uygulamak, yapmak |
| ele almak | incelemek, düzeltmek |
| göz atmak | okumak |
| ihtiyaç duymaktadır | gerekir |
| yer almaktadır, bulunmaktadır | vardır, ya da (sil) |
| amaçlamaktadır, hedeflemektedir | (sil, ne yaptığını yaz) |
| -den dolayı, -den kaynaklı olarak | çünkü |
| gerekli olması durumunda, ihtiyaç hâlinde | gerekirse |
| ... olması durumunda | -se: "hata olması durumunda" → "hata olursa" |
| ve/veya | Birini seç, ya da "X, Y ya da ikisi" |
| vb., vs. | Adlarını yaz, ya da "ve diğerleri" |
| örn. | örneğin |
| herhangi bir | (sil): "herhangi bir sorunuz varsa" → "sorunuz varsa" |
| şu anda, şimdi | (sil) |
| ancak, fakat, lakin | ama |
| dolayısıyla, bu nedenle, bundan ötürü | Birini seç ve koru |
| aşağıdaki, yukarıdaki | Adını yaz: "aşağıdaki tablo" → "Tablo 2" |
| basitçe, sadece, yalnızca (dolgu) | (sil) |
| implemente etmek, handle etmek, check etmek | uygulamak, işlemek, denetlemek |
| optimize etmek | hızlandırmak ya da küçültmek (hangisiyse) |
| deploy etmek | yayına almak |

### Eş anlamlı toplama

Belgenin tamamında her kavram için tek kelime kullan (Kurallar 1.1, 10.2).

| Kavram | Seçenekler, birini seç |
|---|---|
| ayar | ayar / yapılandırma / konfigürasyon / seçenek |
| doğrulama | doğrula / kontrol et / denetle / teyit et / emin ol |
| silme | sil (veri) / kaldır (bileşen) / temizle / yok et |
| çalıştırma | çalıştır / yürüt / koştur / başlat |
| hata | hata / sorun / problem / arıza |
| oluşturma | oluştur / yarat / üret / meydana getir |
| güncelleme | güncelle / yenile / tazele |
| kullanıcı | kullanıcı / user / son kullanıcı |

## Dokunulmazlar

Bunlar teknik addır. Kelime kuralları bunları bozsa bile aynen kalır:

- Kod blokları, satır içi kod, tanımlayıcılar, CLI komutları, bayraklar, dosya yolları
- Alıntılanan hata mesajları ve günlük satırları
- Ürün adları, API uç noktaları, yapılandırma anahtarları
- Arayüz etiketleri ve düğme adları
- Sayı ile birimi

Türkçe ek bunlara kesme işaretiyle eklenir: `docker-compose.yml`'yi, `--force`'u, `AndroidManifest.xml`'de.

**Olgular da dokunulmazdır.** Üslubu düzelt, içeriği değil. Kaynakta sayı, neden veya kesin terim yoksa uydurma. Genel ifade genel kalır.

## Sadece Doküman Değil

Aynı kurallar, farklı hedefler. Uzun uyarlamalar `references/kullanim-alanlari.md` dosyasındadır.

- **Hata mesajları:** ne olduğunu görülen geçmişle yaz, nedeni biliniyorsa ekle, çözümü emir kipiyle ver. "Bir hata oluştu" yasak.
- **Runbook:** emir kipi, koşul önce, uyarı adımdan önce.
- **Olay raporu:** yalnızca görülen geçmiş. Saat, oran ve süre ver.
- **Sürüm notları:** kırıcı değişiklik uyarı kalıbını izler. Önce emir, sonra risk.
- **Commit ve PR:** başlık emir kipi, en fazla 12 kelime. Gövde açıklayıcıdır.
- **Arayüz metni:** düğme adı fiil, en fazla üç kelime. Boş durum metni ne yapılacağını söyler.
- **Ajan yönergesi (prompt, AGENTS.md):** soru soramayan bir okur için yazılmış prosedürdür. Bir cümle bir yönerge, "-meli" yok.

## Teslimden Önce Öz Denetim

Bu adım isteğe bağlı değildir. Taslağını şu sekiz denetimden geçir:

1. En uzun üç cümleni say. 12 veya 16 sınırını aşanı böl.
2. Şunları ara: `mektedir`, `maktadır`, `meli`, `malı`, `tarafından`, `gerçekleştir`, `sağla`, `bir şekilde`, `bir biçimde`, `;`, `vb.`, `vs.`, `ve/veya`, `oldukça`, `önem`, `—`, `–`.
3. Her `-se`, `-sa`, `-ursa` ve `durumunda` için: koşul cümlenin başında mı?
4. `-arak`, `-erek`, `-ıp`, `-ip` ara. Bir cümlede birden çoksa cümleyi böl.
5. Hitap kipini say. "-ın" mı, "-ınız" mı, "-malısınız" mı? Tek olmalı.
6. Büyük harfli kısaltmaların eklerini denetle. Kesme işareti var mı? Ek okunuşa uyuyor mu?
7. Bağlaç "de/da" ve "ki" ayrı mı? Soru eki "mi" ayrı mı?
8. Eş anlamlı dönüşümü var mı? Her kavram için tek kelime kaldı mı?

Bulduklarını düzelt, sonra teslim et. Tam denetim için `references/kontrol-listesi.md` dosyasını çalıştır.

## Tam Örnek

**Önce (tipik yapay zekâ Türkçesi):**

> **Bağlantı zaman aşımları.** sqlpipe'ın takılması veya `dial tcp: i/o timeout` hatası ile başarısız olması durumunda, sqlpipe'ı çalıştıran host'un Postgres portuna (genellikle 5432) erişebildiğinden emin olunması gerekmektedir ki bu durum çoğunlukla bir güvenlik grubu veya firewall kuralının bağlantıyı bloklamasından kaynaklanmaktadır. Yönetilen bir veritabanına (RDS, Cloud SQL vb.) bağlanıyorsanız, instance'ın sqlpipe'ın IP'sinden gelen bağlantılara izin verdiğini teyit etmeniz kritik öneme sahiptir. Ayrıca yavaş bir ağ yolu varsayılan timeout'u tetikleyebileceğinden config dosyanızdaki `source.connect_timeout_seconds` değerini artırmayı da deneyebilirsiniz.

**Sonra (prosedürel, fiil = "doğrulayın", koşullar başta, bir cümle bir işlem):**

> **Bağlantı zaman aşımları.** sqlpipe, Postgres portuna bağlanamayınca `dial tcp: i/o timeout` hatasıyla durur. Varsayılan port 5432'dir.
>
> 1. sqlpipe'ı çalıştıran makinenin Postgres portuna eriştiğini doğrulayın. Bunu genellikle bir güvenlik duvarı kuralı engeller.
> 2. Veritabanı yönetiliyorsa (RDS, Cloud SQL), sunucunun sqlpipe'ın IP adresini kabul ettiğini doğrulayın.
> 3. Ağ yavaşsa, ayar dosyasındaki `source.connect_timeout_seconds` değerini artırın.

**Ne değişti:** 40 kelimelik cümleler 12 kelimenin altına bölündü. "Emin olunması gerekmektedir" ve "teyit etmeniz" tek fiile indi: "doğrulayın". Her koşul emrin önüne geçti. "Kritik öneme sahiptir" ve "vb." silindi. Kod ve hata metni değişmedi.

## Sınırlar

Bu kurallar teknik olgular ve yönergeler içindir. Edebî metne, pazarlama metnine ve marka diline uygulama: kurallar ikna dilini tasarım gereği siler. Kullanıcı pazarlama metni için sade Türkçe isterse bunu söyle ve dokümanlar için öner.

Bu beceri resmî değildir. TDK Yazım Kuralları yazım konusunda tek yetkili kaynaktır. ASD-STE100, ASD'nin tescilli markasıdır ve bu beceri ASD ile ilişkili değildir.

## Referanslar

- `references/kontrol-listesi.md`: aranabilir kalıplarla tam denetim listesi
- `references/kullanim-alanlari.md`: hata mesajı, runbook, olay raporu, commit, arayüz metni uyarlamaları
