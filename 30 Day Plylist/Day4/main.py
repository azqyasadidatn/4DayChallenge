import cv2
from ultralytics import YOLO
model_path = r'D:\Azqya Old Code 2\PY and NumPy\30 Day Plylist\Day4\best.pt'

model= YOLO(model_path)
WINDOW_NAME = "Frame"

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
    
    if cv2.waitKey(1) & 0xFF == ord('q') :
       break
    if cv2.getWindowProperty(WINDOW_NAME,cv2.WND_PROP_VISIBLE) <1 :
        break

camera.release()
cv2.destroyAllWindows()