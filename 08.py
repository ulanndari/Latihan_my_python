# pohon_dict = {"mangrove": 10, "kelapa": 5, "mahoni": 8}
# print("Arry Hutomo tanam pohon:", pohon_dict)
# pohon_dict = {"mangrove": 10, "kelapa": 5, "mahoni": 8}
# print(f"Arry Hutomo tanam pohon kelapa: {pohon_dict['kelapa']}")
# pohon_dict = {"mangrove": 10, "kelapa": 5, "mahoni": 8}
# pohon_dict["kelapa"] = 15
# print("Arry Hutomo tanam pohon:", pohon_dict)
# pohon_dict = {"mangrove": 10, "kelapa": 5}
# pohon_dict["mahoni"] = 8
# print("Arry Hutomo tanam pohon:", pohon_dict)
# pohon_dict = {}
# jumlah = int(input("masukkan jumlah pohon: "))
# for i in range(jumlah):
    # pohon = input(f"masukkan nama pohon ke-{i+1}: ")
    # jumlah_pohon = int(input("masukkan jumlah {pohon}: "))
    # pohon_dict[pohon] = jumlah_pohon
# print("Arry Hutomo tanam pohon:", pohon_dict)
# pohon_dict = {"mangrove": 10, "kelapa": 5, "mahoni": 8}
# for pohon, jumlah in pohon_dict.items():
    # print(f"Arry Hutomo tanam {pohon}: {jumlah}!")
# pohon_dict = {"mangrove": 10, "kelapa": 5, "mahoni": 8}
# keys = list(pohon_dict.keys())
# i = 0
# while i < len(keys):
    # pohon = keys[i]
    # print(f"Arry Hutomo tanam {pohon}: {pohon_dict[pohon]}!")
    # i = i + 1
# pohon_dict = {"mangrove": 10, "kelapa": 5, "mahoni": 8}
# for pohon, jumlah in pohon_dict.items():
    # if jumlah > 7:
        # print(f"Arry Hutomo tanam {pohon}: {jumlah}, banyak!")
    # else:
        # print(f"Arry Hutomo tanam {pohon}, {jumlah}, tambah lagi!")
# pohon_dict = {}
# for i in range(3):
    # pohon = input(f"masukkan nama pohon ke-{i+1}: ")
    # jumlah = int(input(f"masukkan jumlah {pohon}: "))
    # pohon_dict[pohon] = jumlah
    # for pohon, jumlah in pohon_dict.items():
        # print(f"Arry Hutomo tanam {pohon}: {jumlah}!")
# berat_dict = {}
# jumlah = int(input("masukkan jumlah sampah: "))
# for i in range(jumlah):
    # jenis = input(f"masukkan jenis sampah ke-{i+1}: ")
    # berat = float(input(f"masukkan berat {jenis} (kg): "))
    # berat_dict[jenis] = berat
# total = 0
# for berat in berat_dict.values():
    # total = total + berat
# print(f"Arry Hutomo daur ulang {total} kg!")
# berat_dict = {"plastik": 5.5, "kertas": 10.5, "organik": 3.0}
# for jenis, berat in berat_dict.items():
    # if berat > 5:
        # print(f"Arry Hutomo daur ulang {jenis}: {berat} kg, banyak!")
    # else:
        # print(f"Arry Hutomo daur ulang {jenis}: {berat} kg, tambah lagi!")
# lampu_dict = {}
# i = 0
# while i < 3:
    # ruangan = input(f"masukkan ruangan ke-{i+1}: ")
    # lampu = int(input(f"masukkan jumlah lampu di {ruangan}: "))
    # lampu_dict[ruangan] = lampu
    # i = i + 1
# total = 0
# for lampu in lampu_dict.values():
    # total = total + lampu
# print(f"Arry Hutomo hemat {total} lampu!")
# donasi_dict = {"sekolah": 100000, "panti asuhan": 200000, "masjid": 50000}
# for tempat, donasi in donasi_dict.items():
    # if donasi > 150000:
        # print(f"Arry Hutomo donasi ke {tempat}: Rp {donasi}!\nbanyak ", "buat komunitas!", sep="=>", end="")
        # print("yuk!")
    # else:
        # print(f"Arry Hutomo donasi ke {tempat}: Rp {donasi}!\ntambah ", "buat komunitas!", sep="=>", end="")
        # print("yuk!")
berat_dict = {}
i = 0
while i < 3:
    jenis = input(f"masukkan jenis sampah ke-{i+1} ")
    berat = float(input(f"masukkan berat {jenis} (kg): "))
    berat_dict[jenis] = berat
    i = i + 1
total = 0
for jenis, berat in berat_dict.items():
    total = total + berat
    if total > 10:
        print(f"Arry Hutomo daur ulang {total} kg!\ncukup ", f"{jenis} banyak!", sep="=>", end="")
        print("yuk!")
    else:
        print(f"Arry Hutomo daur ulang {total} kg!\ntambah ", f"{jenis} kurang!", sep="=>", end="")
        print("yuk!")