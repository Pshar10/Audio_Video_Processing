import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def my_weighted_gray(frame):
    framerec=np.zeros(frame.shape)
    Y=(0.114*frame[:,:,0]+0.587*frame[:,:,1]+0.299*frame[:,:,2])/255
    U=frame[:,:,0]/255.0-Y
    V=frame[:,:,2]/255.0-Y
    U=np.zeros(U.shape)
    V=np.zeros(V.shape)
    B=U+Y
    R=V+Y
    G=(Y-0.114*B-0.299*R)/0.587
    framerec[:,:,0]=B
    framerec[:,:,1]=G
    framerec[:,:,2]=R
    return framerec

def my_average_gray(frame):
    framerec=np.zeros(frame.shape)
    Y=((frame[:,:,0]+frame[:,:,1]+frame[:,:,2])/3)/255 
    U=frame[:,:,0]/255-Y
    V=frame[:,:,2]/255-Y
    U=np.zeros(U.shape)
    V=np.zeros(V.shape)
    B=U+Y
    R=V+Y
    G=(3*Y-B-R)
    framerec[:,:,0]=B
    framerec[:,:,1]=G
    framerec[:,:,2]=R
    return framerec




img = input("For image press 0 or for video press 1")

img = int(img)


if (img == 1) :

    while(True):
        # Capture frame-by-frame
        [ret, frame] = cap.read()
        # Display the original frame
        cv2.imshow('Original',frame)
        framerec = my_weighted_gray(frame)
        framerec1 = my_average_gray(frame)
        cv2.imshow('my_weighted_gray',framerec)
        cv2.imshow('my_average_gray',framerec1)      
        key=cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

else:

    image = cv2.imread("i.jpg")
    img=my_weighted_gray(image)
    cv2.imshow("Original Image",image)
    cv2.imshow("Grayscale Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


