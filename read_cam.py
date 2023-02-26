import cv2 as cv

def take_pic(file_name):
    cam_port = 0
    cam = cv.VideoCapture(cam_port)
    result, image = cam.read()

    if result:
        cv.imwrite(file_name, image)
    else:
        print("No image detected. Please! try again")