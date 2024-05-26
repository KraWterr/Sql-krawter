# SQL Injection Tarama Aracı

Bu araç, belirli bir URL üzerinde SQL enjeksiyon açıklıklarını tespit etmek amacıyla geliştirilmiştir. Araç, girilen URL ve sayfadaki tüm bağlantılar için basit bir SQL enjeksiyon taraması gerçekleştirir.

## Özellikler

- Belirtilen URL'yi ve sayfadaki tüm bağlantıları tarar.
- SQL enjeksiyon açıklıklarını tespit etmek için hata tabanlı SQL enjeksiyon tekniğini kullanır.
- Basit ve kullanımı kolay komut satırı arayüzü.
- Birden fazla bağlantıyı eşzamanlı olarak taramak için çoklu iş parçacığı (multi-threading) kullanır.

## Kurulum ve Kullanım

### Gereksinimler

- Python 3
- `requests` kütüphanesi
- `BeautifulSoup` kütüphanesi

### Kurulum

Gerekli kütüphaneleri yüklemek için aşağıdaki komutları kullanabilirsiniz:

```bash
pip install requests beautifulsoup4
```

### Kullanım

Aracı kullanmak için aşağıdaki adımları izleyin:

1. Kodu indirin veya kopyalayın.
2. Terminal veya komut satırını açın.
3. Aşağıdaki komutu çalıştırarak aracı başlatın:

```bash
python sqli_scanner.py
```

4. Test etmek istediğiniz ana URL'yi girin.

```plaintext
Lütfen test edilecek ana URL'yi girin: http://example.com
```

## Yasal Uyarı

Bu araç sadece eğitim amaçlıdır ve izinsiz olarak kullanılması yasaktır. Kendi sistemleriniz veya izniniz olan sistemler dışında kullanmayın. Aksi takdirde yasal sonuçlarla karşılaşabilirsiniz.

## İletişim

Bu kod bir yazılımcı tarafından oluşturulmuştur. Daha fazla bilgi için [@weertyyyy](https://t.me/weertyyyy) ile iletişime geçebilirsiniz.

---

Bu açıklama, projenizi GitHub'da paylaşırken gerekli bilgileri sağlayacak ve kullanıcılara aracın nasıl kullanılacağı konusunda rehberlik edecektir.
