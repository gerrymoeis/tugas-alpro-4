"""
    Nama: Gerry Moeis M.D.P
    Kelas: 2023E
    NIM: 23091397164
    Prodi: D4 Manajemen Informatika
"""

kata1 = input("Masukkan kata yang diinginkan: ").strip()
kata2 = input("Masukkan kata lain yang diinginkan: ").strip()

anagram1 = sorted(kata1.lower())
anagram2 = sorted(kata2.lower())

print(f"Kata {kata1} {'adalah' if anagram1 == anagram2 else 'bukan'} anagram dari {kata2}")