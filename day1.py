'''
nama: Azqya
nama file : To do list sederhana fia terminal
deskripsi : usr memilih dan mengetik pilihan yg di sediakan, lalu meng input pilihannya
menggunakan if else sederhana

Buat variabel kosong buat nyimpen data.
Tambah item baru ke list (belajar .append()).
Tampilkan semua isi list (belajar for loop).
Hapus item dari list (belajar .pop() atau del).

Tujuan konsep:
Tau apa itu list
Paham cara menambah, membaca, dan menghapus data
Paham loop for
'''
x = "==========="
print(f"\n ${x} SIMPLE TO DO LIST ${x} \n")
task = ["Belajar", "main"]
while True :

    print(f'''Apa rencana mu hari ini?
1. Menambah Kegiatan
2. Menghapus Kegiatan
3. Melihat Kegiatan
4. Sudah

Kamu cuma bisa masukan 1 angka dari 1,2,3, dan 4 yaaa
            
''')

    pilihanuser = input("Masukan Pilihanmu[1/2/3/4] : ")
    task2 = task.copy()

    if pilihanuser == "1" :
        tugas = input("Masukkan kegiatanmu kesini :")
        task.append(tugas)
        print("Tugas di tambahkan o-O") 
    elif pilihanuser == "2":
        for i, t in enumerate(task):
            print(f"{i+1}.{t}")
        Hapustugas = int(input("Masukan urutan dari kegiatan mu :"))
        del task[Hapustugas-1]

    elif pilihanuser == "3" :
        for i, t in enumerate(task):
            print(f'''{i+1}.{t} ''')
    elif pilihanuser == "4":
        print("Selesai...")
        break
    else :
        print("Pilihan mu tidak valid")