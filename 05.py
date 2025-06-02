# jumlah_pohon = 50
# if jumlah_pohon > 30:
    # print("Arry Hutomo tanam banyak pohon, keren!")
# else:
    # print("Arry Hutomo perlu tanam lebih banyak pohon!")
# berat_sampah = 12.5
# if berat_sampah >= 10:
    # print("Arry Hutomo daur ulang cukup banyak sampah!")
# else:
    # print("Arry Hutomo perlu daur ulang lebih banyak")
# hemat_energi = True
# if hemat_energi:
    # print("Arry Hutomo hemat energi, top!")
# else:
    # print("Arry Hutomo perlu lenih hemat energi!")
# donasi = 500000
# if donasi > 3000000:
    # print("Arry Hutomo donasi banyak buat anak yatim!")
# else:
    # print("Arry Hutomo bisa donasi lebih banyak!")
# jumlah_pohon = int(input("masukkan jumlah pohin yang ditanam Arry Hutomo: "))
# if jumlah_pohon > 50:
    # print("Arry Hutomo tanam banyak pohon, luar biasa!")
# else:
    # print("Arry Hutomo perlu tanam lebih banyak pohon!")
# sampah = float(input("masukkan berat sampah (kg): "))
# daur = float(input("masukkan sampah yang didaur ulang (kg): "))
# sisa = (daur - sampah)
# if sisa > 0:
    # print(f"Arry Hutomo masih punya sia {sisa} kg sampah!")
# else:
    # print("Arry Hutomo udah daur ulang semua sampah!")
# lampu = 5
# rumah = 3
# total = lampu * rumah
# if total >10:
    # print(f"Arry Hutomo hemat {total} lampu, keren!")
# else:
    # print("Arry Hutomo perlu hemat lebih banyak lampu!")
# donasi = int(input("masukkan jumlah donasi (Rp): "))
# if donasi >= 1000000:
    # print( "Arry Hutomo donasi besar buat UMKM!" )
# else:
    # print("Arry Hutomo bisa donasi lebih banyak!")
# pohon = 60
# if pohon > 50:
    # print(f"Arry Hutomo tanam {pohon}!\nkeren banget!")
# else:
    # print(f"Arry Hutomo tanam {pohon} pohon!\nayo tambah lagi!")
# sampah = 15.5
# if sampah:
    # print( "Arry Hutomo daur ulang", sampah, "kg", "keren!", sep=" - ")
# else:
    # print("Arry Hutomo daur ulang", sampah, "kg", "tambah lagi!", sep=" - ")
# lampu = 12
# if lampu > 10:
    # print(f"Arry Hutomo hemat {lampu} lampu ", end="")
    # print("di rumah!")
# else:
    # print(f"Arry Hutomo hemat {lampu} lampu ", end="")
    # print("tambah lagi!")
# pohon = 100
# tambah = 50
# mati = 20
# total = (pohon + tambah - mati)
# if total > 100:
    # print(f"Arry Hutomo punya {total} pohon, banyak banget!")
# else:
    # print(f"Arry Hutomo punya {total} pohon, tambah lagi!")
# donasi = int( input("masukkan total donasi (Rp): "))
# penerima = int( input("masukkan jumlah penerima: "))
# sisa = donasi % penerima
# if sisa == 0:
    # print( "Arry Hutomo bagi donasi merata!" )
# else:
    # print(f"Arry Hutomo punya sisa Rp {sisa}!")
# lampu = int(input("masukkan jumlah lampu: "))
# rumah = int(input("masukkan jumlah rumah: "))
# bagi = lampu // rumah
# if bagi > 5:
    # print(f"Arry Hutomo bagi {bagi} lampu per rumah!\nluar biasa!")
# else:
    # print(f"Arry Hutomo bagi {bagi} lampu per rumah!\ntambah lagi!")
sampah = float(input("masukkan berat sampah awal (kg): "))
daur = float(input("masukkan sampah yang di daur ulang (kg): "))
tambah = float(input("masukkan sampah tambahan (kg): "))
total = (sampah - daur + tambah) * 2 / 3
if total > 50:
    print(f"Arry Hutomo hitung sampah {total} kg!\nluar biasa ", "bareng ECC Team!", sep="=>", end="")
    print( "yuk!" )
else:
    print(f"Arry Hutomo hitung sampah {total} kg!\ntambah lagi", "bareng ECC Team!", sep="=>", end="")
    print( "yuk!" )