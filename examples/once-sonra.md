# Önce / sonra

Sol taraf, bir modelin Türkçe çalışırken gerçekten ürettiği metin tipidir. Sağ taraf aynı olguları taşır. Her örneğin altında hangi kuralın işlediği ve neyin kazanıldığı yazar.

Örnekler bir Android projesinden alınmıştır: Kotlin, Compose, özellik modülleri.

---

## 1. Ajanın değişiklik özeti (açıklayıcı)

Bir ajanın en sık ürettiği metin budur: "ne yaptım" özeti.

**Önce**

> Talebiniz doğrultusunda abonelik iptal akışındaki dialogların gösterilmemesi sorununu inceledim ve gerekli düzenlemeleri gerçekleştirdim.
>
> Öncelikle `SubscriptionManagementViewModel` sınıfında yer alan `onCancelClicked` metodunun, taahhüt ve gecikme kontrollerini yapmadan doğrudan iptal akışını tetiklediği tespit edilmiştir. Bu durum, kullanıcıların taahhüt bilgisi olmadan iptal işlemini tamamlayabilmelerine sebep olmaktaydı.
>
> Yapılan düzenlemeler kapsamında; ilgili kontrollerin repository katmanından dönen response üzerinden yapılması sağlanmış, ayrıca `SubscriptionManagementRefundContract` içerisine yeni stateler eklenerek dialog yönetiminin merkezi bir şekilde handle edilmesi mümkün hale getirilmiştir.
>
> Bu değişiklikler ile birlikte kod okunabilirliği artırılmış ve kullanıcı deneyimi iyileştirilmiştir. Herhangi bir sorunuz olması durumunda yardımcı olmaktan memnuniyet duyarım.

**Sonra**

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

Kurallar: 1.8 (`yapılması sağlanmış` fiile döndü), 3.2 (`olmaktaydı` → `tamamladı`), 3.8 (`tespit edilmiştir` → `atladı`), 4.1, 8.1 (noktalı virgül), 9.4 (`dialogların` → `uyarı kutuları`).

Kazanılan: son paragraf tamamen silindi. "Kod okunabilirliği artırılmış ve kullanıcı deneyimi iyileştirilmiştir" cümlesi hiçbir olgu taşımaz. Yerine ölçülebilir bir sonuç geldi: testler geçti.

---

## 2. Ajan yönergesi, `AGENTS.md` veya `CLAUDE.md` (prosedürel)

Bu, kuralların en çok işe yaradığı yerdir. Model "-meli" ekini isteğe bağlı okur.

**Önce**

> Bu projede çalışırken aşağıdaki kurallara dikkat edilmelidir:
>
> - Yeni bir feature modülü eklenirken mevcut modül yapısı incelenmeli ve aynı pattern takip edilmelidir.
> - ViewModel'lerde state yönetimi için Contract pattern kullanılması tercih edilmelidir.
> - Test yazarken mümkün olduğunca mock kullanılmaması önerilir.
> - Commit atmadan önce ktlint çalıştırılması faydalı olacaktır.

**Sonra**

> Bu projede şu kurallara uy:
>
> - Yeni bir özellik modülü eklerken var olan modül yapısını izle.
> - ViewModel'de durum yönetimi için Contract kalıbını kullan.
> - Testte mock yerine fake kullan.
> - Commit'ten önce `ktlint` çalıştır.

Kurallar: 3.1 (emir kipi), kip merdiveni (`-melidir` → emir, `önerilir` ve `faydalı olacaktır` → emir), 3.3 (edilgen çatı etken oldu), 1.7 (`feature` → `özellik`, `pattern` → `kalıp`).

Kazanılan: dört maddenin dördü de yönerge oldu. `-melidir`, `önerilir` ve `faydalı olacaktır` üç ayrı zorunluluk derecesi gibi okunur. Bir ajan bunları atlar. Ajan yönergesi tek bir okura seslenir, bu yüzden ikinci tekil doğaldır. Kural 10.1 kipin tek olmasını ister, hangi kip olduğunu değil.

---

## 3. Kök neden açıklaması (prosedürel)

**Önce**

> Testin fail olmasının sebebi büyük ihtimalle coroutine scopeunun test dispatcher ile düzgün bir şekilde handle edilememesinden kaynaklanıyor olabilir. `runTest` bloğu içerisinde `viewModelScope` kullanıldığında, dispatcherın inject edilmemesi durumunda testin main threadi beklemesi söz konusu olabilmektedir. Bu tarz durumlarda genellikle `MainDispatcherRule` eklenmesi tavsiye edilmektedir. Ayrıca `advanceUntilIdle()` çağrısının da eklenmesi faydalı olabilir.

**Sonra**

> Test, `viewModelScope` içindeki işi beklemeden bitti. `viewModelScope`, `Dispatchers.Main` kullanır. Testte bu dispatcher yok.
>
> İki değişiklik gerekir:
>
> 1. Test sınıfına `MainDispatcherRule` ekleyin.
> 2. Doğrulamadan önce `advanceUntilIdle()` çağırın.
>
> Bunu çalıştırıp doğrulamadım. Testi çalıştırın, sonucu paylaşın.

