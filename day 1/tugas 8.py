# program kategori umur 

print("=== program kategori umur ===")

umur = int(input("masukkan umur: "))

if umur <= 10:
    print("kategori: anak-anak")
elif umur <= 18:
    print("kategori: remaja")
elif umur <= 35:
    print("kategori: dewasa")
elif umur <= 65:
    print("kategori: parubaya")
else:
    print("kategori: tua")