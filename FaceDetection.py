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

    # Variable to check if all faces are smiling
    all_smiling = True

    # For each face
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

        # If no smile is detected in a face, set all_smiling to False
        if len(smiles) == 0:
            all_smiling = False

    # If all faces are smiling and at least 1 second has passed since the last picture
    if all_smiling and time.time() - last_pic_time >= 1:
        smile_frame_counter += 1
        cv2.imwrite(f'smile_frame_{smile_frame_counter}.jpg', img)
        print(f'Smile detected in all faces! Picture taken and saved as smile_frame_{smile_frame_counter}.jpg')
        last_pic_time = time.time()

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

# Release the VideoCapture object
cap.release()
