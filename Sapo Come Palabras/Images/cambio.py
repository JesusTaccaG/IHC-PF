import glob
import cv2
path = glob.glob("Fondos/*.jpg")
cv_img = []
for img in path:
    n = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    n = cv2.resize(n, (640,480), interpolation = cv2.INTER_AREA)
    cv2.imwrite(img,n)