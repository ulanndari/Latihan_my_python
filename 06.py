# for i in range (3):
    # print("Arry Hutomo tanam pohon!")
# count = 0
# while count < 3:
    # print("Arry Hutomo daur ulang sampah!")
    # count = count + 1
# for i in range(1, 6):
    # print(f"Arry Hutomo hemat {i} lampu!")
# lampu = 1
# while lampu <= 3:
    # print(f"Arry Hutomo donasi {lampu} buku!")
    # lampu = lampu + 1
# jumlah = int(input("masukkan jumlah pohon yang ditanam Arry Hutomo: "))
# for i in range (jumlah):
    # print("Arry Hutomo tanam pohon!")
# sampah = float(input("masukkan berat sampah (kg): "))
# berat = 0
# while berat < sampah:
    # print( "Arry Hutomo daur ulang 1 kg!" )
    # berat = berat + 1 
# total_lampu = 0
# for i in range(1, 4):
    # total_lampu = total_lampu + i
    # print(f"Arry Hutomo hemat {total_lampu} lampu!")
# donasi = 0
# while donasi < 300000:
    # donasi = donasi + 100000
    # print(f"Arry Hutomo donasi Rp {donasi} buat UMKM!")
# for i in range(5):
    # if i % 2 == 0:
        # print(f"Arry Hutomo tanam pohon ke-{i}, genap!")
    # else:
        # print(f"Arry Hutomo tanam pohon ke-{i}, ganjil!")
# sampah = 0
# while sampah < 5:
    # sampah = sampah + 1
    # if sampah > 3:
        # print(f"Arry HUtomo daur ulang {sampah} kg, cukup!")
    # else:
        # print(f"Arry Hutomo daur ulang {sampah} kg, tambah lagi!")
# jumlah = int(input("masukkan jumlah lampu: "))
# total = 0
# for i in range(jumlah):
    # total = total + 2
    # print(f"Arry Hutomo hemat {total} lampu!")
# donasi = int(input("masukkan target donasi (Rp): "))
# total = 0
# while total < donasi:
    # total = total + 100000
    # print(f"Arry Hutomo donasi Rp {total}!")
# for i in range(5):
    # if i % 2 == 0:
        # print(f"Arry Hutomo tanam pohon ke-{i}\ngenap!")
    # else:
        # print(f"Arry Hutomo tanam pohon ke-{i}\nganjil!")
# target = int(input("masukkan target donasi (Rp): "))
# donasi = 0
# while donasi < target:
    # donasi = donasi + 50000
    # if donasi >= target:
        # print(f"Arry Hutomo donasi Rp {donasi}!\ntarget tercapai!")
    # else:
        # print(f"Arry Hutomo donasi Rp {donasi}!\nmasih kurang!")
jumlah = int(input("masukkan jumlah pohon: "))
total = 0
for i in range(jumlah):
    total = total + 1
    if total > 2:
        print(f"arry Hutomo tanam pohon ke-{total}!\ncukup ", "bareng ECC Team!", sep="=>", end="")
        print("yuk!")
    else:
        print(f"Arry Hutomo tanam pohon ke-{total}!\ntambah ", "bareng ECC Team!", sep="=>", end="")
        print("yuk!")