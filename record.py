import numpy as np
import numpy as np
import cv2 as cv
import time


capture_duration = 5
cap = cv.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc('M','J','P','G')
out = cv.VideoWriter('output.avi', fourcc, 30.0, (640,  480))

start_time = time.time()

while( int(time.time() - start_time) < capture_duration ):
    ret, frame = cap.read()
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(2) == ord('q'):
        break    

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()

cap = cv.VideoCapture('output.avi')
while cap.isOpened():
    ret, frame = cap.read()
    cv.imshow('frame', frame)
    if cv.waitKey(100) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()



# CV_FOURCC('P','I','M','1')    = MPEG-1 codec

# CV_FOURCC('M','J','P','G')    = motion-jpeg codec (does not work well)

# CV_FOURCC('M', 'P', '4', '2') = MPEG-4.2 codec

# CV_FOURCC('D', 'I', 'V', '3') = MPEG-4.3 codec

# CV_FOURCC('D', 'I', 'V', 'X') = MPEG-4 codec

# CV_FOURCC('U', '2', '6', '3') = H263 codec

# CV_FOURCC('I', '2', '6', '3') = H263I codec

# CV_FOURCC('F', 'L', 'V', '1') = FLV1 codec