import cv2
import numpy as np


# Siyah resim
img = np.zeros((512,512,3))
cv2.imshow("Siyah",img)

# Çizgi
cv2.line(img, (0,0), (255,255), (255,0,0),5) # cv2.line( resim , baslangıc , bitis , renk BGR , kalınlık)
cv2.imshow("Cizgi Mavi",img)

# Dikdörtgen
cv2.rectangle(img, (0,0),(120,180),(0,255,0),cv2.FILLED) # cv2.line( resim , baslangıc , bitis , renk BGR , kalınlık)
cv2.imshow("Dikdortgen",img)

# Cember
cv2.circle(img, (256,256), 45,(0,0,255),cv2.FILLED) # cv2.line( resim , baslangıc , cap , renk BGR , kalınlık)
cv2.imshow("Cember",img)

# Metin
cv2.putText(img, "Kokoli", (10,490), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255)) # cv2.line( resim , baslangıc , font , büyüklük , renk BGR)
cv2.imshow("Metin",img)