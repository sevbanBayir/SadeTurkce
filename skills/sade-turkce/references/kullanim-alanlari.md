# Kullanım alanları

Aynı kurallar, farklı hedefler. Her bölüm, `SKILL.md` kurallarının o metin türüne uyarlanmış hâlidir.

## Hata mesajları

Kalıp: **ne oldu (görülen geçmiş) → neden (biliniyorsa) → ne yapılacak (emir kipi)**.

Yasak: "Bir hata oluştu", "Bir şeyler ters gitti", "Üzgünüz", "Lütfen tekrar deneyin" (tek başına), ünlem, özür.

**Önce:** Bir hata oluştu. Lütfen bilgilerinizin doğru olduğundan emin olun ve tekrar deneyin.
**Sonra:** Veritabanına bağlanılamadı: `app` kullanıcısının parolası yanlış. `DB_PASSWORD` değerini düzeltin, sonra yeniden bağlanın.

Kullanıcının düzeltemeyeceği bir hatada ne yapacağını söyle: "Bu hata sunucu kaynaklıdır. 5 dakika sonra yeniden deneyin."

## Runbook ve prosedür

Sade Türkçe'nin ana alanı. Her adım emir kipindedir. Koşul adımın başındadır. Uyarı, adımdan **önce** gelir.

- Bir adım, bir işlem (5.1).
- Adımın sonucu adımın içindedir: "Servisi başlatın. Servis 10 saniyede hazır olur."
- Not, adımın çalışması için gerekli bilgi içermez (5.5).
- Geri alma adımı her yıkıcı adımın yanındadır.

## Olay raporu

Yalnızca görülen geçmiş. Sayı ver: saat, oran, süre, etkilenen kullanıcı sayısı.

**Önce:** Bazı kullanıcılarımızın hizmete erişiminde yaşanabilecek bir sorun tespit edilmiş olup, yaşanan mağduriyetten dolayı özür dileriz.
**Sonra:** 14:02 ile 14:31 arasında isteklerin %12'si başarısız oldu. 14:00'teki dağıtım, önbellek ısıtma adımını kaldırdı. Değişikliği 14:27'de geri aldık.

Bölümler: **Ne oldu. Ne zaman. Kaç kullanıcı etkilendi. Neden oldu. Ne yaptık. Tekrarını nasıl engelleyeceğiz.**

## Sürüm notları

Her madde bir değişikliktir. Kırıcı değişiklik uyarı kalıbını izler: önce emir, sonra risk (7.2, 7.3).

**Önce:** Bu sürümde API katmanında yapılan iyileştirmeler kapsamında bazı endpoint'lerin davranışında değişiklikler yapılmıştır.
**Sonra:** DİKKAT: `/v1/users` uç noktası artık `email` alanını döndürmez. `/v2/users` uç noktasına geçin.

## Commit mesajı ve PR açıklaması

- Başlık: emir kipi, en fazla 12 kelime, nokta yok. "Oturum yenilemesindeki bellek sızıntısını düzelt"
- Gövde: açıklayıcı metin. Ne değişti, neden değişti. En fazla 16 kelimelik cümleler.
- "Refactor yapıldı", "iyileştirmeler yapıldı" gibi içi boş başlık yazma. Neyin değiştiğini yaz.

## Arayüz metni

- Düğme adı fiildir ve en fazla üç kelimedir: "Kaydet", "Aboneliği iptal et".
- Boş durum metni ne yapılacağını söyler: "Henüz aracınız yok. İlk aracınızı ekleyin."
- Onay metni sonucu söyler: "Bu aracı silerseniz geçmiş bakım kayıtları da silinir."
- "Lütfen" yalnızca kullanıcıdan gerçekten bir iyilik istendiğinde kullanılır. Yönergede kullanılmaz.

## Ajan yönergeleri (prompt, AGENTS.md, CLAUDE.md)

Sistem yönergesi, soru soramayan bir okur için yazılmış prosedürdür. Bu yüzden kurallar burada en sıkı hâliyle geçerlidir.

- Bir cümle, bir yönerge.
- "-meli" yok. Zorunluluksa emir kipi, seçenekse "-ebilirsiniz".
- Koşul başta: "Test başarısız olursa, günlüğü oku."
- Her kavram için tek kelime. Model, eş anlamlıyı ayrı kavram sanır.

## Çeviriye hazırlık

Sade Türkçe, makine çevirisinin ve insan çevirmenin işini kolaylaştırır. Tek anlamlı kelime, kısa cümle ve eksiksiz dil bilgisi, belirsizliğin çoğunu kaldırır. Uzun tamlama ve ulaç zinciri, çeviride en çok hata üreten iki yapıdır (2.1, 3.5).
