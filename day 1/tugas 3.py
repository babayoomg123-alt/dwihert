2# program menghitung nilai ganjil dan genap

angka = int(input("masukkan sebuah angka: "))

if (angka % 2) == 0:
    print(f"{angka} adalah bilangan genap")
else:
    print(f"{angka} adalah bilangan ganjil")