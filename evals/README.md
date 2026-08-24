# Ölçüm

## `sade_lint.py`

Sade Türkçe kurallarının düzenli ifadeyle yakalanabilen bölümünü sayar.

```bash
python3 evals/sade_lint.py --tur prosedurel dosya.md
cat metin.md | python3 evals/sade_lint.py --tur aciklayici -
python3 evals/sade_lint.py --oz-test
```

`--tur` iki değer alır: `prosedurel` (12 kelime sınırı) ve `aciklayici` (16 kelime sınırı).

Çıktı JSON'dur. `ihlal_100_kelime` alanı, iki metni karşılaştırmak için kullanılır.

### Saydığı 21 kural

| Anahtar | Kural | Yakalar |
|---|---|---|
| `cumle_uzun` | 4.1, 6.2 | Sınırı aşan cümle |
| `burokratik_kip` | 3.2 | `-mektedir`, `-maktadır` |
| `yasak_kip` | 3.1 | `-meli`, `-malı` |
| `mistir_kalibi` | 3.8 | `-mıştır`, `-miştir` |
| `edilgen_ozne` | 3.4 | `tarafından` |
| `yardimci_fiil` | 1.4 | `gerçekleştir-`, `sağlan-`, `bulunmakta-` |
| `adlastirma` | 1.8 | `-mesi/-ması` + `gerek/sağlan/yapıl` |
| `bir_sekilde` | Şişkinlik | `bir şekilde`, `bir biçimde` |
| `ulac_zinciri` | 3.5 | Bir cümlede birden çok `-arak/-erek` |
| `noktali_virgul` | 8.1 | `;` |
| `uzun_cizgi` | 8.7 | `—`, `–` |
| `kisaltma_dolgu` | GR | `vb.`, `vs.`, `örn.` |
| `ve_veya` | Şişkinlik | `ve/veya` |
| `dolgu` | Şişkinlik | 25 kalıp: `oldukça`, `kritik önem`, `bu bağlamda` … |
| `olanak_kalibi` | 1.4 | `olanak tanır`, `imkân sağlar` |
| `agir_kosul` | 4.3 | `durumunda`, `hâlinde`, `takdirde` |
| `ingilizce_fiil` | 1.7 | `deploy et-`, `handle et-`, `implemente et-` |
| `sondaki_kosul` | 4.3 | Cümle sonunda kalan koşul |
| `es_anlamli_rotasyon` | 1.1, 10.2 | Beş kavram kümesinde terim dönüşümü |
| `hitap_rotasyon` | 10.1 | Beş hitap sınıfından birden çoğu |
| `kesme_hatasi` | 9.4 | `APIyi`, `API'ı`, `SQL'yi` |

### Bilinen tavan

Bu bir düzenli ifade taramasıdır, biçim bilgisi çözümleyicisi değildir. Şunları bilerek kabul eder:

- **Eksik sayar.** Edilgen çatıyı `tarafından` olmadan yakalayamaz. Zincirleme isim tamlamasını saymaz. Bağlaç olan `de/da` ile hâl eki olan `-de/-da` ayrımını yapmaz: bu ayrım sözdizimi ister.
- **İki kez sayar.** `unutulmamalıdır` hem `yasak_kip` hem `dolgu` sayılır. Örtüşme bilinçlidir; sayı iki metin arasında karşılaştırılır, mutlak bir puan değildir.
- **Yanlış pozitif üretir.** `hitap_rotasyon` en gürültülü denetimdir: cümle sonundaki iyelik eki (`ayarlarınız.`) nazik emir sanılır. `kisa-emir` sınıfı, cümle sonundaki tamlayan ekini (`değişimin.`) emir sanabilir.
- Cümle sınırını nokta, ünlem, soru işareti, iki nokta ve paragraf sonu belirler. Kısaltmadan sonraki nokta (`Dr.`) yanlış bölme yapar.

Hiçbir araç dil uygunluğunu garanti edemez. Son onay yazarındır.

## `ornek_olc.py`

`examples/once-sonra.md` dosyasındaki önce/sonra çiftlerini ölçer.

```bash
python3 evals/ornek_olc.py
```

| Örnek | Önce (ihlal/100 kelime) | Sonra | En uzun cümle |
|---|---|---|---|
| README girişi | 25.00 | 0.00 | 18 → 10 |
| Kurulum | 17.24 | 0.00 | 15 → 7 |
| Hata mesajı | 13.64 | 0.00 | 10 → 8 |
| Olay raporu | 13.04 | 0.00 | 18 → 8 |
| Sürüm notu | 15.00 | 0.00 | 20 → 7 |
| Commit ve PR | 12.00 | 0.00 | 17 → 12 |
| **Toplam** | **16.77** | **0.00** | 26 ihlal → 0 ihlal |

**Bu sayı ne anlatır, ne anlatmaz.** Ölçüm, elle yazılmış örnek metinleri ölçer. Örnekler zaten kurallara uyacak biçimde yazıldı, bu yüzden sıfır sonucu beklenen sonuçtur. Sayı, kuralların ölçülebilir olduğunu ve denetleyicinin çalıştığını gösterir. **Modelin davranışı hakkında hiçbir şey söylemez.**

## Model karşılaştırması

Henüz yapılmadı. `senaryolar.json` dosyası sekiz Türkçe yazma görevi içerir. Karşılaştırma için her senaryoyu iki kez çalıştır:

1. **Temel:** yalın istem, beceri yüklü değil.
2. **Beceri:** aynı istem, `skills/sade-turkce/SKILL.md` bağlamda.

Her iki çıktıyı `sade_lint.py` ile senaryonun `tur` alanına göre ölç. `ihlal_100_kelime` değerlerini karşılaştır.

Sonuçları buraya eklerken şunları yaz: model kimliği, tarih, senaryo başına ham çıktı, sürüm etiketi. Ölçüm yapmadan sayı yazma.

## Testler

```bash
python3 evals/test_sade_lint.py
```

38 kural bazlı test. Her kuralın hem yakalayan hem yakalamayan örneği vardır.
