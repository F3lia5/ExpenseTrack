#Bu test modellerini yapay zeka yardimi ile hazirladim hala ogrenmeye calisiyorum

#
#test_storage.py
#
#Neyi test ediyoruz?
#harcama_ekle() ve harcama_yukle()'nin, gerçek dosya sistemiyle doğru
#etkileşime girdiğini doğruluyoruz.

#ÖNEMLİ - neden monkeypatch.chdir kullanıyoruz:
#storage.py'daki fonksiyonlar hep sabit 'harcama.json' ismini kullanıyor
#(dinamik bir yol parametresi almıyor). Eğer testlerimizi olduğu gibi
#çalıştırsaydık, GERÇEK harcama.json dosyanı ezip bozardık - test verisi
#ile senin gerçek verin karışırdı.

#Çözüm: pytest'in tmp_path fixture'ı, her test için otomatik BOŞ ve
#GEÇİCİ bir klasör oluşturur (test bitince silinir). monkeypatch.chdir()
#ile "şu an neredeyiz" bilgisini geçici olarak o boş klasöre taşıyoruz.
#Böylece storage.py 'harcama.json' dediğinde, aslında bu geçici klasördeki
#bir dosyaya yazıyor/okuyor oluyor - senin gerçek dosyana hiç dokunmuyor.
import json
import pytest
from storage import harcama_ekle, harcama_yukle


@pytest.fixture
def gecici_dizin(tmp_path, monkeypatch):

    #Bu bir FIXTURE - testlerin ihtiyaç duyduğu ortak bir "hazırlık" işlemi.
    #Parametre olarak bir testin fonksiyon adına 'gecici_dizin' yazman
    #yeterli, pytest bunu otomatik çalıştırıp sonucunu sana verir.
    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_harcama_yukle_dosya_yokken(gecici_dizin):

    #EDGE CASE: Hiç harcama.json dosyası yokken (uygulamanın ilk çalıştırılışı)
    #ne olacağını test ediyoruz. Bu, senin storage.py'da bilerek eklediğin
    #"dosya yoksa boş liste döndür" davranışını doğrular - bu davranış
    #olmasaydı program ilk açılışta çökerdi.
    sonuc = harcama_yukle()
    assert sonuc == []


def test_harcama_ekle_ve_yukle(gecici_dizin):
    #MUTLU YOL testi: Bir harcama eklendiğinde, gerçekten dosyaya yazıldığını
    #ve tekrar okunduğunda doğru geldiğini doğrular. Bu, "round-trip" (gidiş-dönüş)
    #testi olarak bilinir - veri kaydedilip geri okunduğunda kaybolmuyor mu diye bakar.
    yeni_harcama = {
        "harcama_tutari": 25,
        "harcama_kategorisi": "MARKET",
        "notlar": "test harcaması",
        # NOT: harcama_ekle() içeride .isoformat() çağırıyor, bu yüzden
        # burada gerçek bir datetime nesnesi vermemiz gerekiyor, string değil.
        "harcama_tarihi_dt": __import__("datetime").datetime(2026, 8, 18),
    }

    harcama_ekle(yeni_harcama)
    tum_harcamalar = harcama_yukle()

    assert len(tum_harcamalar) == 1
    assert tum_harcamalar[0]["harcama_tutari"] == 25
    assert tum_harcamalar[0]["harcama_kategorisi"] == "MARKET"
    # harcama_ekle içeride datetime'ı stringe çevirdiği için, geri okuduğumuzda
    # da string bekliyoruz - Enum/datetime nesnesi değil.
    assert tum_harcamalar[0]["harcama_tarihi_dt"] == "2026-08-18T00:00:00"


def test_harcama_ekle_birden_fazla(gecici_dizin):
    #Bu test, senin storage.py'da EN ÇOK zorlandığın kısmı doğruluyor:
    #"oku -> listeye ekle -> yeniden yaz" mantığının, ikinci bir harcama
    #eklendğinde ilkini SİLMEDİĞİNİ kanıtlamak. Hatırlarsan başta "a" modu
    #ile denemiştin ve dosya bozulmuştu - bu test tam olarak o hatanın
    #bir daha geri gelmediğini garanti ediyor.
    import datetime as dt

    harcama_ekle({
        "harcama_tutari": 10,
        "harcama_kategorisi": "EGITIM",
        "notlar": "",
        "harcama_tarihi_dt": dt.datetime(2026, 8, 1),
    })
    harcama_ekle({
        "harcama_tutari": 20,
        "harcama_kategorisi": "ULASIM",
        "notlar": "",
        "harcama_tarihi_dt": dt.datetime(2026, 8, 2),
    })

    tum_harcamalar = harcama_yukle()

    assert len(tum_harcamalar) == 2
    assert tum_harcamalar[0]["harcama_kategorisi"] == "EGITIM"
    assert tum_harcamalar[1]["harcama_kategorisi"] == "ULASIM"


def test_dosya_gecerli_json_uretiyor(gecici_dizin):
    #Bu test biraz farklı bir şeye bakıyor: storage.py'ın ÜRETTİĞİ dosyanın
    #standart, tek-parça bir JSON olduğunu (senin başta "a" modunda yaşadığın
    #birden fazla obje yan yana, bozuk JSON" sorununun yaşanmadığını) doğrudan
    #dosyayı okuyarak kanıtlıyor - harcama_yukle() üzerinden değil, dosyanın
    #kendisini json.load ile açarak.
    import datetime as dt

    harcama_ekle({
        "harcama_tutari": 5,
        "harcama_kategorisi": "DIGER",
        "notlar": "",
        "harcama_tarihi_dt": dt.datetime(2026, 8, 18),
    })

    with open("harcama.json", "r") as f:
        icerik = json.load(f)   # bozuk JSON olsaydı burada hata alırdık

    assert isinstance(icerik, list)
    assert len(icerik) == 1
