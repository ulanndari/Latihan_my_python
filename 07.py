# pohon_list = ["mangrove", "kelapa", "mahoni"]
# print("Arry Hutomo tanam pohon:", pohon_list)
# pohon_list = ["mangrove", "kelapa", "mahoni"]
# print(f"Arry Hutomo tanam pohon: {pohon_list[1]}")
# pohon_list = ["mangrove", "kelapa", "mahoni"]
# pohon_list[1] = "pinus"
# print("Arry Hutomo tanam pohon:", pohon_list)
# print("Arry Hutomo pohon:", pohon_list[1])
# pohon_list = ["magrove", "kelapa"]
# pohon_list.append("mahoni")
# print("Arry Hutomo tanam pohon:", pohon_list)
# pohon_list =[]
# jumlah = int(input("masukkan jumlah pohon: "))
# for i in range(jumlah):
    # pohon = input(f"masukkan pohon ke-{i+1}: ")
    # pohon_list.append(pohon)
# print("Arry Hutomo tanam pohon:", pohon_list)
# pohon_list= ["mangrove", "kelapa", " mahoni"]
# for pohon in pohon_list:
    # print(f"Arry Hutomo tanam {pohon}!")
# pohon_list = ["manhrove", "kelapa", "mahono"]
# i = 0
# while i < len(pohon_list):
    # print(f"Arry Hutomo tanam {pohon_list[i]}!")
    # i = i + 1
# pohon_list = ["mangrove", "kelapa", "mahoni"]
# for pohon in pohon_list:
    # if pohon == "kelapa":
        # print(f"Arry Hutomo tanam {pohon}, favorit!")
    # else:
        # print(f"Ary Hutomo tanam {pohon}!")
# pohon_list = []
# for i in range(3):
    # pohon = input(f"masukkan pohon ke-{i+1}: ")
    # pohon_list.append(pohon)
    # for pohon in pohon_list:
        # print(f"Arry Hutomo tanam {pohon}")
# pohon_list = ["mangrove", "kelapa", "mahoni"]
# i = 0
# while i < len(pohon_list):
    # if pohon_list[i] == "kelapa":
        # print(f"Arry Hutomo tanam {pohon_list[i]}, favorit!")
    # else:
        # print(f"Arry Hutomo tanam {pohon_list[i]}!")
    # i = i + 1
# berat_list = []
# jumlah = int(input("masukkan jumlah sampah: "))
# for i in range(jumlah):
    # berat = float(input("masukkan berat sampah ke-{i+1} (kg): "))
    # berat_list.append(berat)
# total = 0
# for berat in berat_list:
    # total = total + berat
# print(f"Arry Hutomo daur ulang {total} kg!")
# berat_list = [5.5, 10.5, 3.0]
# for berat in berat_list:
    # if berat > 5:
        # print(f"Arru Hutomo daur ulang {berat} kg, banyak!")
    # else:
        # print(f"Arry Hutomo daut ulang {berat} kg, tambah lagi!")
# lampu_list = []
# i = 0
# while i < 3:
    # lampu = int(input(f"masukkan jumlah lampu ke-{i+1}: "))
    # lampu_list.append(lampu)
    # i = i + 1
# total = 0
# for lampu in lampu_list:
    # total = total + lampu
# print(f"Arry Hutomo hemat {total} lampu!")
# donasi_list = [100000, 200000, 500000]
# for donasi in donasi_list:
    # if donasi > 150000:
        # print(f"Arry Hutomo donasi Rp {donasi}!\nBanyak ", "buat UMKM!", sep="=>", end="")
        # print("yuk!")
    # else:
        # print(f"Arry Hutomo donasi Rp {donasi}!\ntambah ","buat UMKM!", sep="=>", end="")
        # print("yuk!")
berat_list = []
i = 0
while i < 3:
    berat =float(input(f"masukkan berat sampah ke-{i+1} (kg): "))
    berat_list.append(berat)
    i = i + 1
total = 0
for berat in berat_list:
    total = total + berat
    if total > 10:
        print(f"Arry Hutomo daur ulang {total} kg!\ncukup ", "bareng ECC Team!", sep="=>",end="")
        print("yuk!")
    else:
        print(f"Arry Hutomo daur ulang {total} kg!\ntambah ", "bareng ECC Team!", sep="=>", end="")
        print("yuk!")