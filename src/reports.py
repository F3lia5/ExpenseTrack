from dataclasses import asdict
from storage import harcama_ekle, harcama_yukle

def kategoriye_gore_filtrele(kategori_adi):
    tum_harcamalar = harcama_yukle()
    sonuc = [harcama for harcama in tum_harcamalar if harcama['harcama_kategorisi'] == kategori_adi]
    return sonuc

print(kategoriye_gore_filtrele('EGITIM'))

def harcama_zamani(yil_ay):
    tum_harcamalar = harcama_yukle()
    sonuc = [zaman for zaman in tum_harcamalar if zaman['harcama_tarihi_dt'].startswith(yil_ay)]
    return sonuc

print(harcama_zamani('2026-08'))
