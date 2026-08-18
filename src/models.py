from datetime import datetime
from enum import Enum
from dataclasses import asdict, dataclass

class HarcamaKategorisi(Enum):
    YIYECEK = 1
    ULASIM = 2
    EGLENCE = 3
    MARKET = 4
    EV = 5
    ALISVERIS = 6
    SAGLIK = 7
    EGITIM = 8
    DIGER = 9

@dataclass
class Expense():
    harcama_tutari: float | int
    harcama_kategorisi: HarcamaKategorisi
    notlar: str
    harcama_tarihi_dt: datetime
    @property
    def tarih_str(self) -> str:
        #ilk defa datetime'i boyle deniyom ins tekte calisir
        return self.harcama_tarihi_dt.isoformat()

#try koncak bunlara hata ayiklamak icin (sadece elzem olanlar; eger harcama tutarina veya kategoriye secenekli buton koyabilirsem gerek yok)

ornek_deney = Expense(harcama_tutari=10, harcama_kategorisi=HarcamaKategorisi.SAGLIK, notlar="", harcama_tarihi_dt=datetime.now())
