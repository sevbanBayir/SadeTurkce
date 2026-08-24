# Denetim listesi

Bu denetimi her taslakta, teslimden önce çalıştır. Denetimler mekanikten yoruma doğru sıralanmıştır.

## Mekanik denetimler (aranabilir)

Taslakta her kalıbı ara. Kod bloğu ve alıntı dışındaki her eşleşme bir ihlaldir.

| Ara | İhlal | Düzeltme |
|---|---|---|
| `mektedir`, `maktadır` | Bürokratik geniş zaman (3.2) | `-ır`, `-er`: "çalışmaktadır" → "çalışır" |
| `meli`, `malı`, `melidir`, `malıdır` | Yasak kip (3.1) | Zorunluluksa emir kipi. Öneriyse sil. |
| `gerekmektedir`, `gerekmekte` | Yasak kip (3.2) | "gerekir", ya da emir kipi |
| `tarafından` | Edilgen özne (3.4) | Etken cümle kur. |
| `gerçekleştir`, `sağlan`, `sağlamak` | Yardımcı fiil yığını (1.4, 3.7) | Gerçek fiil kullan. |
| `-mesi`, `-ması` + `gerek/sağlan/yapıl` | Adlaştırma (1.8) | Fiile çevir: "kurulmasını sağlayın" → "kurun" |
| `bir şekilde`, `bir biçimde` | Dolgu | Zarf: "hızlı bir şekilde" → "hızlıca" |
| `arak `, `erek `, `ıp `, `ip ` | Ulaç zinciri (3.5) | Bir cümlede birden çoksa böl. |
| `;` | Noktalı virgül (8.1) | İki cümle yaz. |
| `vb.`, `vs.`, `örn.` | Kısaltma dolgusu | Adlarını yaz, "örneğin" |
| `ve/veya` | Belirsizlik | Birini seç. |
| `oldukça`, `son derece`, `bir hayli` | Dolgu | Sil. |
| `önem`, `kritik`, `dikkat çekici` | Dolgu | Sil, olguyu yaz. |
| `kapsamlı`, `güçlü`, `sorunsuz`, `kolayca`, `zahmetsizce` | Dolgu | Sil, ya da ölçülebilir değeri yaz. |
| `olanak tanı`, `imkân sağla`, `imkan ver` | Dolgu kalıbı | "-ebilirsiniz" |
| `unutulmamalıdır`, `belirtmek gerekir` | Dolgu kalıbı | Sil. |
| `bu bağlamda`, `bu doğrultuda`, `bu noktada` | Dolgu | Sil. |
| `söz konusu`, `ilgili` (dolgu) | Belirsiz gönderim | Adını yaz, ya da sil. |
| `durumunda`, `hâlinde`, `halinde` | Ağır koşul kalıbı | `-se`: "hata olması durumunda" → "hata olursa" |
| `herhangi bir` | Dolgu | Sil. |
| `aşağıdaki`, `yukarıdaki` | Belirsiz gönderim | Hedefin adını yaz. |
| `ancak`, `fakat`, `lakin` | Eş anlamlı dönüşümü | "ama" seç ve koru. |
| `başarılı bir şekilde`, `başarıyla` | Dolgu | Sil. |
| `implemente`, `handle`, `check et`, `deploy et`, `optimize et` | Gereksiz İngilizce fiil (1.7) | uygula, işle, denetle, yayına al, hızlandır |
| `-miş`, `-mış` (rivayet) | Yasak kip (3.8) | Görülen geçmiş: `-dı` |

## Türkçe yazım denetimleri

