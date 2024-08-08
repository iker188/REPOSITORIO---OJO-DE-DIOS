import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


try:
    
    cap = cv2.VideoCapture(0) 
    if not cap.isOpened():
        raise IOError("No se pudo abrir la cámara.")

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        
        cv2.imshow('img', img)
        
        
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break

    
    cap.release()
    cv2.destroyAllWindows()

except IOError as e:
    print(e)

except KeyboardInterrupt:
    
    cap.release()
    cv2.destroyAllWindows()

except Exception as e:
    print("Se produjo un error:", e)
    cap.release()
    cv2.destroyAllWindows()