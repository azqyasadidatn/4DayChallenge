import numpy as np
import cv2

def get_limits(color):
    c = np.uint8([[color]])  # BGR
    hsvc = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    hue = int(hsvc[0][0][0])

    # kasih range lebih luas biar toleran sama cahaya
    lower_hue = max(hue - 20, 0)
    upper_hue = min(hue + 20, 179)

    lowerLimit = np.array([lower_hue, 100, 100], dtype=np.uint8)
    upperLimit = np.array([upper_hue, 255, 255], dtype=np.uint8)
    return lowerLimit, upperLimit