| Ara | İhlal | Düzeltme |
|---|---|---|
| ` de `, ` da ` | Bağlaç mı hâl eki mi? (9.1) | Cümleden atılabiliyorsa bağlaçtır, ayrı yaz. |
| `ki` (bitişik) | Bağlaç "ki" (9.2) | Ayrı yaz. İstisnalar: oysaki, mademki, hâlbuki, sanki, çünkü, belki |
| `mi`, `mı`, `mu`, `mü` (bitişik) | Soru eki (9.3) | Ayrı yaz: "çalışıyor mu" |
| Büyük harfli kısaltma + ek, kesmesiz | Kesme eksik (9.4) | `API'yi`, `SQL'i`, `JSON'u` |
| `API'ı`, `SQL'yi`, `JSON'ı`, `URL'yi`, `ID'ı` | Ek okunuşa uymuyor (9.4) | `API'yi`, `SQL'i`, `JSON'u`, `URL'i`, `ID'yi` |
| `GitHub'da`, `Docker'ta` | Ünsüz benzeşmesi (9.5) | `GitHub'ta`, `Docker'da` |
| `i`, `s`, `g`, `u`, `o`, `c` (Türkçe karakter yerine) | Eksik karakter (9.6) | Türkçe karakter kullan. Kod içinde değiştirme. |

## Sayılabilir denetimler

1. **Cümle uzunluğu.** Her cümlenin kelimesini say. Prosedür sınırı 12, açıklama ve not sınırı 16.
   Ters tırnak içindeki kod, sayı ile birimi ve kısaltma tek kelime sayılır (8.2, 8.3, 8.4).
   Listede iki nokta cümleyi bitirir; her madde kendi bütçesine sahiptir (8.6).
2. **Paragraf uzunluğu.** En fazla beş cümle (6.4).
3. **Tamlama uzunluğu.** Üç kelimeyi aşan tamlamayı "için", "ile", "-deki" ile kır (2.1).
4. **Cümle başına işlem.** Bir (5.1).
5. **Liste düzeni.** Giriş cümlesinde iki nokta. Maddeler büyük harfle başlar. Tam cümle olan madde nokta alır, virgül almaz. İç içe liste yok. Emir ile bilgi aynı listede değil (4.6).

## Yorum denetimleri

6. **Sınıflandırma.** Her bölüm ya prosedürel ya açıklayıcıdır. Prosedür emir kipindedir, açıklama değildir.
7. **Çatı.** Her edilgen cümlede: özne gerçekten bilinmiyor mu, bölüm açıklayıcı mı? Değilse etken yaz (3.3, 3.4).
8. **Koşul yeri.** Her koşul emrinin önünde ve virgülle ayrılmış (4.3).
9. **Eş anlamlı dönüşümü.** Belge boyunca kavram başına tek kelime (1.1, 10.2). Şu kümeleri tara: ayar/yapılandırma/konfigürasyon, doğrula/kontrol et/denetle, sil/kaldır/temizle, çalıştır/yürüt/başlat, hata/sorun/problem.
10. **Hitap kipi.** Belge boyunca tek kip (10.1). "Kurun" ile "Kurunuz" karışmaz.
11. **Uyarılar.** Önce emir veya koşul, sonra risk (7.2, 7.3). Hem insana hem veriye risk varsa "UYARI" (7.1).
12. **Sınırlar işlemin yanında.** Sonuç ve sınır, notta değil, adımın içinde (5.4, 5.5).
13. **Not testi.** Bütün notları sil, prosedürü oku. Okur işi yine de doğru yapabiliyor mu? (5.5)
14. **Eksiksizlik.** Ekler ve bağlaçlar yerinde, telgraf üslubu yok (4.2).
15. **Dokunulmazlar sağlam.** Kod, tanımlayıcı, alıntı hata metni, arayüz etiketi ve ürün adı değişmemiş.

## İhlal bildirirken (denetim modu)

Her ihlal için şunu ver: kural numarası, hatalı metin, kurala uygun karşılığı. Yalnızca `SKILL.md` içinde bulunan kural numaralarını kullan.
Kullanıcı TDK uygunluğu istediyse raporu şu cümleyle bitir: "Hiçbir araç TDK yazım uygunluğunu garanti edemez. Son onay yazarındır. Yetkili kaynak, TDK Yazım Kılavuzu'dur."
