# nama : azqya
# nama file : simple kalkulator
# deskripsi : Gakkk adaaa hehe
'''
Fokusnya bukan cuma hitung, tapi ngerti cara kerja function dan alur data di Python.

Program minta user pilih operasi (tambah, kurang, kali, bagi).
User masukin dua angka.
Program panggil function sesuai operasi yang dipilih.
Function ngitung dan return hasilnya.
Hasil ditampilkan ke layar.

perhitungan simple hanya ada kali bagi tambah kurang
'''

def kali(a,b):
    return a*b
def bagi(a,b):
    return a/b
def tambah(a,b):
    return a +b
def kurang(a,b):
    return a - b

while True :
    x = "==========="
    print(f"{x} Simple Kalkulator{x}")
    print('''Pilih Operasi :
    1. Kali
    2. Bagi
    3. Tambah
    4. Kurang
    5. Keluar''')
    PilihanOperasi = input(": ")

    if PilihanOperasi == "5" :
        print("Okkey See U deh yaaa")
        break

    angka1= float(input("Masukan angka 1 :"))
    angka2= float(input("Masukan angka 2 :"))
    if PilihanOperasi == "1" :
        print(f"Hasil : {kali(angka1,angka2)}")
    elif PilihanOperasi == "2" :
        print(f"Hasil : {bagi(angka1,angka2)}")
    elif PilihanOperasi == "3" :
        print(f"Hasil : {tambah(angka1,angka2)}")
    elif PilihanOperasi == "4" :
        print(f"Hasil : {kurang(angka1,angka2)}")
    else:
        print("Hayooo kamu cuma bisa pilih angka di menu yaaa")