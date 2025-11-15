import cv2
import subprocess
from ultralytics import YOLO

RTSP_URL = "rtsp://192.168.0.104:8554/mystream" # ip 192.168.0.104
WIDTH = 720
HEIGHT = 480

model_path = r'D:\Azqya Old Code 2\PY and NumPy\30 Day Plylist\Day4\best.pt'
model = YOLO(model_path)

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

ffmpeg_cmd = [
    r'C:\Users\ASUS\ffmpeg\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe',
    "-re",
    "-f", "rawvideo",
    "-pix_fmt", "bgr24",
    "-s", f"{WIDTH}x{HEIGHT}",
    "-i", "-",               
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-f", "rtsp",
    RTSP_URL
]

process = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)

print("⚡ Streaming dimulai... Tekan CTRL + C untuk stop.")

while True:
    ret, frame = cam.read()
    if not ret:
        break

    result = model(frame, stream=True)
    result_list = list(result)
    if len(result_list) == 0:
        annotated = frame
    else:
        annotated = result_list[0].plot()

    # ====== KIRIM FRAME KE FFMPEG ======
    process.stdin.write(annotated.tobytes())

cam.release()
process.stdin.close()
process.wait()

