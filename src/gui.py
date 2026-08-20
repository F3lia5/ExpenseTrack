from this import s
import tkinter as tk
from tkinter import DoubleVar, messagebox
from tracemalloc import Frame
from models import HarcamaKategorisi

def kategori_sec():
    secilen = kategori_var.get()
    messagebox.showinfo("Kategori",
        f"Seçilen kategori: {secilen} \nSeçilen tutar: {scale.get()}TL"
    )

def tutar_kontrol(event):
    try:
        value = float(entry.get())
        if value < 0:
            tutar_sayaci.set(0.00)
        elif value > 10000:
            tutar_sayaci.set(10000.00)
        else:
            scale.set(value)

    except ValueError:
        tutar_sayaci.set(0.00)

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("700x1000")

bg_color = "#2c3e50"
root.configure(bg=bg_color)

kategori_var = tk.StringVar()

for secilenkategori in HarcamaKategorisi:
    giris = tk.Radiobutton(
        root,
        text=secilenkategori.name,
        variable=kategori_var,
        value=secilenkategori.name,
        bg=bg_color,
        activebackground=bg_color,
        font=("Helvetica", 12)
    )
    giris.pack(pady=5)

tutar_sayaci = tk.DoubleVar(value=0.00)

frame = tk.Frame(
    root,
    padx=15,
    pady=15,
    bg="#e8f0fe",
    bd=2,
    relief="solid",
)
frame.pack(pady=10)

scale = tk.Scale(
    frame,
    length=300,
    from_=0,
    to=10000,
    orient=tk.HORIZONTAL,
    resolution=0.01,
    variable=tutar_sayaci,
    showvalue=0,
    bg="#e8f0fe",
    highlightthickness=0
)
scale.grid(row=0, column=0, padx=10)

entry = tk.Entry(
    frame,
    textvariable=tutar_sayaci,
    width=10,
    font=("Helvetica", 12),
    bg="#ffffff"
)
entry.grid(row=0, column=1, padx=10)

entry.bind("<Return>", tutar_kontrol)

kategori_sec_button = tk.Button(
    root,
    text="Kategori Seç",
    command=kategori_sec,
    bg="#4CAF50",
    fg="white",
    font=("Helvetica", 10, "bold")
)
kategori_sec_button.pack(pady=10)

root.mainloop()
