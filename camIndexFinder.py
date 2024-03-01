import cv2

for i in range(10):
    cap = cv2.VideoCapture(i)
    if not cap.isOpened():
        print(f"Index {i}: Camera not found")
    else:
        print(f"Index {i}: Camera found")
        cap.release()
