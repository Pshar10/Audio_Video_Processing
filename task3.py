import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def Y_component(frame):
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

def Cb_component(frame):
    framerec=np.zeros(frame.shape)
    Y=(0.114*frame[:,:,0]+0.587*frame[:,:,1]+0.299*frame[:,:,2])/255
    U=frame[:,:,0]/255.0-Y
    V=frame[:,:,2]/255.0-Y
    Y=np.ones(Y.shape)*0.5
    # U=np.zeros(U.shape)
    B=U+Y
    R=V+Y
    G=(Y-0.114*B-0.299*R)/0.587
    framerec[:,:,0]=B
    framerec[:,:,1]=G
    framerec[:,:,2]=R
    return framerec

def Cr_component(frame):
    framerec=np.zeros(frame.shape)
    Y=(0.114*frame[:,:,0]+0.587*frame[:,:,1]+0.299*frame[:,:,2])/255
    U=frame[:,:,0]/255.0-Y
    V=frame[:,:,2]/255.0-Y
    U=np.zeros(U.shape)
    Y=np.ones(Y.shape)*0.5
    # V=np.zeros(V.shape)
    B=U+Y
    R=V+Y
    G=(Y-0.114*B-0.299*R)/0.587
    framerec[:,:,0]=B
    framerec[:,:,1]=G
    framerec[:,:,2]=R
    return framerec

def Reconstructed_component(frame):
    framerec=np.zeros(frame.shape)
    Y=(0.114*frame[:,:,0]+0.587*frame[:,:,1]+0.299*frame[:,:,2])/255
    U=frame[:,:,0]/255.0-Y
    V=frame[:,:,2]/255.0-Y

# Reforming the frame

    B=U+Y
    R=V+Y
    G=(Y-0.114*B-0.299*R)/0.587
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
        cv2.imshow('Original_RGB',frame)
        # Display the original frame
        framerec = Y_component(frame)
        framerec1 = Cb_component(frame)
        framerec2 = Cr_component(frame)
        framerec3 = Reconstructed_component(frame)
        cv2.imshow('Y_component',framerec)
        cv2.imshow('Cb_component',framerec1)      
        cv2.imshow('Cr_component',framerec2)    
        cv2.imshow('Reconstructed_component',framerec3)    
        key=cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

else:

    image = cv2.imread("i.jpg")
    img=Y_component(image)
    cv2.imshow("Original Image",image)
    cv2.imshow("Grayscale Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


