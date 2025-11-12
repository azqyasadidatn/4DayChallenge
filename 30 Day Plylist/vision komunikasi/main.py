
import serial
import time

# PR 

'''
 Ambil koordinat posisi objek (x, y, w, h) dari hasil result YOLO.
 Hitung posisi relatif objek terhadap tengah frame.
 Buat logika gerak robot (misal: geser kanan/kiri/maju) berdasar posisi itu.
 Kirim perintah ke mikrokontroler (ESP32/Arduino) pakai pyserial.
 (Opsional) Kasih delay / trigger manual biar gak auto-capture tiap frame (sekarang nyimpen terus).
'''



stm32 = serial.Serial('COM3', 9600)   # ganti 'COM3' sesuai port kamu
time.sleep(2)

center_x = 720 // 2
center_y = 480 // 2
margin = 50 


# model= YOLO(model_path)

result = model ( frame, stream= True)
for r in result :
    boxes = r.boxes
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        label = model.names[cls]


        obj_center_x = int((x1 + x2) / 2)
        obj_center_y = int((y1 + y2) / 2)

        if conf > 0.8:
                if obj_center_x < center_x - margin:
                    stm32.write(b'LEFT\n')
                    print("Geser kiri")
                elif obj_center_x > center_x + margin:
                    stm32.write(b'RIGHT\n')
                    print("Geser kanan")
                else:
                    stm32.write(b'PICK\n')
                    print("Ambil!")

stm32.close()