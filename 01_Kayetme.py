import cv2
import numpy as np

resim = cv2.imread("eren.jpg",0)
cv2.imshow("eren",resim)
a = cv2.waitKey(0)

if a == 27:
    cv2.destroyAllWindows()
elif a == ord("s"):
    cv2.imwrite("erenButSad.jpg",resim)
    