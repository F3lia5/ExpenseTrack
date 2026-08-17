from dataclasses import asdict
import json
from models import Expense, ornek_deney
import os

veri = asdict(ornek_deney)
veri['harcama_tarihi_dt'] = veri['harcama_tarihi_dt'].isoformat()
veri['harcama_kategorisi'] = veri['harcama_kategorisi'].name

dosya_varmi = os.path.exists('harcama.json')

if dosya_varmi:
    with open('harcama.json', 'r') as f:
        data = json.load(f)
        print(data)
else:
    data = []

data.append(veri)
with open('harcama.json', 'w') as f:
    json.dump(data, f)
