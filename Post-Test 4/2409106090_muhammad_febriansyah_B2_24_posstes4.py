percobaan = 0
username="febri"
pw="90"
while percobaan < 3:
    masukkan_nama=input("masukkan nama akun kamu:")
    masukkan_pw=input("masukkan pw akun kamu:")
        
    if masukkan_nama == username or masukkan_pw == pw:
        print('login berhasil')
        berat_badan=float(input("masukkan berat badan: "))
        tinggi_badan=float(input("masukkan tinggi badan: "))
        tinggi_m=float(tinggi_badan/100)
        BMI=float(berat_badan/(tinggi_m * tinggi_m))
        if BMI<18.5:
            print("berat badan kamu underweight")
        elif BMI>=18.5 and BMI<=24.9:
            print("berat badan kamu normal")
        elif BMI>=24.9 and BMI<=29.9:
            print("berat badan kamu overweight")
        elif BMI > 29.9:
            print("mohon maaf badan kamu obesitas")
        opsi = input("ingin berhenti ? \n 1. ya \n 2. tidak \n\n pilih nomor 1/2 : ")
        if opsi == "2":
            continue
        else:
            break
    else:
        print("login gagal")
        percobaan += 1
