import cv2
from ultralytics import YOLO
import os
import serial
import time

model_path = r'D:\Azqya Old Code 2\PY and NumPy\30 Day Plylist\Day4\best.pt'

model= YOLO(model_path)
WINDOW_NAME = "Frame"
count = 0

fileName = r"D:\Azqya Old Code 2\PY and NumPy\30 Day Plylist\Day4\Data"
os.makedirs(fileName, exist_ok=True)

stm32 = serial.Serial('COM3', 9600)   # ganti 'COM3' sesuai port kamu
time.sleep(2)

center_x = 720 // 2
center_y = 480 // 2
margin = 50 

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 566)

while True :
    success,frame = camera.read()
    if not success :
        break

    result = model (frame, stream= True)

    for r in result :
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = model.names[cls]


            obj_center_x = int((x1 + x2) / 2)
            obj_center_y = int((y1 + y2) / 2)

    anotade_frame_ist = list(result)
    anotade_frame = anotade_frame_ist[0].plot()
    cv2.imshow(WINDOW_NAME, anotade_frame)

    ''' otomatis capture  '''
    file_Name = os.path.join(fileName, f"File{count}.jpg")
    cv2.imwrite(file_Name,frame)
    print(f"Ping! Gambar Tersimpan{file_Name}")
    count += 1
    key = cv2.waitKey(1) & 0xFF
    
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



    ''' close '''
    if key == ord('q') :
       break
    if cv2.getWindowProperty(WINDOW_NAME,cv2.WND_PROP_VISIBLE) <1 :
        break
    # elif key == ord('c'):


camera.release()
stm32.close()
cv2.destroyAllWindows()