def header():
    print("MENGHITUNG LUAS SEGITIGA")

header()

def luas_segitiga():
    alas = float(input('Masukkan alas: '))
    tinggi = float((input('Masukkan tinggi: ')))

    return alas, tinggi


def hitung_luas(alas, tinggi):
    return 0.5 * alas * tinggi


alas, tinggi = luas_segitiga()
print(hitung_luas(alas, tinggi))
