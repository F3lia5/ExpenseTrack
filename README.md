💰 ExpenseTrack (Kişisel Harcama Takipçisi)

    Python standart kütüphaneleri, OOP ilkeleri ve katmanlı mimari (Business Logic ile GUI ayrımı) kullanılarak geliştirilmiş, Tkinter tabanlı masaüstü harcama takip uygulaması.

📌 Proje Hakkında

ExpenseTrack, harcamalarınızı kategori bazlı takip etmenizi, harcama geçmişinizi dosya sisteminde güvenle saklamanızı ve harcama alışkanlıklarınıza dair özet raporlar almanızı sağlayan hafif ve harici bir bağımlılık gerektirmeyen masaüstü uygulamasıdır.
Öne Çıkan Özellikler & Konular

    Katmanlı Mimari: Arayüz (GUI) ile iş mantığının (Business Logic) tamamen ayrıştırılması.

    Sıfır Dış Bağımlılık (Çekirdek): Python'ın standart kütüphaneleri kullanılarak geliştirilmiştir (tkinter, dataclasses, enum, json, datetime, collections).

    Veri Güvenliği & Doğrulama: try/except blokları ile hatalı veri girişlerinin engellenmesi ve verilerin JSON formatında kalıcı tutulması.

    Birim Testleri: pytest ile test edilebilir arka plan mimarisi.

📁 Proje Dizin Yapısı

expensetrack/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── models.py       # Veri modelleri ve Enum tanımları
│   ├── storage.py      # JSON kaydetme ve okuma işlemleri
│   ├── reports.py      # Raporlama ve istatistik hesaplamaları
│   └── gui.py          # Tkinter kullanıcı arayüzü
├── tests/
│   └── test_models.py  # Birim testler
└── expensetrack.py      # Ana uygulama giriş noktası

---

## ⚙️ Kurulum ve Çalıştırma

### Gereksinimler

* Python 3.8+
* Tkinter (Arch Linux kullanıcıları için: `sudo pacman -S tk`)

### Çalıştırma

1. Repoyu klonlayın:

```bash
git clone [https://github.com/kullanici-adi/expensetrack.git](https://github.com/kullanici-adi/expensetrack.git)
cd expensetrack

```

2. Uygulamayı başlatın:

```bash
python expensetrack.py

```

3. Testleri çalıştırmak için (Opsiyonel):

```bash
pip install pytest
pytest

```

---

## 🎯 Geliştirme Yol Haritası & İlerleme (Progress)

Projenin modüler geliştirme sürecindeki mevcut durumu:

* [✅] **1. Hazırlık ve Ortam Kurulumu**
Sistem bağımlılıklarının kontrolü, proje dizin yapısının ve sanal ortamın oluşturulması.
* [ ] **2. Veri Modelleri (`src/models.py`)**
`Enum` ile kategori yapısı, `@dataclass` ile `Expense` sınıfı ve veri doğrulama kuralları.
* [ ] **3. Veri Saklama ve Dosya İşlemleri (`src/storage.py`)**
JSON formatında okuma/yazma, hata yönetimi ve veri dönüştürücüler.
* [ ] **4. Raporlama Mantığı (`src/reports.py`)**
Kategori filtreleme, toplam harcama ve `Counter` ile en çok harcanan kategori tespiti.
* [ ] **5. Kullanıcı Arayüzü (`src/gui.py`)**
Tkinter pencereleri, harcama ekleme formları, tablo (`Treeview`) ve özet alanı.
* [ ] **6. Ana Giriş Noktası (`expensetrack.py`)**
Arayüz döngüsünün (`mainloop()`) başlatılması ve uygulama entegrasyonu.
* [ ] **7. Test ve Kalite (`tests/test_models.py`)**
`pytest` ile birim (unit) testlerinin yazılması.

---

## 📄 Lisans

