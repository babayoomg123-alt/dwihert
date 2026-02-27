baris = int(input("masukkan jumlah baris: "))
for i in range(1, baris + 1):

    print(" " * (baris - i), end="")

    print("* " * i)