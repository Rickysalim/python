def header():
    print("=================")
    print("PROGRAM QUIZ")
    print("====================")

header()

def input_nama_dan_nim (): 
    nama = str(input('masukan nama: '))
    nim = str(input('masukan nim: '))
    return nama, nim

def tampil():
    print('nama',nama)
    print('nim',nim)

nama, nim  = input_nama_dan_nim()
tampil()