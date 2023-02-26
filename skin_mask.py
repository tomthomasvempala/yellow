import cv2
import numpy as np

def mask_skin(file_name,new_file):
    img = cv2.imread(file_name)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0, 20, 70])
    upper_skin = np.array([20, 255, 255])
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imwrite(new_file, result)
