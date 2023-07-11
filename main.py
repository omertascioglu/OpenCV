import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error opening video capture")
    exit()

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Camera", frame)

        # Capture photo when any key is pressed
        if cv2.waitKey(1) != -1:
            cv2.imwrite("photo.jpg", frame)
            print("Photo captured!")
            break

cap.release()
cv2.destroyAllWindows()