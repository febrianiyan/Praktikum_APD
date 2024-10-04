import os

os.system('cls || clear')

mahasiswa = ["Steven", "Michael", "Selyn"]
kesempatan = 3
isLogin = False

while kesempatan > 0:
    os.system('cls || clear')
    print("="*40)
    print("Login Form".center(40))
    print("="*40)
    username = input("Masukkan nama akun\t: ")
    password = input("Masukkan password\t: ")
    if username.lower() == "admin" and password == "admin":
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
        print("Program CRUD Daftar Mahasiswa".center(40))
        print("="*40)
        print("[1] Lihat Daftar Nama Mahasiswa")
        print("[2] Tambah Nama Mahasiswa")
        print("[3] Edit Nama Mahasiswa")
        print("[4] Hapus Nama Mahasiswa")
        print("[5] Keluar Program")
        pilihan = input("\nMasukkan pilihan: ")

        if pilihan == "1":
            os.system('cls || clear')
            print("="*40)
            print("Daftar Nama Mahasiswa".center(40))
            print("="*40)
            # program melihat daftar nama mahasiswa
            index=0
            for i in mahasiswa:
             print(f"{index+1}.",i)
             index+=1

            #  for i in range(len(mahasiswa)):
            #      print(f"{i+1}.{mahasiswa[i]}")
            #  for i,date in enumerate(mahasiswa,1)
            #      print(i,date)
            input("\nKlik enter untuk melanjutkan...")
        elif pilihan == "2":
            os.system('cls || clear')
            print("="*40)
            print("Tambah Nama Mahasiswa".center(40))
            print("="*40)
            # program menambahkan nama mahasiswa
            input("\nKlik enter untuk melanjutkan...")
        elif pilihan == "3":
            os.system('cls || clear')
            print("="*40)
            print("Edit Nama Mahasiswa".center(40))
            print("="*40)
            # program mengedit nama mahasiswa
            input("\nKlik enter untuk melanjutkan...")
        elif pilihan == "4":
            os.system('cls || clear')
            print("="*40)
            print("Hapus Nama Mahasiswa".center(40))
            print("="*40)
            # program menghapus nama mahasiswa
            del mahasiswa [2]
            print (mahasiswa)
            input("\nKlik enter untuk melanjutkan...")
        elif pilihan == "5":
            break
        else:
            print("\nPilihan tidak tersedia!")
            input("\nKlik enter untuk melanjutkan...")
else:
    os.system("cls || clear")
    print("Kesempatan login sudah habis! Keluar dari program!")

os.system("cls || clear")
print("="*40)
print("Program Selesai!".center(40))
print("="*40)