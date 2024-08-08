import cv2
import requests
import time
import os




api_url = "https://graph.facebook.com/v13.0/YOUR_PHONE_NUMBER_ID/messages"
access_token = "YOUR_ACCESS_TOKEN"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

if not os.path.exists('capturas'):
    os.makedirs('capturas')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
message_sent = False

while True:
    ret, img = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    if len(faces) > 0:
        if not message_sent:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f'capturas/captura_{timestamp}.jpg'
            cv2.imwrite(filename, img)

            image_url = "https://example.com/path/to/your/uploaded/image.jpg"

            data = {
                "messaging_product": "whatsapp",
                "to": "+1234567890",
                "type": "image",
                "image": {
                    "link": image_url
                }
            }
            response = requests.post(api_url, headers=headers, json=data)
            print(response.json())
            message_sent = True
    else:
        message_sent = False

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('img', img)
    
    k = cv2.waitKey(30)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()