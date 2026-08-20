#bu test modellerini yapay zeka yardimiyla yazdim hala ogrenmeye calisiyorum

"""
test_models.py

Neyi test ediyoruz?
Expense dataclass'ının doğru oluşturulduğunu ve tarih_str property'sinin
doğru string ürettiğini doğruluyoruz. Bu dosyada dış bir kaynağa (dosya,
internet) ihtiyaç yok - sadece nesne oluşturup değerlerini kontrol ediyoruz,
bu yüzden en basit test dosyamız bu.
"""
from datetime import datetime
from models import Expense, HarcamaKategorisi


def test_expense_olusturma():
    """
    MUTLU YOL testi: Normal, beklenen bir Expense nesnesi oluşturulduğunda
    her alanın doğru şekilde saklandığını doğrular.
    Bu, en temel test - "nesne dediğim gibi mi kuruluyor" sorusuna cevap verir.
    """
    tarih = datetime(2026, 8, 18, 12, 0, 0)
    harcama = Expense(
        harcama_tutari=50,
        harcama_kategorisi=HarcamaKategorisi.MARKET,
        notlar="haftalık alışveriş",
        harcama_tarihi_dt=tarih,
    )

    assert harcama.harcama_tutari == 50
    assert harcama.harcama_kategorisi == HarcamaKategorisi.MARKET
    assert harcama.notlar == "haftalık alışveriş"
    assert harcama.harcama_tarihi_dt == tarih


def test_tarih_str_property():
    """
    Bu, senin models.py'da yazdığın @property'nin gerçekten doğru
    çalıştığını kanıtlayan test. property'ler normal dataclass alanları
    gibi asdict() ile görünmüyordu (bunu storage.py'ı yazarken keşfetmiştin) -
    ama kendi başına çağrıldığında doğru string üretmeli, onu test ediyoruz.
    """
    tarih = datetime(2026, 8, 18, 12, 30, 0)
    harcama = Expense(
        harcama_tutari=10,
        harcama_kategorisi=HarcamaKategorisi.EGITIM,
        notlar="",
        harcama_tarihi_dt=tarih,
    )

    # isoformat() ne üretir biliyoruz: "2026-08-18T12:30:00"
    assert harcama.tarih_str == "2026-08-18T12:30:00"


def test_kategori_enum_degerleri():
    """
    EDGE CASE / SABİTLİK testi: Enum üyelerinin doğru sayısal değerlere
    sahip olduğunu doğrular. Bu önemli çünkü storage.py'da .value kullanmıyoruz
    ama ileride biri yanlışlıkla .value'ya güvenirse, bu test o hatayı hemen
    yakalar. Ayrıca Enum'un beklenmedik şekilde değişmediğini (birinin yanlışlıkla
    bir üyeyi silmediğini/değiştirmediğini) garanti eder.
    """
    assert HarcamaKategorisi.MARKET.value == 4
    assert HarcamaKategorisi.EGITIM.name == "EGITIM"
