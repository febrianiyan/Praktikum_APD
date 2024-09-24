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
else:
    print("mohon maaf badan kamu obesitas")