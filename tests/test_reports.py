# bu test modulunu yapay zeka ile yazdim hala ogrenme asamasindayim

"""
test_reports.py

Neyi test ediyoruz?
reports.py'daki 5 fonksiyonun (filtreleme, toplama, sayma) doğru
sonuç ürettiğini doğruluyoruz.

ÖNEMLİ - burada da gecici_dizin fixture'ını kullanıyoruz:
reports.py'daki her fonksiyon, arka planda storage.py'daki harcama_yukle()'yi
çağırıyor - yani o da 'harcama.json' dosyasına bağımlı. Bu yüzden test_storage.py'da
kullandığımız aynı fixture'ı burada da kullanacağız, gerçek dosyana dokunmadan
test verimizi hazırlayacağız.

STRATEJİ: Her testin başında, "önce birkaç örnek harcama ekleyelim, sonra
reports.py fonksiyonlarının bu örnek veri üzerinde doğru çalıştığını kontrol
edelim" şeklinde ilerleyeceğiz. Bu yüzden fixture'ımızı biraz genişletip,
hazır bir "örnek veri seti" de ekleyeceğiz - tekrar tekrar aynı harcamaları
elle yazmamak için (11. dersteki "kod tekrarını önleme" prensibi, testler
için de geçerli).
"""
import datetime as dt
import pytest
from storage import harcama_ekle
from models import HarcamaKategorisi
from reports import (
    kategoriye_gore_filtrele,
    harcama_zamani,
    toplam_harcama,
    kategoriye_gore_toplam,
    kategoriye_gore_toplam_tutar,
)


@pytest.fixture
def ornek_veri(tmp_path, monkeypatch):
    """
    Bu fixture, test_storage.py'daki gecici_dizin fixture'ının GENİŞLETİLMİŞ
    hali - hem izole bir klasöre geçiyor HEM DE önceden 3 örnek harcama
    ekliyor. Bu sayede her test fonksiyonunun içinde harcama_ekle()'yi
    tekrar tekrar çağırmamıza gerek kalmıyor, fixture bunu bizim için
    bir kere yapıyor.

    Eklenen 3 harcama:
    - 10 TL, EGITIM, Ağustos 2026
    - 20 TL, MARKET, Ağustos 2026
    - 15 TL, EGITIM, Temmuz 2026  <- farklı ay, filtrelemeyi test etmek için
    """
    monkeypatch.chdir(tmp_path)

    harcama_ekle({
        "harcama_tutari": 10,
        "harcama_kategorisi": HarcamaKategorisi.EGITIM,
        "notlar": "kitap",
        "harcama_tarihi_dt": dt.datetime(2026, 8, 5),
    })
    harcama_ekle({
        "harcama_tutari": 20,
        "harcama_kategorisi": HarcamaKategorisi.MARKET,
        "notlar": "",
        "harcama_tarihi_dt": dt.datetime(2026, 8, 10),
    })
    harcama_ekle({
        "harcama_tutari": 15,
        "harcama_kategorisi": HarcamaKategorisi.EGITIM,
        "notlar": "kurs",
        "harcama_tarihi_dt": dt.datetime(2026, 7, 20),
    })

    return tmp_path


def test_kategoriye_gore_filtrele(ornek_veri):
    """
    MUTLU YOL: EGITIM kategorisini filtrelediğimizde, sadece o kategoriye
    ait 2 harcamanın (10 TL ve 15 TL) döndüğünü, MARKET'in (20 TL) hiç
    listede olmadığını doğrular.
    """
    sonuc = kategoriye_gore_filtrele("EGITIM")

    assert len(sonuc) == 2
    tutarlar = [harcama["harcama_tutari"] for harcama in sonuc]
    assert 10 in tutarlar
    assert 15 in tutarlar
    assert 20 not in tutarlar   # MARKET'in listeye SIZMADIĞINI doğrulamak önemli


def test_kategoriye_gore_filtrele_olmayan_kategori(ornek_veri):
    """
    EDGE CASE: Hiç harcama yapılmamış bir kategori (SAGLIK) filtrelendiğinde,
    hata vermeden BOŞ bir liste dönmeli - bu, "hiç eşleşme yoksa ne olur"
    sorusuna cevap veren, gerçek kullanımda sık karşılaşılacak bir senaryo.
    """
    sonuc = kategoriye_gore_filtrele("SAGLIK")
    assert sonuc == []


def test_harcama_zamani(ornek_veri):
    """
    MUTLU YOL: Ağustos 2026'ya göre filtrelediğimizde, sadece o ayki
    2 harcamanın (10 TL ve 20 TL) döndüğünü, Temmuz'daki 15 TL'nin
    listede OLMADIĞINI doğrular. Bu, startswith() mantığının doğru
    çalıştığını kanıtlıyor.
    """
    sonuc = harcama_zamani("2026-08")

    assert len(sonuc) == 2
    tutarlar = [harcama["harcama_tutari"] for harcama in sonuc]
    assert 15 not in tutarlar   # Temmuz'daki harcama sızmamalı


def test_toplam_harcama(ornek_veri):
    """
    MUTLU YOL: Üç harcamanın (10 + 20 + 15) toplamının 45 çıktığını
    doğrular - en basit ama en kritik test, çünkü sum() burada yanlış
    key kullanırsa ya da yanlış listeyi toplarsa hemen fark edilir.
    """
    assert toplam_harcama() == 45


def test_kategoriye_gore_toplam_sayim(ornek_veri):
    """
    MUTLU YOL: Counter tabanlı fonksiyonun, EGITIM kategorisinde KAÇ TANE
    (tutar değil, adet) harcama olduğunu doğru saydığını kontrol eder.
    Örnek veride EGITIM'e ait 2 harcama var (10 TL ve 15 TL) - yani
    beklenen sayım 2, bu iki harcamanın TOPLAM TUTARI olan 25 değil.
    Bu test, "sayım" ile "toplam tutar" fonksiyonlarının birbirine
    KARIŞMADIĞINI kanıtlıyor.
    """
    assert kategoriye_gore_toplam("EGITIM") == 2


def test_kategoriye_gore_toplam_tutar(ornek_veri):
    """
    MUTLU YOL: EGITIM kategorisine toplam ne kadar harcandığını test eder.
    Örnek veride EGITIM'e ait 10 TL ve 15 TL var, toplamı 25 olmalı.
    Bir önceki testle (sayım=2) karıştırılmaması gereken, farklı bir
    fonksiyonun doğru çalıştığını kanıtlıyoruz.
    """
    assert kategoriye_gore_toplam_tutar("EGITIM") == 25


def test_kategoriye_gore_toplam_tutar_olmayan_kategori(ornek_veri):
    """
    EDGE CASE: Hiç harcama yapılmamış bir kategoride toplam tutar
    istendiğinde, hata vermeden 0 dönmeli. sum() boş bir listede
    çalıştığında otomatik 0 döner - bunu doğrulamak, ileride biri
    bu davranışı yanlışlıkla bozarsa hemen fark etmemizi sağlar.
    """
    assert kategoriye_gore_toplam_tutar("SAGLIK") == 0
