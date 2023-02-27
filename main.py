import os

from read_cam import take_pic
from skin_mask import mask_skin
from yellow import average_yellow

wk = 'workspace/'

low = []
normal = []
high = []

for filename in os.listdir('images'): 
    mask_skin('images/'+filename,wk+'skin.jpg')
    value = average_yellow(wk+"skin.jpg")
    key = filename
    if value<=10:
        normal.append((key,value))
    elif value <=20:
        low.append((key,value))
    else:
        high.append((key,value))

print("Given Data set\n")

print("\nNORMAL")
for img in normal:
    print(img)

print("\nLOW")
for img in low:
    print(img)


print("\nHIGH")
for img in high:
    print(img)

take_pic(wk+'cam.png')
mask_skin(wk+'cam.png',wk+"input_image.png")


print("\n\nCurrent sample is:")

value = average_yellow(wk+"input_image.png",True)
if value ==0:
    exit()
if value<=10:
    print("NORMAL")
elif value<=20:
    print("LOW")
else:
    print("HIGH")
print("with yellow content :"+ str(value))
