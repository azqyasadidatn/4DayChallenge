'''
1. numpy
2. Fungsi os.path,Tujuan & Kegunaan

os.path.join(),
Menggabungkan komponen jalur secara cerdas. 
Ini adalah fungsi terpenting. Daripada menulis 'folder' + '/' + 'file.jpg', 
Anda bisa menulis os.path.join('folder', 'file.jpg'). Fungsi ini akan otomatis 
menggunakan pemisah jalur yang benar (/ di Linux/macOS, \ di Windows).

os.path.exists(),
Memeriksa apakah file/folder ada. Digunakan untuk pengecekan error yang baik 
sebelum memanggil cv2.imread(). Ini mencegah AttributeError: 'NoneType' jika gambar tidak ditemukan.

os.path.abspath(),
Mengubah jalur relatif menjadi jalur absolut (lengkap). Membantu menghilangkan ambiguitas saat program
dijalankan dari direktori yang berbeda.
'''
import cv2
import numpy
import os

image = cv2.imread(r'D:\Azqya Old Code 2\PY and NumPy\30 Day Plylist\azqya.jpg')
# image = cv2.imread(r'D:\Azqya Old Code 2\PY and NumPy\30 Day Plylist\burung.jpg')
# image = os.path.join('D:', 'Azqya Old Code 2', 'PY and NumPy', '30 Day Plylist', 'azqya.jpg')
# print(image) 
# # print(image.shape)

# window_name = 'Gambarku'
# cv2.namedWindow(window_name,cv2.WINDOW_NORMAL) #memungkinkan ubah ukuran jendela
# cv2.resizeWindow(window_name,400,420)

'''
if image is not None :
    window_name = 'Gambarku'
    cv2.namedWindow(window_name,cv2.WINDOW_NORMAL) #memungkinkan ubah ukuran jendela
    cv2.resizeWindow(window_name,800,600)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else :
    print ("ERORRRRRRRR HUHUUU TT")
print(image)
'''
##############MENGUBAH DAN MENGAKSES PIKSEL TERTENTU##########################
'''
cara mengakses nilai BGR dari piksel tunggal, misalnya 
piksel di koordinat (100, 50). Ini adalah kunci untuk 
memahami bagaimana cara mengubah warna pada titik tertentu
di gambar.
'''

'''

pixel_value = image[100,50]

print(f"Nilai BGR piksel(100,50) : {pixel_value}")

image[ 700 :900, 200:400] = [0, 200, 100]
image[700:900, 1000:1200] = [100, 0, 1]
image[100:300, 1000:1200] = [100, 0, 1]
cv2.imshow(window_name,image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
##########################(Region of Interest / ROI)##########################
'''
Tujuan dari ROI adalah mengambil sub-array (bagian kecil) dari gambar asli. 
!! Saat memotong ROI, variabel roi yang baru tetap menjadi array NumPy yang independen !!

'''

# roi = image[700:1100, 700:900]

# cv2.imshow(window_name, roi)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
##########################   RESIZE  && COLOR  ##########################
resize_image = cv2.resize(image,(640,480))

img_color = cv2.cvtColor(resize_image, cv2.COLOR_BGR2RGB)

cv2.imshow('gambar', img_color)

# cv2.imshow('gambar', resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()