Bu proje MIT lisansı altında sunulmaktadır.
"""

filename = "README.md"
with open(filename, "w", encoding="utf-8") as f:
f.write(readme_content)

print(f"README file created successfully: {filename}")

```

```text?code_stdout&code_event_index=1
README file created successfully: README.md


```

Your README file is ready


GitHub'da yayınlanmaya uygun, iç ders/öğrenme notlarından arındırılmış ve geliştirme adımlarını `[ ]` şeklinde takip edebileceğin `README.md` dosyası oluşturuldu.

### `README.md` İçeriği:

```markdown
# 💰 ExpenseTrack (Kişisel Harcama Takipçisi)

> Python standart kütüphaneleri, OOP ilkeleri ve katmanlı mimari (Business Logic ile GUI ayrımı) kullanılarak geliştirilmiş, Tkinter tabanlı masaüstü harcama takip uygulaması.

---

## 📌 Proje Hakkında

**ExpenseTrack**, harcamalarınızı kategori bazlı takip etmenizi, harcama geçmişinizi dosya sisteminde güvenle saklamanızı ve harcama alışkanlıklarınıza dair özet raporlar almanızı sağlayan hafif ve harici bir bağımlılık gerektirmeyen masaüstü uygulamasıdır.

### Öne Çıkan Özellikler & Konular
- **Katmanlı Mimari:** Arayüz (GUI) ile iş mantığının (Business Logic) tamamen ayrıştırılması.
- **Sıfır Dış Bağımlılık (Çekirdek):** Python'ın standart kütüphaneleri kullanılarak geliştirilmiştir (`tkinter`, `dataclasses`, `enum`, `json`, `datetime`, `collections`).
- **Veri Güvenliği & Doğrulama:** `try/except` blokları ile hatalı veri girişlerinin engellenmesi ve verilerin JSON formatında kalıcı tutulması.
- **Birim Testleri:** `pytest` ile test edilebilir arka plan mimarisi.

---

## 📁 Proje Dizin Yapısı

```text
expensetrack/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── models.py       # Veri modelleri ve Enum tanımları
│   ├── storage.py      # JSON kaydetme ve okuma işlemleri
│   ├── reports.py      # Raporlama ve istatistik hesaplamaları
│   └── gui.py          # Tkinter kullanıcı arayüzü
├── tests/
│   └── test_models.py  # Birim testler
└── expensetrack.py      # Ana uygulama giriş noktası

```

---

## ⚙️ Kurulum ve Çalıştırma

### Gereksinimler

* Python 3.8+
* Tkinter (Arch Linux kullanıcıları için: `sudo pacman -S tk`)

### Çalıştırma

1. Repoyu klonlayın:

```bash
git clone [https://github.com/kullanici-adi/expensetrack.git](https://github.com/kullanici-adi/expensetrack.git)
cd expensetrack

```

2. Uygulamayı başlatın:

```bash
python expensetrack.py

```

3. Testleri çalıştırmak için (Opsiyonel):

```bash
pip install pytest
pytest

```

---

## 🎯 Geliştirme Yol Haritası & İlerleme (Progress)

Projenin modüler geliştirme sürecindeki mevcut durumu:

* [ ] **1. Hazırlık ve Ortam Kurulumu**
Sistem bağımlılıklarının kontrolü, proje dizin yapısının ve sanal ortamın oluşturulması.
* [ ] **2. Veri Modelleri (`src/models.py`)**
`Enum` ile kategori yapısı, `@dataclass` ile `Expense` sınıfı ve veri doğrulama kuralları.
* [ ] **3. Veri Saklama ve Dosya İşlemleri (`src/storage.py`)**
JSON formatında okuma/yazma, hata yönetimi ve veri dönüştürücüler.
* [ ] **4. Raporlama Mantığı (`src/reports.py`)**
Kategori filtreleme, toplam harcama ve `Counter` ile en çok harcanan kategori tespiti.
* [ ] **5. Kullanıcı Arayüzü (`src/gui.py`)**
Tkinter pencereleri, harcama ekleme formları, tablo (`Treeview`) ve özet alanı.
* [ ] **6. Ana Giriş Noktası (`expensetrack.py`)**
Arayüz döngüsünün (`mainloop()`) başlatılması ve uygulama entegrasyonu.
* [ ] **7. Test ve Kalite (`tests/test_models.py`)**
`pytest` ile birim (unit) testlerinin yazılması.

---

## 📄 Lisans

Bu proje MIT lisansı altında sunulmaktadır.

```

```
