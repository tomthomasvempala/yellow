from PIL import Image
import cv2 as cv

from read_cam import take_pic
from skin_mask import mask_skin

def yellow_intensity(r,g,b):
    rg_closeness = 10
    b_gap = 10
    rg_height = 10
    if abs(r-g) < 50 :
        rg_closeness = 10
    elif abs(r-g) < 100:
        rg_closeness = 8
    elif abs(r-g) < 150:
        rg_closeness = 3
    else:
        rg_closeness = 1

    b_diff = abs(b - (r+g)/2)
    if b_diff > 200:
        b_gap = 10
    elif b_diff > 180:
        b_gap = 8
    elif b_diff > 150:
        b_gap = 6
    elif b_diff > 120:
        b_gap = 4
    elif b_diff > 100:
        b_gap = 3
    else:
        b_gap=1

    rg_avg = (r+g)/2
    if rg_avg > 210:
        rg_height = 10 
    elif rg_avg >150:
        rg_avg = 6
    elif rg_avg >100:
        rg_avg = 3
    else:
        rg_avg=1
    return ((rg_closeness * rg_height * b_gap) / 1000)



def yellow_content(im,x,y):
    coordinate = x, y
    rgb = im.getpixel(coordinate)
    if rgb == (0,0,0):
        return -1
    yellow= (yellow_intensity(rgb[0],rgb[1],rgb[2]))
    return yellow*100

def average_yellow(img_name, marks = False):
    sum =0
    count = 0
    im = Image.open(r""+img_name)
    x = im.width
    y = im.height
    for i in range(0,x,5):
        for j in range(0,y,5):  
            x = yellow_content(im,i,j)
            if x==-1:
                continue
            if marks:
                for p in range(i-1, i+2):  
                    for q in range(j-1, j+2):
                        if not (p==i and q==j):
                            im.putpixel((p, q), (255, 0, 0))
            sum=sum+x
            count=count+1
    if marks:
        im.save("workspace/marks.png")
    if count == 0:
        print("No skin found")
        return 0
    avg = sum/count
    if marks:
        print("Pixels considered: "+ str(count))
    return avg
