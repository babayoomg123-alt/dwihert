# ===================================================
# program kelulusan siswa
# ===================================================

while True:
    nilai_siswa = int(input("\nmasukkan nilai siswa: "))

    if nilai_siswa >= 75:
        print("tuntas")
        break
    else:
        ulang = input("nilai kurang. apakah ingin mengulang? (ya?/tidak): ")

        if ulang.lower() == "ya":
            continue
        else:
            print("tidak tuntas")
            break