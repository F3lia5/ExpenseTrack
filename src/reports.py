from dataclasses import asdict
from storage import harcama_ekle, harcama_yukle
from collections import Counter

def kategoriye_gore_filtrele(kategori_adi):
    tum_harcamalar = harcama_yukle()
    sonuc = [harcama for harcama in tum_harcamalar if harcama['harcama_kategorisi'] == kategori_adi]
    return sonuc

def harcama_zamani(yil_ay):
    tum_harcamalar = harcama_yukle()
    sonuc = [zaman for zaman in tum_harcamalar if zaman['harcama_tarihi_dt'].startswith(yil_ay)]
    return sonuc

def toplam_harcama():
    tum_harcamalar = harcama_yukle()
    toplam = sum([harcama['harcama_tutari'] for harcama in tum_harcamalar])
    return toplam

def kategoriye_gore_toplam(kategori_adi):
    tum_harcamalar = harcama_yukle()
    kategori_listesi = [harcama['harcama_kategorisi'] for harcama in tum_harcamalar]
    sayac = Counter(kategori_listesi)
    return sayac[kategori_adi]

def kategoriye_gore_toplam_tutar(kategori_adi):
    toplam = sum([harcama['harcama_tutari'] for harcama in kategoriye_gore_filtrele(kategori_adi)])
    return toplam
