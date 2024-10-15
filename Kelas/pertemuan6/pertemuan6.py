#Deklarasi Dictionary

# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# daftar_buku={}
# daftar_buku["novel 1"]="senyum pertama di pagi hari"
# print (daftar_buku)

#Sifat Dictionary

# musik = {
# "judul" : "All we Know",
# "judul" : "Something Just Like This"
# }
# print(musik["judul"])

#Membuat Dictionary

# Biodata = {
# "Nama" : "Aldy Ramadhan Syahputra",
# "NIM" : 2109106079,
# "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" :True,
# "Social Media" : {
# "Instagram" : "@aldyrmdhns_",
# "Discord" : "\'Izanami#6848"
# }
# }

# daftar_buku={}
# daftar_buku["novel 1"]="senyum pertama di pagi hari"
# daftar_buku[1]="matahri"
# # print (daftar_buku)
# daftar_buku=dict(Buku1 = "herry poter", Buku2 = "percy jackson")
# print (daftar_buku)

#Mengakses Item pada Dictionary

# print(daftar_buku.get("buku2"))
# print(daftar_buku[2])

#Perulangan pada Python

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# for i in Nilai:
#     print (i)

# for i, j in Nilai.items():
#     print(f"nilai dari {i} itu valuenya adalah {j}")

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# Nilai["struktur data"]=99

# Nilai.update({"struktur data":99})
# Nilai.update({"Matematika":70})
# print(Nilai)

#8.10.Menghapus Item Pada Dictionary

# data = {
# "Nama" : "Aldy",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# del data["Nama"]
# #Setelah diubah
# print(data)
# #memanggil data yang telah dihapus
# print(data.get("Nama"))

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# print(Nilai)
# print()
# trashbin=Nilai.pop("Matematika")
# print(Nilai)
# print()
# print(trashbin)

# del Nilai["Fisika"]
# print(Nilai)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# print(f"jumlah elemen dari variabel dict nilai adalah {len(Nilai)}")

#Copy & Fromkeys

# Buku = {
# "No Longer Human" : "Osamu Dazai",
# "Harry Potter" : "J.K. Rowlings",
# "Hamlet" : "William Shakespeare"
# }
# pinjam = Buku.copy()
# print("Dictionary yang Telah Disalin : ", pinjam)

import os

os.system("cls")
# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

#Keys & Value

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# #menggunakan keys
# for i in Nilai.keys():
#  print(i)
# print("")
# #menggunakan value
# for i in Nilai.values():
#  print(i)

#Setdefault

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)

#Dictionary of List and Nested Dictionary

# Musik = {
#     "The Chainsmoker" : ["All we Know", "TheParis"],
#     "Alan Walker" : ["Alone", "Lily"],
#     "Neffex" : ["Best of Me", "Memories"]
# }
# #mengakses key dan value dari dictionary
# for i, j in Musik.items():
#  print(f"Musik milik {i} adalah : ")
# #mengambil nilai dari list
# for song in j:
#  print(song)
# print("")

mahasiswa = {
101 : {"Nama" : "Aldy", "Umur" : 19},
111 : {"Nama" : "Abdul", "Umur" : 18, "Hobi" : "makan,tidur,olahraga "}
}
# for key, value in mahasiswa.items():
#  print("ID Mahasiswa : ", key)
# for key_a, value_a in value.items():
#  print (key_a, " : ", value_a)
# print("")

print(mahasiswa[111]["Hobi"][-1])