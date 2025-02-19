import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    
    if success:
        # Görüntüyü griye çevir
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        gray = cv2.GaussianBlur(img, (5,5), 0)
        # Kenar algılama için uygun eşik değerlerini hesapla
        med_val = np.median(gray)
        low = int(max(0, (1 - 0.33) * med_val))
        high = int(min(255, (1 + 0.33) * med_val))
        
        # Kenar algılama işlemi
        edges = cv2.Canny(gray, threshold1=low, threshold2=high)
        
        # Sonucu göster
        cv2.imshow("Canny Edge Detection", edges)
    
    # Çıkış için 'q' tuşuna basılmasını bekle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
