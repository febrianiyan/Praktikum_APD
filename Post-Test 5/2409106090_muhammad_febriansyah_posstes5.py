import os

# List untuk menyimpan akun yang terdaftar
listuser = []
jenisvoucher = ["160"]
hargavoucher = ["20000"]
listvoucher = [jenisvoucher, hargavoucher] 
kesempatan = 3
isLogin = False 

# Menu awal untuk login atau registrasi
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
        # Proses login
        while kesempatan > 0:
            os.system('cls || clear')
            print("="*40)
            print("Login Form".center(40))
            print("="*40)
            username = input("Masukkan nama akun\t: ")
            password = input("Masukkan password\t: ")

            # Cek akun admin atau akun terdaftar
            if (username.lower() == "febri" and password == "90") or \
                any(user['username'] == username.lower() and user['password'] == password for user in listuser):
                isLogin = True
                print("\nBerhasil login!")
                input("\nKlik enter untuk melanjutkan...")
                break

            kesempatan -= 1
            print("\nUsername atau password salah!")
            print(f"\nKesempatan login tersisa {kesempatan} kali lagi!")
            input("\nKlik enter untuk melanjutkan...")

        if isLogin:
            # Program CRUD jika berhasil login
            while isLogin:
                os.system('cls || clear')
                print("="*40)
                print("Program CRUD Pembelian Voucher Game".center(40))
                print("="*40)
                if username == "febri":
                    print("[1] Tambah Voucher Game")
                    print("[2] Hapus Voucher Game")
                print("[3] List Voucher Game")
                print("[4] Ganti Akun")
                pilihan = input("\nMasukkan pilihan: ")

                if pilihan == "1" and username =="febri":
                    os.system('cls || clear')
                    print("="*40)
                    print("Tambah Voucher Game".center(40))
                    print("="*40)

                    voucherbaru = input("masukkan jumlah diamond\t: ")
                    hargabaru = input("masukkan harga\t\t: ")

                    jenisvoucher.append(voucherbaru)
                    hargavoucher.append(hargabaru)
                    # program penambahan voucher game

                    input("\nKlik enter untuk melanjutkan...")
                elif pilihan == "2":
                    os.system('cls || clear')
                    print("="*40)
                    print("Hapus Voucher Game".center(40))
                    print("="*40)
                    # program menghapus voucher game
                    
                    # Tampilkan list voucher game yang tersedia
                    print("List Voucher Game:")
                    for i in range(len(jenisvoucher)):
                        print(f"[{i+1}] {jenisvoucher[i]} Diamond - Rp{hargavoucher[i]}")

                    # Meminta input pengguna untuk memilih voucher yang akan dihapus
                    hapus_voucher = input("\nMasukkan nomor voucher yang ingin dihapus: ")

                    # Pengecekan apakah input adalah angka dan valid
                    if hapus_voucher.isdigit():
                        hapus_voucher = int(hapus_voucher) - 1
                        if hapus_voucher >= 0 and hapus_voucher < len(jenisvoucher):
                            # Hapus voucher dari kedua list
                            del jenisvoucher[hapus_voucher]
                            del hargavoucher[hapus_voucher]
                            print("\nVoucher berhasil dihapus!")
                        else:
                            print("\nNomor voucher tidak valid!")
                    else:
                        print("\nInput harus berupa angka!")

                    input("\nKlik enter untuk melanjutkan...")
                elif pilihan == "3":
                    os.system('cls || clear')
                    print("="*40)
                    print("List Voucher Game".center(40))
                    print("="*40)
                    if jenisvoucher and hargavoucher:
                        print("Hubungi 0822-3471-8877")
                        print()
                        for i in range(len(jenisvoucher)):
                            print(f"{i+1}. {jenisvoucher[i]} Diamond - Rp. {hargavoucher[i]}")
                    else:
                        print("voucher tidak ada")
                    # program pembelian voucher game
                    input("\nKlik enter untuk melanjutkan...")

                elif pilihan == "4":
                    break
                else:
                    print("\nPilihan tidak tersedia!")
                    input("\nKlik enter untuk melanjutkan...")
        else:
            os.system("cls || clear")
            print("Kesempatan login sudah habis! Keluar dari program!")
            break

    elif pilihan_awal == "2":
        # Proses registrasi akun
        os.system('cls || clear')
        print("="*40)
        print("Registrasi Akun".center(40))
        print("="*40)
        username = input("Masukkan nama akun baru: ")
        password = input("Masukkan password baru: ")
        # Menambahkan akun ke listuser
        listuser.append({"username": username.lower(), "password": password})
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
