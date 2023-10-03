"""
    Nama: Gerry Moeis M.D.P
    Kelas: 2023E
    NIM: 23091397164
    Prodi: D4 Manajemen Informatika
"""

kalimat = input("Masukkan kalimat yang diinginkan: ").strip().split(" ")

def cari_kata(kalimat, min_or_max):
    jumlah_huruf_tiap_kata = [len(kata) for kata in kalimat]
    kata_kata = []

    if min_or_max == "min":
        kata_kata = [kalimat[i] for i, jumlah_huruf in enumerate(jumlah_huruf_tiap_kata) if jumlah_huruf == min(jumlah_huruf_tiap_kata)]
    elif min_or_max == "max":
        kata_kata = [kalimat[i] for i, jumlah_huruf in enumerate(jumlah_huruf_tiap_kata) if jumlah_huruf == max(jumlah_huruf_tiap_kata)]

    return kata_kata

kata_terpendek = cari_kata(kalimat, "min")
kata_terpanjang = cari_kata(kalimat, "max")

print(f"Dalam Kalimat {kalimat}")
print(f"Terdapat kata terpendek yaitu: {', '.join(kata_terpendek)}")
print(f"Terdapat kata terpanjang yaitu: {', '.join(kata_terpanjang)}")