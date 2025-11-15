import cv2
import os
import time

windowName = "Camera"
camera = cv2.VideoCapture(1)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)

count = 0
lastCapture = 0
Captur_Deelay = 0.7

auto_capture = False
fileName = r"D:\Azqya Old Code 2\PY and NumPy\30 Day Plylist\Percobaan Vision\DAATA" #path foldernyan nya
os.makedirs(fileName, exist_ok=True)

def Capture(frame):
        global count, lastCapture
        currentTime = time.time()
        if currentTime - lastCapture >= Captur_Deelay:
            filename = os.path.join(fileName, f"Azqya{count}.jpg") 
            cv2.imwrite(filename, frame)
            print(f"Holaa O_o Gambar tersimpan: {filename}")
            count += 1
            lastCapture = currentTime

while True:
    success,frame = camera.read()
    if not success :
        break

    frame = cv2.flip(frame,1)
    cv2.imshow(windowName, frame)

    
    key = cv2.waitKey(1) & 0xFF 

    if  key == ord('q'):
       break
    if cv2.getWindowProperty(windowName,cv2.WND_PROP_VISIBLE) <1 :
        break
    if auto_capture:
        Capture(frame)
        
    if key == ord('c'):
       auto_capture = True
       print(f"X for stop")
    elif key == ord("x"):
        auto_capture= False
        print("Bay bayy ...")
    
    


camera.release()
cv2.destroyAllWindows()