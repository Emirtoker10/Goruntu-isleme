import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    
    success,img = cap.read()
    
    if success:
        # resmi içe aktar
        """
        img = cv2.imread("london.jpg",0)
        plt.figure(),plt.imshow(img,cmap="gray"),plt.axis("off"),plt.title("asıl görüntü")
        """
        # kenar algılamayı filtreleme
        edges = cv2.Canny(image = img , threshold1 = 0 , threshold2 = 255)
        
        med_val = np.median(img)
        print(med_val)
        
        low = int(max(0,(1 - 0.33)*med_val))
        high = int(min(255,(1 + 0.33)*med_val))
        
        print(low)
        print(high)
        
        # mediana göre flitreleme
        edges = cv2.Canny(image = img , threshold1 = low , threshold2 = high)
        
        # blurlama
        blurred_img = cv2.blur(img,ksize = (5,5))
        
        med_val = np.median(blurred_img)
        print(med_val)
        
        low = int(max(0,(1 - 0.33)*med_val))
        high = int(min(255,(1 + 0.33)*med_val))
        
        print(low)
        print(high)
        
        edges = cv2.Canny(image = blurred_img , threshold1 = low , threshold2 = high)
        cv2.imshow(":)",edges)
