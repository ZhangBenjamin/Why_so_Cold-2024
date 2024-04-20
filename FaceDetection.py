import cv2
import time
import numpy as np

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
@@ -25,32 +24,20 @@
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Variable to check if all faces are smiling
    all_smiling = True

    # For each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

        # If no smile is detected in a face, set all_smiling to False
        if len(smiles) == 0:
            all_smiling = False
        else:
            # Draw the rectangle around each face and smile
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)

    # If all faces are smiling and at least 1 second has passed since the last picture
    if all_smiling and time.time() - last_pic_time >= 1:
        smile_frame_counter += 1
        # Save a copy of the frame without rectangles
        img_no_rect = np.copy(img)
        cv2.imwrite(f'smile_frame_{smile_frame_counter}.jpg', img_no_rect)
        print(f'Smile detected in all faces! Picture taken and saved as smile_frame_{smile_frame_counter}.jpg')
        last_pic_time = time.time()
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
            if time.time() - last_pic_time >= 1:  # At least 1 second since last picture
                smile_frame_counter += 1
                cv2.imwrite(f'smile_frame_{smile_frame_counter}.jpg', img)
                print(f'Smile detected! Picture taken and saved as smile_frame_{smile_frame_counter}.jpg')
                last_pic_time = time.time()

    # Display
    cv2.imshow('img', img)
