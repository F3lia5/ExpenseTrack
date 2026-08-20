import tkinter as tk
from tkinter import messagebox
from models import HarcamaKategorisi

def kategori_sec():
    secilen = kategori_var.get()
    if not secilen:
        messagebox.showwarning("Uyarı", "Lütfen bir kategori seçin!")
        return
    messagebox.showinfo(
        "İşlem Başarılı",
        f"Seçilen Kategori: {secilen}\nGirilen Tutar: {tutar_sayaci.get()} TL"
    )

def tutar_kontrol(event):
    try:
        value = float(entry.get())
        if value < 0:
            tutar_sayaci.set(0.00)
        elif value > 10000:
            tutar_sayaci.set(10000.00)
        else:
            tutar_sayaci.set(value)
    except ValueError:
        tutar_sayaci.set(0.00)

# --- RENK PALETİ (Modern Koyu Tema) ---
BG_MAIN = "#1E2024"       # En arka plan (Koyu gri/siyah)
BG_CARD = "#2B2D31"       # Kart/Kutu arka planı (Biraz daha açık gri)
FG_TEXT = "#F2F3F5"       # Metin rengi (Kırık beyaz - göz yormaz)
ACCENT_COLOR = "#1DB954"  # Vurgu rengi (Modern yeşil)

root = tk.Tk()
root.title("Modern Expense Tracker")
root.geometry("500x700")
root.configure(bg=BG_MAIN)

# --- BAŞLIK ---
baslik = tk.Label(
    root,
    text="Harcama Ekle",
    font=("Segoe UI", 20, "bold"),
    bg=BG_MAIN,
    fg=FG_TEXT
)
baslik.pack(pady=(30, 20))

kategori_var = tk.StringVar()

# --- KATEGORİLER ---
kategori_frame = tk.Frame(root, bg=BG_MAIN)
kategori_frame.pack(fill="x", padx=50)

kategori_label = tk.Label(
    kategori_frame, text="Kategori Seçiniz:", font=("Segoe UI", 11), bg=BG_MAIN, fg="#A0A5AD"
)
kategori_label.pack(anchor="w", pady=(0, 10))

for secilenkategori in HarcamaKategorisi:
    giris = tk.Radiobutton(
        kategori_frame,
        text=secilenkategori.name,
        variable=kategori_var,
        value=secilenkategori.name,
        bg=BG_MAIN,
        fg=FG_TEXT,
        selectcolor=BG_CARD, # Seçim yuvarlaginin içi
        activebackground=BG_MAIN,
        activeforeground=ACCENT_COLOR,
        highlightthickness=0,
        font=("Segoe UI", 12),
        cursor="hand2" # Üzerine gelince el işareti cikiyo
    )
    giris.pack(anchor="w", pady=2)

tutar_sayaci = tk.DoubleVar(value=0.00)

# --- TUTAR GİRİŞ ALANI ---
tutar_label = tk.Label(
    root, text="Tutar Belirleyiniz (TL):", font=("Segoe UI", 11), bg=BG_MAIN, fg="#A0A5AD"
)
tutar_label.pack(anchor="w", padx=50, pady=(20, 5))

frame = tk.Frame(
    root,
    padx=20,
    pady=15,
    bg=BG_CARD,
    bd=0,
    relief="flat",
)
frame.pack(pady=10)

scale = tk.Scale(
    frame,
    length=250,
    from_=0,
    to=10000,
    orient=tk.HORIZONTAL,
    resolution=0.01,
    variable=tutar_sayaci,
    showvalue=0,
    bg=BG_CARD,
    fg=FG_TEXT,
    troughcolor=BG_MAIN,
    activebackground=ACCENT_COLOR,
    highlightthickness=0,
    cursor="hand2"
)
scale.grid(row=0, column=0, padx=(0, 15))

entry = tk.Entry(
    frame,
    textvariable=tutar_sayaci,
    width=8,
    font=("Segoe UI", 14, "bold"),
    bg=BG_MAIN,
    fg=ACCENT_COLOR,
    insertbackground=FG_TEXT, # İmleç (yanıp sönen çizgi) rengi
    bd=0,
    justify="center",
    relief="flat"
)
entry.grid(row=0, column=1)
entry.bind("<Return>", tutar_kontrol)

# --- ONAY BUTONU ---
kategori_sec_button = tk.Button(
    root,
    text="Harcamayı Kaydet",
    command=kategori_sec,
    bg=ACCENT_COLOR,
    fg="white",
    font=("Segoe UI", 12, "bold"),
    bd=0,
    relief="flat",
    padx=30,
    pady=12,
    cursor="hand2",
    activebackground="#179643",
    activeforeground="white"
)
kategori_sec_button.pack(pady=(40, 10))

root.mainloop()
