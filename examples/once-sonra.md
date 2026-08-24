# Önce / sonra

Sol sütun tipik yapay zekâ Türkçesidir. Sağ sütun aynı olguları taşıyan sade sürümdür. Her örneğin altında hangi kuralın işlediği yazar.

---

## 1. README girişi (açıklayıcı)

**Önce**

> sqlpipe, PostgreSQL tablolarınızı S3'e Parquet formatında senkronize etmenize olanak tanıyan, yüksek performanslı ve kapsamlı bir komut satırı aracıdır. Sağlam mimarisi sayesinde büyük veri setlerini sorunsuz bir şekilde işleyebilmekte, minimum konfigürasyon ile hızlı bir şekilde devreye alınabilmektedir.

**Sonra**

> sqlpipe, PostgreSQL tablolarını S3'e Parquet dosyası olarak kopyalar. Tek bir yapılandırma dosyası ister. Bir tabloyu tam olarak ya da yalnızca değişen satırlarıyla kopyalayabilirsiniz.

Kurallar: 3.2 (`-mekte` → `-ır`), 1.4 (`olanak tanıyan` → `-ebilirsiniz`), 6.2 (16 kelime sınırı), şişkinlik sözlüğü (`yüksek performanslı`, `kapsamlı`, `sağlam`, `sorunsuz bir şekilde` silindi). Kaynakta ölçüm yoktu, bu yüzden performans savı da silindi. Uydurulmadı.

---

## 2. Kurulum (prosedürel)

**Önce**

> Kuruluma başlamadan önce sisteminizde Go 1.21 veya üzeri bir sürümün kurulu olduğundan emin olunması gerekmektedir. Daha sonra aşağıdaki komutu çalıştırarak binary'yi indirebilir ve PATH'inize ekleyerek kullanıma hazır hale getirebilirsiniz.

**Sonra**

> Go sürümünüzü doğrulayın. sqlpipe en az Go 1.21 ister.
>
> 1. Kurulum betiğini çalıştırın: `curl -sSL https://get.sqlpipe.dev | sh`
> 2. Betik, çalıştırılabilir dosyayı `/usr/local/bin` dizinine koyar.
> 3. Kurulumu doğrulayın: `sqlpipe version`

Kurallar: 5.1 (bir cümle bir işlem), 5.2 (emir kipi), 1.8 (`emin olunması gerekmektedir` → `doğrulayın`), 3.5 (`çalıştırarak` ve `ekleyerek` ulaç zinciri bölündü), 10.1 (tek hitap kipi).

---

## 3. Hata mesajı

**Önce**

> Hata: Bir sorun oluştu. Lütfen bağlantı ayarlarınızı kontrol ettikten sonra tekrar deneyiniz. Sorunun devam etmesi durumunda sistem yöneticiniz ile iletişime geçmeniz gerekmektedir.

**Sonra**

> Hata: S3 yüklemesi reddedildi. `sqlpipe-prod` kullanıcısında `s3:PutObject` izni yok.
> İzni IAM politikasına ekleyin, sonra komutu yeniden çalıştırın.

Kurallar: hata mesajı kalıbı (ne oldu → neden → ne yapılacak), 10.1 (`deneyiniz` ile `geçmeniz` dönüşümü kalktı), şişkinlik (`Bir sorun oluştu` hiçbir olgu taşımaz).

---

## 4. Olay raporu

**Önce**

> Bazı kullanıcılarımızın hizmete erişiminde yaşanabilecek bir sorun tespit edilmiş olup, ekiplerimiz tarafından konu ile ilgili gerekli çalışmalar başlatılmıştır. Yaşanan mağduriyetten dolayı özür dileriz.

**Sonra**

> 14:02 ile 14:31 arasında isteklerin %12'si başarısız oldu. 14:00'teki dağıtım, önbellek ısıtma adımını kaldırdı. Değişikliği 14:27'de geri aldık. Dağıtım denetimine önbellek testi ekledik.

Kurallar: 3.8 (`başlatılmıştır` → `ekledik`), 3.4 (`tarafından` silindi), 3.3 (edilgen çatı etken oldu), şişkinlik (`ilgili`, `gerekli`). Sayılar kaynaktan gelir; kaynakta yoksa uydurulmaz.

---

## 5. Sürüm notu (kırıcı değişiklik)

**Önce**

> Bu sürümde API katmanında gerçekleştirilen iyileştirmeler kapsamında bazı endpoint'lerin davranışlarında değişiklikler yapılmış olup, kullanıcıların ilgili entegrasyonlarını gözden geçirmeleri tavsiye edilmektedir.

**Sonra**

> DİKKAT: `/v1/users` uç noktası artık `email` alanını döndürmez. `/v2/users` uç noktasına geçin. Eski uç nokta 1 Mart 2027'de kapanır.

Kurallar: 7.1 (risk düzeyi adlandırıldı), 7.2 ve 7.3 (önce emir, sonra risk), 1.4 (`gerçekleştirilen` silindi), 3.2 (`tavsiye edilmektedir` → emir kipi).

---

## 6. Commit mesajı ve PR açıklaması

**Önce**

> refactor: kod kalitesinin artırılması ve bazı iyileştirmelerin yapılması
>
> Bu PR kapsamında, mevcut yapıda bulunan bazı sorunların giderilmesi ve kod okunabilirliğinin artırılması amacıyla çeşitli düzenlemeler gerçekleştirilmiştir.

**Sonra**

> fix: oturum yenilemesindeki bellek sızıntısını gider
>
> `TokenRefresher`, her yenilemede yeni bir `Timer` üretti ve eskisini iptal etmedi. Bellek 24 saatte 40 MB büyüdü. Yenilemeden önce eski zamanlayıcıyı iptal ettim.

Kurallar: 1.8 (`artırılması`, `giderilmesi`, `yapılması` fiile döndü), 3.8 (`gerçekleştirilmiştir` → `ettim`), 6.1 (cümle başına bir yeni bilgi). Başlık neyin değiştiğini söyler.
