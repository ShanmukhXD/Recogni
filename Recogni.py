import cv2 #Remember to run  pip install opencv-python  in Command Prompt to install Python's OpenCV package

def recogni():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam. Please make sure the camera is connected and accessible.")
        return

    # Load images of known persons & add more as needed
    person1_image = cv2.imread("Path to image file") #Replace "Path to image file" to your folder's path where images are stored for detection

    # Convert images to grayscale & add more as needed
    person1_gray = cv2.cvtColor(person1_image, cv2.COLOR_BGR2GRAY)

    # Create face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    known_faces = {
        "Person 1": person1_gray,
    }

    while True:
        ret, frame = cap.read()

        # Convert the frame to grayscale for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            face_roi = gray_frame[y:y + h, x:x + w]

            # Compare face with known faces
            for name, known_face in known_faces.items():
                result = cv2.matchTemplate(face_roi, known_face, cv2.TM_CCOEFF_NORMED)
                _, confidence, _, _ = cv2.minMaxLoc(result)

                if confidence > 0.8:  # Adjust the confidence threshold as needed
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (x + 6, y + h - 6), font, 0.5, (255, 255, 255), 1)


        cv2.imshow('Recogni', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        recogni()
    except Exception as e:
        print(f"An error occurred: {e}")
