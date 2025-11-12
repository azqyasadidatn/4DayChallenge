import cv2
import os

windowName = "Camera Azqya"
camera = cv2.VideoCapture(0)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

count = 0
fileName = r"D:\Azqya Old Code 2\PY and NumPy\30 Day Plylist\Percobaan Vision\DAATA"
os.makedirs(fileName, exist_ok=True)

while True:
    success,frame = camera.read()
    if not success :
        break

    cv2.imshow(windowName, frame)

    key = cv2.waitKey(1) & 0xFF 

    if  key == ord('q'):
       break
    if cv2.getWindowProperty(windowName,cv2.WND_PROP_VISIBLE) <1 :
        break
    elif key == ord('c'):
        # filename = f"D:\Azqya Old Code 2\PY and NumPy\30 Day Plylist\Percobaan Vision\DAATA{count}.jpg"
        filename = os.path.join(fileName, f"Azqya{count}.jpg") 
        cv2.imwrite(filename, frame)
        print(f"[INFO] Gambar tersimpan: {filename}")
        count += 1


camera.release()
cv2.destroyAllWindows()