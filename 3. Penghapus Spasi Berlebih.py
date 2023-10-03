"""
    Nama: Gerry Moeis M.D.P
    Kelas: 2023E
    NIM: 23091397164
    Prodi: D4 Manajemen Informatika
"""

kalimat = input("Masukkan kalimat yang diinginkan (Kalau bisa yg gk beratur): ").strip()
kalimat_yang_diperbaiki = []
for kata in kalimat.split(" "):
    if len(kata) > 0: kalimat_yang_diperbaiki.append(kata)

print(f"Kalimat awal: {kalimat}")
print(f"Diperbaiki menjadi: {' '.join(kalimat_yang_diperbaiki)}")