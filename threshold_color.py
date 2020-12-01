import cv2
import numpy as np

cap =cv2.VideoCapture(0)
def empty(a):
    pass

###################
cv2.namedWindow("hsv")
cv2.createTrackbar("hue min", "hsv", 0, 179, empty)
cv2.createTrackbar("hue max", "hsv", 179, 179, empty)
cv2.createTrackbar("sat min", "hsv", 0, 255, empty)
cv2.createTrackbar("sat max", "hsv", 255, 255, empty)
cv2.createTrackbar("val min", "hsv", 0, 255, empty)
cv2.createTrackbar("val max", "hsv", 255, 255, empty)
##################3


while True:
    _, img = cap.read()
    imgh = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("hue min", "hsv")
    h_max = cv2.getTrackbarPos("hue max", "hsv")
    s_min = cv2.getTrackbarPos("sat min", "hsv")
    s_max = cv2.getTrackbarPos("sat max", "hsv")
    v_min = cv2.getTrackbarPos("val min", "hsv")
    v_max = cv2.getTrackbarPos("val max", "hsv")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgh, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hstack = np.hstack([img, mask, result])
    cv2.imshow("image", hstack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    


