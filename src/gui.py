import tkinter as tk
from tkinter import messagebox
from models import HarcamaKategorisi

def kategori_sec():
    secilen = kategori_var.get()
    messagebox.showinfo("Kategori", f"Seçilen kategori: {secilen}")


root = tk.Tk()
root.title("Expense Tracker")
root.geometry("300x600")

kategori_var = tk.StringVar()

for secilenkategori in HarcamaKategorisi:
    print(secilenkategori.name)
    giris = tk.Radiobutton(root, text=secilenkategori.name, variable=kategori_var, value=secilenkategori.name)
    giris.pack()



kategori_sec_button = tk.Button(root, text="Kategori Seç", command=kategori_sec)
kategori_sec_button.pack()

root.mainloop()
