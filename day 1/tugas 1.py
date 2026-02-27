# program menghitung keliling dan luas persegi, persegi panjang, dan trapesium

# persegi
sisi_persegi = 5
keliling_persegi = 4 * sisi_persegi
luas_persegi = sisi_persegi * sisi_persegi * sisi_persegi
 
# persegi panjang 
panjang_persegipanjang = 10
lebar_persegipanjang = 5
keliling_persegipanjang = 2 * (panjang_persegipanjang + lebar_persegipanjang)
luas_persegipanjang = panjang_persegipanjang * lebar_persegipanjang

#trapesium (asumsi trapesium sama kaki)
sisi_atas_trapesium = 4
sisi_bawah_trapesium = 8
tinggi_trapesium = 3
sisi_miring_trapesium = 3.6 # Nilai ini perlu dihitung atau diinput
keliling_trapesium = sisi_atas_trapesium + sisi_bawah_trapesium + 2 * sisi_miring_trapesium
luas_trapesium = 0.5 * (sisi_atas_trapesium + sisi_bawah_trapesium) * tinggi_trapesium

print(f"keliling persegi: {keliling_persegi}, luas persegi: {luas_persegi}")
print(f"keliling persegi panjang: {keliling_persegipanjang}, luas persegi panjang: {luas_persegipanjang}")
print(f"keliling trapesium: {keliling_trapesium}, luas trapesium: {luas_trapesium}")