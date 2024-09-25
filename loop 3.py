total_belanja = float(input("masukkan total belanja: "))
if (total_belanja >= 300000):
    diskon = 0.15 * total_belanja
    total_bayar = total_belanja - diskon
    print  ("selamat anda dapat diskon sebanyak 15% jadi total barang anda adalah: ", total_bayar)

else: print  ("total barang anda adalah", total_belanja)