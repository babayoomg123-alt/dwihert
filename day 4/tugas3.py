import tkinter as tk
from tkinter import messagebox

def simpan_data():
    # Logic to save data (e.g., to a file or database)
    nama = entry_nama.get()
    if nama:
        messagebox.showinfo("Sukses", f"Data {nama} berhasil disimpan!")
    else:
        messagebox.showwarning("Peringatan", "Nama Lengkap harus diisi!")

def hapus_data():
    # Clears all fields
    entry_nama.delete(0, tk.END)
    entry_tgl.delete(0, tk.END)
    entry_asal.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_ayah.delete(0, tk.END)
    entry_ibu.delete(0, tk.END)
    entry_telp.delete(0, tk.END)
    text_alamat.delete("1.0", tk.END)

root = tk.Tk()
root.title("Program Data Siswa")
root.geometry("400x600")
root.configure(bg="#f0f0f0")

# Header
header = tk.Label(root, text="DATA SISWA BARU", font=("Arial", 16, "bold"), bg="#ADD8E6", pady=10)
header.pack(fill=tk.X)

# Helper function for labels and entries
def create_field(parent, label_text):
    label = tk.Label(parent, text=label_text, bg="#f0f0f0", anchor="w")
    label.pack(fill=tk.X, padx=20, pady=(5, 0))
    entry = tk.Entry(parent)
    entry.pack(fill=tk.X, padx=20, pady=(0, 5))
    return entry

# Form Fields
entry_nama = create_field(root, "Nama Lengkap")
entry_tgl  = create_field(root, "Tanggal Lahir")
entry_asal = create_field(root, "Asal Sekolah")
entry_nisn = create_field(root, "NISN")
entry_ayah = create_field(root, "Nama Ayah")
entry_ibu  = create_field(root, "Nama Ibu")
entry_telp = create_field(root, "Nomor Telepon / HP")

# Address Field (Text box for multiline)
tk.Label(root, text="Alamat", bg="#f0f0f0", anchor="w").pack(fill=tk.X, padx=20)
text_alamat = tk.Text(root, height=4)
text_alamat.pack(fill=tk.X, padx=20, pady=(0, 10))

# Buttons
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

btn_hapus = tk.Button(btn_frame, text="Hapus", bg="#e67e22", fg="white", width=10, command=hapus_data)
btn_hapus.pack(side=tk.LEFT, padx=5)

btn_simpan = tk.Button(btn_frame, text="Simpan", bg="#e67e22", fg="white", width=10, command=simpan_data)
btn_simpan.pack(side=tk.LEFT, padx=5)

root.mainloop()