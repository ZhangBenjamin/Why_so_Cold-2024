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

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # For each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 25)

        # Only consider it a smile if there are more than 5 detected regions
        if len(smiles) > 5:
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
                if time.time() - last_pic_time >= 1:  # At least 1 second since last picture
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
