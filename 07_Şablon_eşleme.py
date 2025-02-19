import cv2
import matplotlib.pyplot as plt

# template matching : şablon eşleme

img = cv2.imread("cat.jpg",0)
img = cv2.resize(img,(640,360))
cv2.imshow("resim",img)

template = cv2.imread("cat_template.jpg",0)
cv2.imshow("resim2",template)

h , w = template.shape

res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF)

min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)

bottom_right = (max_loc[0]+w, max_loc[1]+h)

cv2.rectangle(img,max_loc , bottom_right,255,2)


plt.figure()
plt.subplot(121),plt.imshow(res,cmap="gray")
plt.title("eşleşen sonuc"),plt.axis("off")
plt.subplot(122),plt.imshow(img,cmap="gray")
plt.title("tespit edilen sonuc"),plt.axis("off")
plt.suptitle("meth")
plt.show()











































