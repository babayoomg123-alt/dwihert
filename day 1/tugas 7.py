# program menghitung gaji bersih

print("=== program perhitungan gaji ===")

nama = input("masukkan nama: ")
gaji_pokok = float(input("masukkan gaji pokok: "))

tunjangan = 0.20 * gaji_pokok
pajak = 0.15 * (gaji_pokok + tunjangan)
gaji_bersih = gaji_pokok + tunjangan - pajak

print("\n=== Hasil Perhitungan ===")
print("Nama:", nama)
print("Gaji Pokok:", gaji_pokok)
print("Gaji Bersih:", gaji_bersih)