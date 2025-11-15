import cv2
from ultralytics import YOLO
import os
import time

model_path = r'D:\Azqya Old Code 2\PY and NumPy\30 Day Plylist\Day4\best.pt'

model= YOLO(model_path)
WINDOW_NAME = "Frame"
count = 0

fileName = r"D:\Azqya Old Code 2\PY and NumPy\30 Day Plylist\Day4\Data"
os.makedirs(fileName, exist_ok=True) 
Capture_Delay = 0.8
auto_capture = False
# time.sleep(2)

center_x = 720 // 2
center_y = 480 // 2
margin = 50 

camera =cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True :
    success,frame = camera.read()
    if not success :
        break
    frame = cv2.flip(frame,1)
    result = model (frame, stream= True)

    anotade_frame_ist = list(result)

    if len(anotade_frame_ist) == 0:
        anotade_frame = frame
    else:
        anotade_frame = anotade_frame_ist[0].plot()

 
    for r in result:
        boxes = r.boxes
        if not boxes:
            continue
    
    cv2.imshow(WINDOW_NAME, anotade_frame)

    ''' otomatis capture  '''

    def Capture(frame):
        global count, lastCapture
        currentTime = time.time()
        if currentTime - lastCapture >= Capture_Delay:
            filename = os.path.join(fileName, f"Azqya{count}.jpg") 
            cv2.imwrite(filename, frame)
            print(f"Holaa O_o Gambar tersimpan: {filename}")
            count += 1
            lastCapture = currentTime

    ''' close '''
    key = cv2.waitKey(1) & 0xFF 

    if  key == ord('q'):
       break
    if cv2.getWindowProperty(WINDOW_NAME,cv2.WND_PROP_VISIBLE) <1 :
        break

    if key == ord('c'):
       auto_capture = True
       print(f"X for stop")
    elif key == ord("x"):
        auto_capture= False
        print("Bay bayy ...")
    if auto_capture:
        Capture(frame)


camera.release()
cv2.destroyAllWindows()