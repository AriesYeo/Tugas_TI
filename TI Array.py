
# # CATATAN ARRAY

# # 1.Basic Info ngecek total item
# # array = [ 1, 2, 3, 4, 6]
# # array [0] = "siwa"
# # total = len (array)
# # print (total)

# # 2.Menggantikan item Array ke item lain
# # array = [ 1, 2, 3, 4, 6]
# # array [0] = "siwa"
# # print (array[0], array[1])

# # 3.Array print biasa
# # array = [ 1, 2, 3, 4, 6]
# # for x in array:
# #     print (x)

# # 4.Menambahkan array dan membuat mereka menjadi deret 
# # array = [ 1, 2, 3, 4, 6, "Tono"]
# # array.append("budi")
# # array. append ("tono")
# # print (array)


# # Tugas pertama Versi 1

# # array = [1,2,3,4,5,6,7,8,9,10]
# # print (array[1], array[3], array[5], array[7], array[9])

# # Tugas Pertama versi 2

# # def Num(arr):
# #     hasil = []
# #     for bilangan in arr:
# #         if bilangan % 2 == 0:
# #             hasil.append(bilangan)
# #     return hasil

# # i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # hasil = Num(i)
# # print(hasil)

# # Tugas Pertama versi 3

# # Array = [1,2,3,4,5,6,7,8,9,10]
# # genap = [x for x in Array if x %2 == 0 ]
# # print (genap)


# # Tugas Kedua Versi 1

# # array = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]
# # array[1] = "senin" 
# # print (array[1])
# # # Tugas Kedua versi 2 
# # def hari(x):
# #     # Array yang berisi nama hari dari Senin hingga Minggu
# #     hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    
# #     # Cek apakah input valid (antara 1 hingga 7)
# #     if 1 <= x <= 7:
# #         return {hari[x - 1]}
# #     else:
# #         return "Input tidak valid. Masukkan angka antara 1 hingga 7."

# # # Contoh input
# # x = int(input("Masukkan angka (1-7): "))
# # print(hari(x))


# # Tugas ketiga 
# # def cek (nama):
# #     Karyawan = ["budi", "bunga", "alex", "mawar", "dani", "sultan"]
# #     if nama.lower() in Karyawan:
# #         return f"{nama.capitalize()} adalah karyawan."
# #     else:
# #         return f"{nama.capitalize()} bukan karyawan."

# # nama = input("Input Nama Karyawan: ")
# # print (cek(nama))

# # Tugas Keempat
# # input_angka = input("Masukkan deret angka (pisahkan dengan koma): ")
# # angka = [int(num) for num in input_angka.split(",")]
# # angka.sort()
# # print (angka)



# # # tugas kelima 

# input_angka = input("Masukkan angka (pisahkan dengan koma): ")
# angka = [int(num) for num in input_angka.split(",")]
# total= sum(angka)
# print (total)


# Tugas keenam (ide aplikasi dengan menggunakawn array)

#bikin aplikasi to do list biar kita bisa ingat