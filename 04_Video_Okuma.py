import cv2
import time

cap = cv2.VideoCapture("askım.mp4")

print("Genislik :",cap.get(3))
print("Yükseklik :",cap.get(4))

if cap.isOpened() == False:
    print("Hata")
    
while True:
    ret,frame = cap.read()
    
    if ret == True:
        time.sleep(0.05)
        cv2.imshow("Video", frame)
        
    else:
        break
            
    if cv2.waitKey(1) == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
    
