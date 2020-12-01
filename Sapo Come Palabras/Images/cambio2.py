import glob
import cv2
import numpy as np
img = cv2.imread('Button.png', cv2.IMREAD_UNCHANGED)
imgs=[]
a=400
b=972
c=185
d=9
print(img.shape)
for i in range(d):
    imgs.append(img[b:(b+c), a:(a+c)])
    b=b+c+33
a=1345
b=972
for i in range(d):
    imgs.append(img[b:(b+c), a:(a+c)])
    b=b+c+33
a=2351
b=101
d=13
for i in range(d):
    imgs.append(img[b:(b+c), a:(a+c)])
    b=b+c+33
a=3296
b=101
d=12
for i in range(d):
    imgs.append(img[b:(b+c), a:(a+c)])
    b=b+c+33
for i in range(len(imgs)):
    cv2.imwrite(str(i)+'.png',imgs[i])