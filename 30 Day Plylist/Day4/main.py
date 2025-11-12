import cv2
from ultralytics import YOLO
import os
model_path = r'D:\Azqya Old Code 2\PY and NumPy\30 Day Plylist\Day4\best.pt'

# PR 

'''
 Ambil koordinat posisi objek (x, y, w, h) dari hasil result YOLO.
 Hitung posisi relatif objek terhadap tengah frame.
 Buat logika gerak robot (misal: geser kanan/kiri/maju) berdasar posisi itu.
 Kirim perintah ke mikrokontroler (ESP32/Arduino) pakai pyserial.
 (Opsional) Kasih delay / trigger manual biar gak auto-capture tiap frame (sekarang nyimpen terus).
'''

model= YOLO(model_path)
WINDOW_NAME = "Frame"
count = 0
fileName = r"D:\Azqya Old Code 2\PY and NumPy\30 Day Plylist\Day4\Data"
os.makedirs(fileName, exist_ok=True)

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 566)

while True :
    success,frame = camera.read()
    if not success :
        break

    result = model (frame, stream= True)

    anotade_frame_ist = list(result)
    anotade_frame = anotade_frame_ist[0].plot()
    cv2.imshow(WINDOW_NAME, anotade_frame)

    ''' otomatis capture  '''
    file_Name = os.path.join(fileName, f"File{count}.jpg")
    cv2.imwrite(file_Name,frame)
    print(f"Ping! Gambar Tersimpan{file_Name}")
    count += 1
    key = cv2.waitKey(1) & 0xFF
    
    ''' close '''
    if key == ord('q') :
       break
    if cv2.getWindowProperty(WINDOW_NAME,cv2.WND_PROP_VISIBLE) <1 :
        break
    # elif key == ord('c'):


camera.release()
cv2.destroyAllWindows()