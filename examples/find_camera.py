import cv2

for i in range(10):
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    ok = cap.isOpened()
    print(f"Index {i}: {'OK' if ok else 'Not available'}")

    if ok:
        ret, frame = cap.read()
        print(f"  Read frame: {'YES' if ret else 'NO'}")
    cap.release()