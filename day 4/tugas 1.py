import tkinter as tk

def hitung():
    # Mengambil input, dikalikan, lalu update label
    total = float(ent_h.get()) * float(ent_k.get())
    lbl_res.config(text=f"Total: Rp {total:,.2f}")

root = tk.Tk()
root.title("Kasir")

# Elemen UI
tk.Label(root, text="Harga:").pack()
ent_h = tk.Entry(root); ent_h.pack()

tk.Label(root, text="Kuantitas:").pack()
ent_k = tk.Entry(root); ent_k.pack()

tk.Button(root, text="Hitung Total", command=hitung).pack()
lbl_res = tk.Label(root, text="Total: Rp 0.00")
lbl_res.pack()

root.mainloop()