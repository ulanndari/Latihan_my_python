# def tanam_pohon():
    # print("Arry Hutomo tanam pohon!")
# 
# tanam_pohon()
# def tanam_pohon (jenis):
    # print(f"Arry Hutomo tanam pohon {jenis}!")
# 
# tanam_pohon("mangrove")
# def hitung_pohon(jumlah):
    # return jumlah + 5
# 
# hasil = hitung_pohon(10)
# print(f"Arry Hutomo tanam {hasil} pohon!")
# def hitung_sampah(berat):
    # return berat * 2
# 
# hasil = hitung_sampah(5.5)
# print(f"Arry Hutomo daur ulang {hasil} kg sampah!")
# def tanam_pohon(jenis):
    # print(f"Arry Hutomo tanam pohon {jenis}!")
# 
# pohon = input("masukkan jenis pohon: ")
# tanam_pohon(pohon)
# def tanam_pohon(jumlah):
    # for i in range(jumlah):
        # print("Arry Hutomo tanam pohon!")
# 
# tanam_pohon(3)
# def cek_pohon(jumlah):
    # if jumlah > 7:
        # print(f"Arry Hutomo tanam {jumlah} pohon, banyak!")
    # else:
        # print(f"Arry Hutomo tanam {jumlah} pohon, tambah lgi!")
# 
# cek_pohon(10)
# def tanam_banyak(jumlah):
    # for i in range(jumlah):
        # print(f"Arry Hutomo tanam pohon ke-{i+1}!")
# 
# jumlah = int(input("masukkan jumlah pohon: "))
# tanam_banyak(jumlah)
# def hitung_total_pohon(pohon_list):
    # total = 0
    # for jumlah in pohon_list:
        # total = total + jumlah
    # return total
# 
# pohon_list = [10, 5, 8]
# hasil = hitung_total_pohon(pohon_list)
# print(f"Arry Hutomo tanam {hasil} pohon!")
# def hitung_total_sampah(berat_dict):
    # total = 0
    # for berat in berat_dict.values():
        # total = total + berat
    # return total
# 
# berat_dict = {"plasti": 5.5, "kertas": 3.0, "organik": 2.5}
# hasil = hitung_total_sampah(berat_dict)
# print(f"Arry Hutomo daur ulang {hasil} kg!")
# def cek_pohon_list(pohon_list):
    # for jumlah in pohon_list:
        # if jumlah > 7:
            # print(f"Arry Hutomo tanam {jumlah} pohon, banyak!")
        # else:
            # print(f"Arry Hutomo tanam {jumlah} pohon, tambah lagi!")
# 
# pohon_list = [10, 5, 8]
# cek_pohon_list(pohon_list)
# def hitung_sampah_dict(berat_dict):
    # keys = list(berat_dict.keys())
    # i = 0
    # total = 0
    # while i < len(keys):
        # total = total + berat_dict[keys[i]]
        # i = i + 1
    # return total
# 
# berat_dict = {"plastik": 5.5, "kertas": 3.0, "organik": 2.5}
# hasil = hitung_sampah_dict(berat_dict)
# print(f"Arry hutomo daur ulang {hasil} kg!")
# def cek_pohon_list(pohon_list):
    # for jumlah in pohon_list:
        # if jumlah > 7:
            # print(f"Arry Hutomo tanam {jumlah} pohon, banyak!")
        # else:
            # print(f"Arry Hutomo tanam {jumlah} pohon, tambah lagi!")
# 
# pohon_list = [10, 5, 8]
# cek_pohon_list(pohon_list)
# def hitung_sampah_dict(berat_dict):
    # keys = list(berat_dict.keys())
    # i = 0
    # total = 0
    # while i < len(keys):
        # total = total + berat_dict[keys[i]]
        # i = i + 1
    # return total
# 
# berat_dict = {"plastik": 5.5, "kertas": 3.0, "organik": 2.5}
# hasil = hitung_sampah_dict(berat_dict)
# print(f"Arry Hutomo daur ulang {hasil} kg!")
# def cek_donasi(jumlah):
    # if jumlah > 150000:
        # print(f"Arry Hutomo donasi Rp {jumlah}!\nbanyak ","buat komunitas!", sep="=>", end="")
        # print("yuk!")
    # else:
        # print(f"Arry Hutomo donasi Rp {jumlah}!\ntambah ","buat komunitas!", sep="=>", end="")
        # print("yuk!")
# 
# donasi = int(input("masukkan jumlah donasi (Rp): "))
# cek_donasi(donasi)
def hitung_dan_cek_sampah(berat_dict):
    total = 0
    i = 0
    keys = list(berat_dict.keys())
    while i < len(keys):
        jenis = keys[i]
        total = total + berat_dict[jenis]
        if total > 10:
            print(f"Arry Hutomo daur ulang {total} kg!\ncukup ",f"{jenis} banyak!", sep="=>", end="")
            print("yuk!")
        else:
            print(f"Arry Hutomo daur ulang {total} kg!\ntambah ",f"{jenis} kurang!", sep="=>", end="")
            print("yuk!")
        i = i + 1
    return total

berat_dict = {}
for i in range(3):
    jenis = input(f"masukkan jenis sampah ke-{i+1} ")
    berat = float(input(f"masukkan berat {jenis} (kg): "))
    berat_dict[jenis] = berat
hasil = hitung_dan_cek_sampah(berat_dict)
print(f"total akhir: {hasil} kg!")