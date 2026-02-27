import tkinter as tk
from tkinter import ttk

def hitung():
    # Logika sederhana: Biaya = (Keluar - Masuk) * 2000
    try:
        biaya = (int(e_keluar.get()) - int(e_masuk.get())) * 2000
        lbl_biaya.config(text=f"Rp. {max(0, biaya)}")
        # Tambah ke tabel (Treeview)
        tabel.insert("", "end", values=(e_plat.get(), e_masuk.get(), e_keluar.get(), biaya))
    except: pass

root = tk.Tk()
root.title("Aplikasi Parkir Kelompok 6")

# Panel Input (Kiri)
tk.Label(root, text="No Plat Polisi").grid(row=0, column=0)
e_plat = tk.Entry(root); e_plat.grid(row=0, column=1)

tk.Label(root, text="Waktu Masuk").grid(row=1, column=0)
e_masuk = tk.Entry(root); e_masuk.grid(row=1, column=1)

tk.Label(root, text="Waktu Keluar").grid(row=2, column=0)
e_keluar = tk.Entry(root); e_keluar.grid(row=2, column=1)

tk.Button(root, text="Hitung Biaya", command=hitung).grid(row=3, column=0, columnspan=2)

# Panel Biaya (Kanan)
tk.Label(root, text="Biaya Per Jam", fg="red").grid(row=0, column=2)
lbl_biaya = tk.Label(root, text="Rp. 0", font=("Arial", 20), fg="red")
lbl_biaya.grid(row=1, column=2, rowspan=2)

# Tabel (Bawah)
cols = ("No Plat", "Masuk", "Keluar", "Biaya")
tabel = ttk.Treeview(root, columns=cols, show="headings", height=5)
for col in cols: tabel.heading(col, text=col)
tabel.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()