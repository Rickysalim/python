def jualan():
    a = "capucino"
    b = "teh"
    print ("Pilihan")
    print ("1.", a)
    print ("2.", b)
    print ("3. Exit")

def capucino():
    cap = "memilih capucino"
    print(cap)
    capucino = int(input("masukkan harga : "))
    ppn = 10/100
    total = capucino*ppn
    print("jumlah yang harus di bayarkan",total+capucino)

def teh():
    te = "memilih TEH"
    print(te)
    teh = int(input("masukkan harga : "))
    ppn = 10/100
    total = teh*ppn
    print("jumlah yang harus di bayarkan",total+teh)

def welcome():
    nim = int(input("masukan nim: "))
    nama = str(input("masukan nama: "))
    print ("NIM : ", nim)
    print ("NAMA : ", nama)
    print ("-------------------")

def end():
    print ("-------------------")

while True:
    welcome()
    jualan()
    pil = int(input("masukkan pilihan : "))
    if pil == 1:
        capucino()
    elif pil == 2:
        teh()
    elif pil == 3:
        break
    else:
        print ("pilihan salah")
    end()