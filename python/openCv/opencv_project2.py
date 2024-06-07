import cv2

source = 'race_car.mp4'  # source = 0 for webcam

cap = cv2.VideoCapture(source)
cv2.namedWindow("hello", cv2.WINDOW_NORMAL)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out_mp4 = cv2.VideoWriter("race_car_out.mp4", cv2.VideoWriter_fourcc(*"MJPG"), 10, (frame_width, frame_height))

while cv2.waitKey(1) != 27:
    has, frame = cap.read()
    if not has:
        break
    frame = cv2.flip(frame, 1)
    cv2.imshow("hello", frame)

    # Write the frame to the output file
    out_mp4.write(frame)

# Release video capture and writer
cap.release()
out_mp4.release()

# Close all windows
cv2.destroyAllWindows()
