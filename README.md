# Sade Türkçe

Türkçe yazan bir dil modeli iki ayrı kaynaktan bozulur.

Birincisi eğitim verisindeki kurum yazışma dilidir: "gerçekleştirilmesi gerekmektedir", "söz konusu olabilmektedir", "ilgili çalışmalar başlatılmıştır". İkincisi İngilizceden geçen kalıplardır: "-e olanak tanır", "bir şekilde", ara söz çizgisi. İkisi birleşince uzun, edilgen ve olgu taşımayan metin çıkar.

Bu depo, o metni ölçülebilir kurallara bağlar. Dört parçadan oluşur:

- **Skill:** kural kataloğunun tamamı, gerektiğinde yüklenir.
- **Output style:** kısa sürüm, her Türkçe yanıtta çalışır.
- **Sistem yönergesi:** skill desteği olmayan araçlar için.
- **Denetleyici:** kuralları sayan bir Python betiği.

Kurallar [ASD-STE100](https://www.asd-ste100.org/) Basitleştirilmiş Teknik İngilizce'nin mantığından gelir. Ama çeviri değildir. Nedenini aşağıda anlatıyorum.

## Sorun ne

Aşağıdaki metin, bir ajanın Türkçe çalışırken ürettiği tipik değişiklik özetidir.

> Talebiniz doğrultusunda abonelik iptal akışındaki dialogların gösterilmemesi sorununu inceledim ve gerekli düzenlemeleri gerçekleştirdim.
>
> Öncelikle `SubscriptionManagementViewModel` sınıfında yer alan `onCancelClicked` metodunun, taahhüt ve gecikme kontrollerini yapmadan doğrudan iptal akışını tetiklediği tespit edilmiştir. Bu durum, kullanıcıların taahhüt bilgisi olmadan iptal işlemini tamamlayabilmelerine sebep olmaktaydı.
>
> Yapılan düzenlemeler kapsamında; ilgili kontrollerin repository katmanından dönen response üzerinden yapılması sağlanmış, ayrıca `SubscriptionManagementRefundContract` içerisine yeni stateler eklenerek dialog yönetiminin merkezi bir şekilde handle edilmesi mümkün hale getirilmiştir.
>
> Bu değişiklikler ile birlikte kod okunabilirliği artırılmış ve kullanıcı deneyimi iyileştirilmiştir. Herhangi bir sorunuz olması durumunda yardımcı olmaktan memnuniyet duyarım.

Metin doğrudur. Sorun doğruluk değil, okuma maliyetidir. En uzun cümlesi 28 kelimedir. Son paragrafı hiçbir olgu taşımaz. Hangi dosyaların değiştiğini bulmak için üç kez okumak gerekir.

Aynı olgular, kurallarla:

> İptal akışında uyarı kutuları görünmedi. Nedenini buldum ve düzelttim.
>
> `SubscriptionManagementViewModel.onCancelClicked`, taahhüt ve gecikme denetimini atladı. Doğrudan iptal akışını başlattı. Bu yüzden kullanıcı, taahhüdünü görmeden iptali tamamladı.
>
> Üç dosyayı değiştirdim:
>
> - `SubscriptionManagementViewModel`: denetimi, depo katmanının döndüğü yanıttan okur.
> - `SubscriptionManagementRefundContract`: iki yeni durum aldı.
> - `DomainErrorExtensions`: iki hata metnini güncelledim.
>
> Testleri çalıştırdım. Hepsi geçti.

En uzun cümle 28 kelimeden 7 kelimeye indi. İçi boş kapanış paragrafı gitti, yerine ölçülebilir bir sonuç geldi. Değişen dosyalar listeye çıktı.

Altı tam örnek: [`examples/once-sonra.md`](examples/once-sonra.md). Ajan yönergesi, kök neden açıklaması, PR açıklaması, kod inceleme yorumu ve olay raporu.

## Neden çeviri değil

ASD-STE100 İngilizceye özel bir kontrollü dildir. Kurallarını Türkçeye taşırken dördü kırılır.

**Kelime sınırları anlamını yitirir.** Türkçe eklemeli bir dildir. "yapılandırabilirsiniz" tek kelimedir, İngilizcesi dört kelimedir. 20 kelimelik bir Türkçe cümle, 35 kelimelik bir İngilizce cümleye denktir. Bu depo sınırları 12 ve 16 kelimeye çeker.

**Etken çatı kuralı ters çalışır.** İngilizcede edilgen çatı bir sapmadır. Türkçede teknik yazının varsayılanıdır: "kurulur", "yapılandırılır", "denetlenmesi sağlanır". Kural bu yüzden çatıyı değil kipi hedefler: prosedürde emir kipi, belgenin tamamında tek biçim.

**Şişkinliğin kaynağı başkadır.** İngilizcede `leverage`, `robust`, `seamlessly`. Türkçede adlaştırma ve yardımcı fiil: "doğrulama işleminin gerçekleştirilmesi". Bir de bürokratik `-mektedir` ile zincirleme isim tamlaması: "veritabanı bağlantı havuzu zaman aşımı ayarı değeri".

**Türkçenin kendi mekanik kuralları vardır.** Bağlaç olan "de/da" ayrı yazılır. Kısaltmaya gelen ek kesme işaretiyle ayrılır ve kısaltmanın okunuşuna uyar: `API'yi`, `SQL'i`, `JSON'u`. İngilizce tanımlayıcılarla dolu Türkçe dokümanlarda en sık görülen yanlış budur. Makineyle aranabilir.

## Kurallar ne yapar

10 bölüm, 51 numaralı kural. Her kuralın somut bir işi vardır.

| Kural | Neden var |
|---|---|
| Yönergede 12, açıklamada 16 kelime | Uzun cümle, okuru geri dönmeye zorlar |
| Adlaştırma yasağı | "Doğrulama işleminin gerçekleştirilmesi" eylemi gizler, "doğrulayın" göstermez |
| `-mektedir` yasağı | Kurum yazışma dilinin taşıyıcısıdır, hiçbir anlam katmaz |
| `-meli` yasağı | Okur ve model bunu isteğe bağlı okur |
| Tek hitap kipi | "Kurun / Kurunuz / Kurmalısınız / Kurulur" aynı belgede dönüşür |
| Bir cümlede bir yan cümle | `-arak … -ıp … -dığında` zinciri, öznenin izini kaybettirir |
| Tamlama en fazla üç kelime | Okur hangi kelimenin hangisine bağlandığını çözemez |
| Koşul cümlenin başında | Sonda duran koşulu okur, işlemi yaptıktan sonra görür |
| Bir kavram, bir kelime | Eş anlamlı dönüşümü, okura iki ayrı şey varmış izlenimi verir |
| Uzun çizgi yasağı | Türkçede uzun çizgi konuşma çizgisidir, ara söz yapmaz |
| Kesme işareti okunuşa uyar | `APIyi` ve `API'ı` yanlıştır, `API'yi` doğrudur |

Tam katalog: [`skills/sade-turkce/SKILL.md`](skills/sade-turkce/SKILL.md).

### Nerede en çok işe yarar

**Ajan yönergelerinde.** `AGENTS.md` ve `CLAUDE.md` dosyaları, soru soramayan bir okur için yazılmış prosedürlerdir. "-melidir", "önerilir" ve "faydalı olacaktır" üç ayrı zorunluluk derecesi gibi okunur, model üçünü de atlar.

> Yeni bir feature modülü eklenirken mevcut modül yapısı incelenmeli ve aynı pattern takip edilmelidir.

> Yeni bir özellik modülü eklerken var olan modül yapısını izle.

**Kök neden açıklamalarında.** Model, emin olmadığı yerde belirsizliği metnin tamamına serper. Kural, belirsizliği tek bir cümlede toplamaya zorlar.

> Testin fail olmasının sebebi büyük ihtimalle coroutine scopeunun test dispatcher ile düzgün bir şekilde handle edilememesinden kaynaklanıyor olabilir. Bu tarz durumlarda genellikle `MainDispatcherRule` eklenmesi tavsiye edilmektedir.

> Test, `viewModelScope` içindeki işi beklemeden bitti. `viewModelScope`, `Dispatchers.Main` kullanır. Testte bu dispatcher yok. Test sınıfına `MainDispatcherRule` ekleyin. Bunu çalıştırıp doğrulamadım.

Soldaki metin beş yere belirsizlik serper: `büyük ihtimalle`, `olabilir`, `bu tarz durumlarda`, `genellikle`, `tavsiye edilmektedir`. Sağdaki metin mekanizmayı kesin anlatır ve tek gerçek belirsizliği son cümlede adlandırır.

**PR ve commit metinlerinde.** Belirsiz cümle, eksik olguyu gizler. "Lokalde test edilmiş olup herhangi bir sorun ile karşılaşılmamıştır" cümlesi neyin denendiğini söylemez. Bu cümlenin düzeltmesi kelime seçimi değildir: eksik olgu yazarın elindedir.

## Kurulum

**Claude Code eklentisi.** Bu depo aynı zamanda bir eklenti pazarıdır.

```bash
claude plugin marketplace add sevbanBayir/SadeTurkce && claude plugin install sade-turkce@sade-turkce
```

**Elle kopyalama.**

```bash
cp -r skills/sade-turkce ~/.claude/skills/ && cp output-styles/sade-turkce.md ~/.claude/output-styles/
```

**Skill desteği yoksa.** [`prompts/system-prompt.md`](prompts/system-prompt.md) dosyasındaki bloğu kopyala. Sistem yönergene, `AGENTS.md`, `CLAUDE.md` ya da `.cursorrules` dosyana yapıştır. Dar bağlamlar için kısa sürüm de var.

### Skill ile output style farkı

| Parça | Ne zaman çalışır |
|---|---|
| [`skills/sade-turkce/`](skills/sade-turkce/SKILL.md) | Yazma işi uyunca, ya da `/sade-turkce` yazınca |
| [`output-styles/sade-turkce.md`](output-styles/sade-turkce.md) | Her yanıtta |

Skill, kural kataloğunun tamamını bağlama yükler. Uzun bir metni denetlerken ve kural numarası verirken işe yarar. Output style kısa sürümdür ve her Türkçe yanıtta çalışır. İkisi birlikte kullanılabilir.

Output style'ı açmak için `~/.claude/settings.json` dosyasına şunu yaz:

```json
{ "outputStyle": "sade-turkce" }
```

## Denetleyici

`evals/sade_lint.py`, kuralların düzenli ifadeyle yakalanabilen 21 tanesini sayar.

```bash
python3 evals/sade_lint.py --tur prosedurel dosya.md
```

Çıktı JSON'dur. `ihlal_100_kelime` alanı iki metni karşılaştırmak içindir.

Türkçeye özel iki ayrıntıyı doğru işler. Birincisi büyük harf çevrimidir: Python'un `lower()` işlevi `İ` harfini birleşik noktalı `i` yapar ve kalıp eşleşmesini bozar. İkincisi ünsüz yumuşamasıdır: `olanak` kelimesi ek alınca `olanağı` olur.

Yakalayamadıklarını [`evals/README.md`](evals/README.md) açıkça yazar. Bu bir düzenli ifade taramasıdır, biçim bilgisi çözümleyicisi değildir. Edilgen çatıyı `tarafından` olmadan bulamaz. Bağlaç olan "de/da" ile hâl ekini ayıramaz: bu ayrım sözdizimi ister. `hitap_rotasyon` denetimi yanlış pozitif üretir.

## Ölçüm durumu

`examples/once-sonra.md` dosyasındaki altı çift ölçüldü:

```bash
python3 evals/ornek_olc.py
```

| | Önce | Sonra |
|---|---|---|
| İhlal / 100 kelime | 13.85 | 0.00 |
| Toplam ihlal | 41 | 0 |
| Kelime sayısı | 296 | 217 |

**Bu sayı ne anlatır, ne anlatmaz.** Ölçüm örnek metinleri ölçer. Sağ taraftaki metinleri kurallara uyacak biçimde ben yazdım, bu yüzden sıfır beklenen sonuçtur. Sayı, kuralların ölçülebilir olduğunu ve denetleyicinin çalıştığını gösterir. Modelin davranışı hakkında hiçbir şey söylemez.

**Model karşılaştırması henüz yapılmadı.** `evals/senaryolar.json` sekiz Türkçe görev taşır, yöntem `evals/README.md` içinde yazılıdır. Depoda ölçülmemiş sayı yoktur.

## Sınırlar

Kurallar teknik olgular ve yönergeler içindir. Edebî metne, tanıtım metnine ve marka diline uygulama: ikna dilini tasarım gereği silerler.

Bu depo resmî değildir. Yazım konusunda tek yetkili kaynak TDK Yazım Kılavuzu'dur. Hiçbir araç dil uygunluğunu garanti edemez, son onay yazarındır.

Denetleyiciyi bu README'nin üstünde çalıştırdım. Alıntıladığım kötü örnekleri dışarıda bırakmak için:

```bash
grep -v '^>' README.md | python3 evals/sade_lint.py --tur aciklayici -
```

Kendi düzyazımda 988 kelimede 19 ihlal kaldı, yani 100 kelimede 1.92. En uzun cümle 15 kelime. Kalanların çoğu kaçınılmazdır: `-mektedir` yasağını anlatmak için `-mektedir` yazmak gerekir. Bir tanesi de yanlış pozitiftir. Denetleyici, "Türkçe eklemeli bir dildir" cümlesindeki `eklemeli` kelimesini yasak kip sanır. Dil bilimi terimini `-meli` ekinden ayıramaz.

## Lisans ve atıf

MIT. Depo yapısını ve yaklaşımını [AminBlg/SimpleEnglish](https://github.com/AminBlg/SimpleEnglish) (MIT) deposundan aldım. İçeriği Türkçe için yeniden türettim.

ASD-STE100, ASD'nin tescilli markasıdır. Bu depo ASD ile ilişkili değildir.
