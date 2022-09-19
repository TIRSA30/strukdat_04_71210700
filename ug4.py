import json

with open('mahasiswa.json', 'r') as file:
    a = json.load(file)

    b = dict()
    c = int(input("Masukkan Jumkah Mahasiswa baru : "))

    for i in range(c):
        nm = input("Masukkan nama anda: ")
        hb = []

        untuk_hobi = int(input("Masukkan jumlah hobi: "))
        for j in range(untuk_hobi):
            hb1 = input("Masukkan hobi ke-{} : ".format(j+1))
            hb.append(hb1)
        per = input("Masukkan prestasi anda: ")

        print("====Data Berhasil ditambahkan===")
        print()

        b [nm] = [{"Biodata": {"Hobi": hb, "Prestasti" : per}}]

    a.update(b)

with open('mahasiswa.json', 'w') as file:
    json.dump(a,file)