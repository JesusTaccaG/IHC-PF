import glob
import cv2
image1 = cv2.imread('Recursos/circulo_1.png', cv2.IMREAD_UNCHANGED)
image2 = cv2.imread('Recursos/circulo_2.png', cv2.IMREAD_UNCHANGED)
m, n, sh = image1.shape
image3=cv2.resize(image1, (m*2,n*2), interpolation = cv2.INTER_AREA)
image4=cv2.resize(image2, (m*2,n*2), interpolation = cv2.INTER_AREA)
cv2.imwrite('circulo_1.png',image3)
cv2.imwrite('circulo_2.png',image4)