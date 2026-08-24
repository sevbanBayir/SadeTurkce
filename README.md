# Sade Türkçe

**Yapay zekân LinkedIn gönderisi gibi Türkçe yazıyor. Bakım kılavuzu gibi yazsın.**

Türkçe teknik metni sade ve tek anlamlı yazmaya zorlayan bir agent skill'i. Kurallar, havacılığın 1983'ten beri kullandığı [ASD-STE100](https://www.asd-ste100.org/) kontrollü dilinin mantığından gelir. Ama çeviri değildir: Türkçe eklemeli ve sonuncul yüklemli bir dildir, bu yüzden kurallar yeniden türetilmiştir.

Bürokratik dil ve yapay zekâ şişkinliği yan etki olarak ölür.

---

## Önce / sonra

| Şişkin | Sade |
|---|---|
| Kullanıcının iptal akışında karşılaşabileceği uyarıların gösterilmesi işleminin, taahhüt durumunun kontrol edilmesi sonrasında gerçekleştirilmesi gerekmektedir. | İptal akışındaki uyarı kutularını, taahhüt denetiminden sonra gösterin. |
| Bir hata oluştu. Lütfen bağlantı ayarlarınızı kontrol ettikten sonra tekrar deneyiniz. | S3 yüklemesi reddedildi. `sqlpipe-prod` kullanıcısında `s3:PutObject` izni yok. İzni ekleyin, sonra komutu yeniden çalıştırın. |
| Bazı kullanıcılarımızın hizmete erişiminde yaşanabilecek bir sorun tespit edilmiş olup, ekiplerimiz tarafından çalışmalar başlatılmıştır. | 14:02 ile 14:31 arasında isteklerin %12'si başarısız oldu. 14:00'teki dağıtım, önbellek ısıtma adımını kaldırdı. |

Altı tam örnek: [`examples/once-sonra.md`](examples/once-sonra.md).

## Kurulum

**Claude Code eklentisi.** Bu depo aynı zamanda bir eklenti pazarıdır.

```bash
claude plugin marketplace add sevbanBayir/SadeTurkce && claude plugin install sade-turkce@sade-turkce
```

**Elle kopyalama.** Depoyu klonlayın, sonra iki klasörü kopyalayın.

```bash
cp -r skills/sade-turkce ~/.claude/skills/ && cp output-styles/sade-turkce.md ~/.claude/output-styles/
```

**Skill desteği yoksa.** [`prompts/system-prompt.md`](prompts/system-prompt.md) dosyasındaki bloğu sistem yönergene, `AGENTS.md`, `CLAUDE.md` ya da `.cursorrules` dosyana yapıştır. Dar bağlamlar için kısa sürümü de var.

### Skill ile output style farkı

| Parça | Ne zaman çalışır |
|---|---|
| [`skills/sade-turkce/`](skills/sade-turkce/SKILL.md) | Yazma işi uyunca, ya da `/sade-turkce` yazınca |
| [`output-styles/sade-turkce.md`](output-styles/sade-turkce.md) | Her yanıtta |

Output style'ı açmak için `~/.claude/settings.json` dosyasına şunu yaz:

```json
{ "outputStyle": "sade-turkce" }
```

## Kurallar

10 bölüm, ~50 numaralı kural. Ağır işi yapanlar:

| Kural | Neyi öldürür |
|---|---|
| Yönergede 12, açıklamada 16 kelime | Uzayıp giden cümle |
| Adlaştırma yasağı | "Doğrulama işleminin gerçekleştirilmesi" → "doğrulayın" |
| `-mektedir` yasağı | Bürokratik geniş zaman |
| `-meli` yasağı | Okurun isteğe bağlı sandığı zorunluluk |
| Tek hitap kipi | "Kurun / Kurunuz / Kurmalısınız / Kurulur" dönüşümü |
| Bir cümlede bir yan cümle | `-arak … -ıp … -dığında` zinciri |
| Tamlama en fazla üç kelime | "veritabanı bağlantı havuzu zaman aşımı ayarı değeri" |
| Koşul cümlenin başında | Okurun geç fark ettiği "… olması durumunda" |
| Bir kavram, bir kelime | ayar/yapılandırma/konfigürasyon kumarı |
| Kesme işareti okunuşa uyar | `APIyi`, `API'ı`, `SQL'yi` |
| Uzun çizgi yasağı | İngilizceden geçen ara söz çizgisi |

Tam katalog: [`skills/sade-turkce/SKILL.md`](skills/sade-turkce/SKILL.md). Denetim listesi: [`references/kontrol-listesi.md`](skills/sade-turkce/references/kontrol-listesi.md).

Evet, bu README kuralların yarısını çiğniyor. Tanıtım metni kapsam dışıdır, beceri bunu bilir ve dokümanlarda kalır.

## Sadece doküman değil

[`references/kullanim-alanlari.md`](skills/sade-turkce/references/kullanim-alanlari.md) şunlar için uyarlama taşır: hata mesajları, runbook, olay raporu, sürüm notu, commit ve PR, arayüz metni, ajan yönergesi, çeviriye hazırlık.

Gitmediği yer: edebî metin, tanıtım metni, marka dili. Kurallar ikna dilini tasarım gereği siler.

## Denetleyici

`sade_lint.py`, kuralların düzenli ifadeyle yakalanabilen 21 tanesini sayar.

```bash
python3 evals/sade_lint.py --tur prosedurel dosya.md
```

```bash
python3 evals/sade_lint.py --oz-test && python3 evals/test_sade_lint.py
```

Türkçeye özel iki ayrıntıyı doğru işler: `İ` ve `I` harflerinin küçültülmesi, ve ünsüz yumuşaması (`olanak` → `olanağı`).

Ölçüm durumu, bilinen tavan ve yanlış pozitifler: [`evals/README.md`](evals/README.md).

**Model karşılaştırması henüz yapılmadı.** `evals/senaryolar.json` sekiz Türkçe görev taşır ve karşılaştırma yöntemi yazılıdır. Depoda ölçülmemiş sayı yoktur.

## İngilizce sürümden farkları

Bu depo, [AminBlg/SimpleEnglish](https://github.com/AminBlg/SimpleEnglish) deposunun yapısını izler. İçerik çeviri değildir.

- **Kelime sınırları düşük: 20/25 yerine 12/16.** Türkçe eklemelidir. "yapılandırabilirsiniz" tek kelimedir, İngilizcesi dört kelimedir.
- **Bölüm 2 (tamlamalar) ve Bölüm 9 (TDK yazım) yeni.** İngilizcede karşılıkları yoktur.
- **Kural 10.1 (hitap kipi tutarlılığı) yeni.** Türkçe teknik yazının bir numaralı tutarsızlığıdır.
- **Yasak listesi başkadır.** İngilizcede `should`, `leverage`, `robust`. Türkçede adlaştırma, `-mektedir`, `tarafından`, ulaç zinciri.
- **Onaylı sözlük yoktur.** ASD sözlüğü teliflidir ve Türkçesi yoktur. Bu depo mekaniği kullanır: bir kavram, bir kelime.

## Lisans ve atıf

MIT. Yapı ve yaklaşım için [AminBlg/SimpleEnglish](https://github.com/AminBlg/SimpleEnglish) (MIT) kaynak alınmıştır.

Bu depo resmî değildir. Yazım konusunda tek yetkili kaynak TDK Yazım Kılavuzu'dur. ASD-STE100, ASD'nin tescilli markasıdır; bu depo ASD ile ilişkili değildir.
