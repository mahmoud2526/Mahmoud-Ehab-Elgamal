import cv2
import sys
import numpy as np

s = 0
privew_mode = 0
blur = 1
features = 2
canny_edge_detection = 3

feature_params = dict(maxCorners=500, qualityLevel=0.2, minDistance=15, blockSize=9)

source = cv2.VideoCapture(s)
cv2.namedWindow("hello", cv2.WINDOW_NORMAL)
cv2.resizeWindow("hello", 500, 500)

new_width = 1280
new_height = 720
image_filter = privew_mode
result = None

while cv2.waitKey(1) != 27:
    has, frame = source.read()
    if not has:
        break

    new = cv2.flip(frame, 1)
    if image_filter == privew_mode:
        result = frame
    elif image_filter == canny_edge_detection:
        result = cv2.Canny(frame, 60, 150)
    elif image_filter == blur:
        result = cv2.blur(frame, (13, 13))
    elif image_filter == features:
        result = frame.copy()  # Make a copy of the frame
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(frame_gray, **feature_params)
        if corners is not None:
            for corner in corners:
                x, y = corner.ravel()
                cv2.circle(result, (int(x), int(y)), 10, (0, 255, 0), 1)

    cv2.imshow("hello", result)

    key = cv2.waitKey(1)
    if key == ord("Q") or key == ord("q") or key == 27:
        break
    elif key == ord("C") or key == ord("c"):
        image_filter = canny_edge_detection
    elif key == ord("B") or key == ord("b"):
        image_filter = blur
    elif key == ord("F") or key == ord("f"):
        image_filter = features
    elif key == ord("P") or key == ord("p"):
        image_filter = privew_mode

source.release()
cv2.destroyAllWindows()
