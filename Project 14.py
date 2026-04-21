import cv2

cap = cv2.VideoCapture(0)

mode = "normal"

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if mode == "gray":
        processed = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    elif mode == "canny":
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        processed = cv2.Canny(gray, 100, 200)

    elif mode == "invert":
        processed = cv2.bitwise_not(frame)

    elif mode == "sepia":
        kernel = cv2.transform(frame, 
            [[0.272, 0.534, 0.131],
             [0.349, 0.686, 0.168],
             [0.393, 0.769, 0.189]])
        processed = kernel

    else:
        processed = frame

    cv2.imshow("Image Processing", processed)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('g'):
        mode = "gray"
    elif key == ord('c'):
        mode = "canny"
    elif key == ord('i'):
        mode = "invert"
    elif key == ord('s'):
        mode = "sepia"
    elif key == ord('n'):
        mode = "normal"
    elif key == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
