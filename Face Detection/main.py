import cv2

face_ref = cv2.CascadeClassifier("face_ref.xml")
camera = cv2.VideoCapture(0)

def face_detection(frame):
    # harus punya frame dari setiap kameranya
    #kirim ke sini dari kamera
    optimaized_frame = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    faces = face_ref.detectMultiScale( optimaized_frame,scaleFactor=1.1, minSize=(100,20), minNeighbors= 3)
    return faces
    


def drawer_box(frame):
    for x,y,w,h  in face_detection(frame) :
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255),4)
# di rekomendasikan frame nya hitamputih dulu biar lebh ringan dan mudah


def close_window():
   camera.release()
   cv2.destroyAllWindows()
   exit()

def main():
  while True :
    success,frame = camera.read()
    if not success or frame is None:
       print("tidak terbaca")
       break
    # blr_size = 7  
    # blurvid = cv2.blur(frame,(blr_size,blr_size) )
    drawer_box(frame)
    cv2.imshow("Cy Face Detection",frame )
    
    
    if cv2.waitKey(1) & 0xFF == ord('q') :
        close_window()
    

if __name__ == '__main__':
    main()