import cv2

cap = cv2.VideoCapture(0)   #0 means first webcam

if cap.isOpened():
    while True:
        state, frame = cap.read()
        if state:
            cv2.imshow("Vedio",frame)
            if cv2.waitKey(1) == 27:    # click on quit (or) if cv2.waitKey(1) == ord('c')
                break
    cap.release()
    cv2.destroyAllWindows()
else:
    print('Camera not working!!')

            