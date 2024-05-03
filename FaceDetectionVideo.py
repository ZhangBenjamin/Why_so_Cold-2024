import cv2
import time

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# To capture video from webcam
cap = cv2.VideoCapture(0)

# Counter for the smile frames
smile_frame_counter = 0

# Time of last picture taken
last_pic_time = time.time()

# Timer for the countdown
timer = 0

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(10, 10))

    # For each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.9, minNeighbors=22)

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
            if time.time() - last_pic_time >= 1 and timer == 0:  # At least 1 second since last picture and timer is not running
                timer = 3  # Start the timer
            if timer > 0:
                cv2.putText(img, str(timer), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
                timer -= 1
                time.sleep(1)
            elif timer == 0:
                smile_frame_counter += 1
                cv2.imwrite(f'smile_frame_{smile_frame_counter}.jpg', img)
                print(f'Smile detected! Picture taken and saved as smile_frame_{smile_frame_counter}.jpg')
                last_pic_time = time.time()

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

# Release the VideoCapture object
cap.release()
