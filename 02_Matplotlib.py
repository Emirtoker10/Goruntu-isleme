import cv2
from matplotlib import pyplot as plt


resim = cv2.imread("eren.jpg",0)

cv2.imshow("resim penceresi",resim)

plt.imshow(resim,cmap="gray")

cv2.waitKey()
cv2.destroyAllWindows()


