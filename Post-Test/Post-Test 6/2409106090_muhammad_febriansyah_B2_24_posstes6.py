import os

listuser = {}
jenisvoucher = ["160"]
hargavoucher = ["20000"]
listvoucher = {
    "160": "20000"
}
kesempatan = 3
isLogin = False

while True:
    os.system('cls || clear')
    print("="*40)
    print("Selamat Datang di Program CRUD".center(40))
    print("="*40)
    print("[1] Login")
    print("[2] Registrasi")
    print("[3] Keluar Program")
    pilihan_awal = input("\nMasukkan pilihan: ")

    if pilihan_awal == "1":
        while kesempatan > 0:
            os.system('cls || clear')
            print("="*40)
            print("Login Form".center(40))
            print("="*40)
            username = input("Masukkan nama akun\t: ")
            password = input("Masukkan password\t: ")

            if (username.lower() == "febri" and password == "90") or \
             username in listuser and listuser[username] == password:
    
                isLogin = True
                print("\nBerhasil login!")
                input("\nKlik enter untuk melanjutkan...")
                break

            kesempatan -= 1
            print("\nUsername atau password salah!")
            print(f"\nKesempatan login tersisa {kesempatan} kali lagi!")
            input("\nKlik enter untuk melanjutkan...")

        if isLogin:
            while isLogin:
                os.system('cls || clear')
                print("="*40)
                print("Program CRUD Pembelian Voucher Game".center(40))
                print("="*40)
                if username == "febri":
                    print("[1] Tambah Voucher Game")
                    print("[2] Hapus Voucher Game")
                    print("[3] Update Voucher Game")
                print("[4] List Voucher Game")
                print("[5] Ganti Akun")
                pilihan = input("\nMasukkan pilihan: ")

                if pilihan == "1" and username =="febri":
                    os.system('cls || clear')
                    print("="*40)
                    print("Tambah Voucher Game".center(40))
                    print("="*40)
                    new_voucher = input("Masukkan Nominal Diamond: ")
                    new_price = input("Masukkan harga Diamond: ")
                    listvoucher[new_voucher] = new_price
                    print(f"Voucher {new_voucher} berhasil ditambahkan!")
                    input("\nKlik enter untuk melanjutkan...")

                elif pilihan == "2" and username =="febri":
                    os.system('cls || clear')
                    print("="*40)
                    print("Hapus Voucher Game".center(40))
                    print("="*40)

                    if listvoucher:
                        for key, value in listvoucher.items():
                            print(f"{key} Diamond - Rp. {value}")

                        delete_voucher = input("\nMasukkan Nominal voucher Diamond yang ingin dihapus: ")

                        if delete_voucher in listvoucher:
                            del listvoucher[delete_voucher]
                            print(f"Voucher '{delete_voucher}' berhasil dihapus!")
                        else:
                            print(f"Voucher '{delete_voucher}' tidak ditemukan!")
                    else:
                        print("Tidak ada voucher yang tersedia untuk dihapus.")

                    input("\nKlik enter untuk melanjutkan...")

                elif pilihan == "3" and username =="febri":
                    os.system('cls || clear')
                    print("="*40)
                    print("Update Voucher Game".center(40))
                    print("="*40)

                    if listvoucher:
                        for key, value in listvoucher.items():
                            print(f"{key} Diamond - Rp. {value}")

                    voucher_to_update = input("Masukkan Nominal voucher Diamond yang ingin di-update: ")

                    if voucher_to_update in listvoucher:
                        new_price = input("Masukkan harga baru untuk voucher tersebut: ")
                        listvoucher[voucher_to_update] = new_price
                        print(f"Voucher '{voucher_to_update}' berhasil di-update!")
                    else:
                        print("Voucher tidak ditemukan!")

                    input("\nKlik enter untuk melanjutkan...")

                elif pilihan == "4":
                    os.system('cls || clear')
                    print("="*40)
                    print("List Voucher Game".center(40))
                    print("="*40)
                    if listvoucher:
                        for key, value in listvoucher.items():
                            print(f"{key} Diamond - Rp. {value}")
                    else:
                        print("Voucher tidak ada")
                    input("\nKlik enter untuk melanjutkan...")

                elif pilihan == "5":
                    break
                else:
                    print("\nPilihan tidak tersedia!")
                    input("\nKlik enter untuk melanjutkan...")
        else:
            os.system("cls || clear")
            print("Kesempatan login sudah habis! Keluar dari program!")
            break

    elif pilihan_awal == "2":
        os.system('cls || clear')
        print("="*40)
        print("Registrasi Akun".center(40))
        print("="*40)
        username = input("Masukkan nama akun baru: ")
        password = input("Masukkan password baru: ")
        listuser[username.lower()] = password
        print("\nAkun berhasil didaftarkan!")
        input("\nKlik enter untuk melanjutkan...")

    elif pilihan_awal == "3":
        break

    else:
        print("\nPilihan tidak tersedia!")
        input("\nKlik enter untuk melanjutkan...")

os.system("cls || clear")
print("="*40)
print("Program Selesai!".center(40))
print("="*40)