Kurallar: 3.2 (`olabilmektedir` → `yok`), 9.4 (`scopeunun` → `viewModelScope`, `dispatcherın` → `dispatcher`), 4.1, 5.2 (emir kipi).

Kazanılan: sahte belirsizlik gitti. Soldaki metin `büyük ihtimalle`, `olabilir`, `söz konusu olabilmektedir`, `genellikle` ve `faydalı olabilir` ile beş yere belirsizlik serpiştirir. Sağdaki metin mekanizmayı kesin anlatır ve tek gerçek belirsizliği son cümlede adlandırır: yazar bunu çalıştırmadı.

---

## 4. PR açıklaması (açıklayıcı)

**Önce**

> ## Açıklama
> Bu PR ile birlikte ödeme akışında yaşanan timeout sorunlarının giderilmesi amaçlanmaktadır. Mevcut implementasyonda retry mekanizması bulunmadığından dolayı, network kaynaklı geçici hatalarda kullanıcıların ödeme işlemini tamamlayamadığı gözlemlenmiştir.
>
> ## Yapılan Değişiklikler
> - `PaymentsRepositoryImpl` içerisine exponential backoff ile retry logic eklenmiştir.
> - Timeout süresi 10 saniyeden 30 saniyeye çıkarılmıştır.
> - İlgili unit testler yazılmıştır.
>
> ## Test
> Lokalde test edilmiş olup herhangi bir sorun ile karşılaşılmamıştır.

**Sonra**

> ## Sorun
> Ödeme isteği, ağ hatasında yeniden denemedi. Kullanıcı ödemeyi tamamlayamadı.
>
> ## Değişiklik
> - `PaymentsRepositoryImpl` artık üstel geri çekilmeyle yeniden dener.
> - Zaman aşımı 10 saniyeden 30 saniyeye çıktı.
> - `PaymentsRepositoryImplTest` yeni testler aldı.
>
> ## Doğrulama
> Birim testleri geçti. Ağ hatasını cihazda uçak moduyla denedim. Ödeme, ikinci denemede tamamlandı.

Kurallar: 3.8 (`eklenmiştir` → `dener`), 1.8 (`giderilmesi amaçlanmaktadır` → sorunu yaz), 3.3 (`gözlemlenmiştir` → `tamamlayamadı`), 1.7 (`timeout` → `zaman aşımı`).

Kazanılan: "Lokalde test edilmiş olup herhangi bir sorun ile karşılaşılmamıştır" cümlesi neyin denendiğini gizler. Bu cümlenin düzeltmesi kelime seçimi değildir. Eksik olgu yazarın elindedir: neyi, nasıl denedin? Elinde yoksa ne yaptıysan onu yaz.

---

## 5. Kod inceleme yorumu (prosedürel)

**Önce**

> Bu kısımda null check yapılmasının faydalı olabileceğini düşünüyorum. Ayrıca `!!` operatörünün kullanımından kaçınılması genel olarak önerilmektedir. Belki `?.let` bloğu ile handle edilmesi daha uygun olabilir. Ne düşünürsünüz?

**Sonra**

> `user!!` satırı, oturum kapanınca çöker. `logout()` çağrısı `user` alanını `null` yapar.
>
> `user?.let { }` kullanın. Ya da erken dönün: `val u = user ?: return`.

Kurallar: 1.8 (`null check yapılmasının` → `çöker`), kip merdiveni (`faydalı olabileceğini düşünüyorum`, `önerilmektedir`, `belki`, `olabilir` silindi), 5.2 (emir kipi).

Kazanılan: yorum artık bir gözlem değil, bir bulgu. Soldaki metin dört katmanlı nezaketin altına gerçek hatayı gömer: kod çöküyor. Sağdaki metin önce çökmeyi, sonra nedenini, sonra iki çözümü verir.

---

## 6. Olay raporu (açıklayıcı)

**Önce**

> Bazı kullanıcılarımızın uygulamaya giriş yapmasında yaşanabilecek bir sorun tespit edilmiş olup, ekiplerimiz tarafından konu ile ilgili gerekli çalışmalar ivedilikle başlatılmıştır. Yaşanan mağduriyetten dolayı özür dileriz.

**Sonra**

> 09:14 ile 09:52 arasında Android istemcide oturum açma isteklerinin %38'i başarısız oldu. 09:10'daki yapılandırma değişikliği, token yenileme adresini eskisiyle değiştirdi. Değişikliği 09:48'de geri aldık. Yapılandırma değişikliklerine kanarya dağıtımı ekledik.

Kurallar: 3.8 (`başlatılmıştır` → `ekledik`), 3.4 (`tarafından` silindi), 3.3 (edilgen çatı etken oldu), şişkinlik (`ilgili`, `gerekli`, `ivedilikle`).

Kazanılan: soldaki metin kaç kişinin, ne kadar süre, neden etkilendiğini söylemez. Sağdaki metin dördünü de söyler. Sayılar kaynaktan gelir. Kaynakta yoksa uydurulmaz, genel ifade genel kalır.
