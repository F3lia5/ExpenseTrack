import json
from models import Expense, ornek_deney
import os

def harcama_yukle():
    if os.path.exists('harcama.json'):
        with open('harcama.json', 'r') as f:
            data = json.load(f)
            return data
    return []

def harcama_ekle(veri):
    veri['harcama_tarihi_dt'] = veri['harcama_tarihi_dt'].isoformat()
    veri['harcama_kategorisi'] = veri['harcama_kategorisi'].name

    data = harcama_yukle()

    data.append(veri)
    with open('harcama.json', 'w') as f:
        json.dump(data, f)
