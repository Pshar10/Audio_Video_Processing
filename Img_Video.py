
from cv2 import data
import numpy as np
import cv2
import pickle
import getch
import time
char =None



def Y_component(frame):
    Y=(0.114*frame[:,:,0]+0.587*frame[:,:,1]+0.299*frame[:,:,2])/255
    # f = open('Captured_Y.bin', 'wb')
    # pickle.dump(Y, f)       
    # f.close() 

    return Y

def Cb_component(frame):
    Cb=(0.437*frame[:,:,0]-0.289*frame[:,:,1]-0.147*frame[:,:,2])/255  
    # f = open('Captured_Cb.bin', 'wb')
    # pickle.dump(Cb, f)      
    # f.close() 

    return Cb

def Cr_component(frame):
    Cr=(-0.100*frame[:,:,0]-0.515*frame[:,:,1]+0.615*frame[:,:,2])/255
    # f = open('Captured_Cr.bin', 'wb')
    # pickle.dump(Cr, f)      
    # f.close() 

    return Cr

def Reconstructed_component(frame,Y,Cb,Cr):
    framerec=np.zeros(frame.shape)
    Y=Y
    U=Cb
    V=Cr

# Reforming the frame
    R = 1.00*Y + 0.00*U + 1.403*V
    G = 1.00*Y - 0.344*U - 0.714*V
    B = 1.00*Y + 1.773*U + 0000*V


    framerec[:,:,0]=B
    framerec[:,:,1]=G
    framerec[:,:,2]=R
    return framerec



class VideoProcessing(object):
    
    def Process():
        char =None
        while(char != ord(' ')):
            print("\nWelcome to the Image/Video options\n\n")
            print("Press i for Image Processing \n\nv for Video Processing \n\nr for Video Recording\n\np for Playing \n\nPress Space to quit")
            while((char != ord('i')) and (char != ord('v')) and (char != ord('r')) and (char != ord('p'))  and (char != ord(' '))):
                char = getch.getch()
                char = ord(char)

                if char == ord('v'):
                    cap = cv2.VideoCapture(0)
                    capture_duration = 15
                    start_time = time.time()
                    while(int(time.time() - start_time) < capture_duration):
                        # Capture frame-by-frame
                        [ret, frame] = cap.read()
                        # Display the original frame
                        cv2.imshow('Original',frame)
                        Y = Y_component(frame)
                        Cb = Cb_component(frame)
                        Cr = Cr_component(frame)
                        #Reconstructinf the BGR
                        framerec3 = Reconstructed_component(frame,Y,Cb,Cr)
                        cv2.imshow('Y_component',Y)    
                        cv2.imshow('Cb_component',Cb)    
                        cv2.imshow('Cr_component',Cr)    
                        cv2.imshow('Reconstructed_component',framerec3)    
                        key=cv2.waitKey(1) & 0xFF
                        if key == ord('q'):
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    char = None

                if char == ord('i'):
                    start_time = time.time()
                    while( int(time.time() - start_time) < 5 ):
                        image = cv2.imread("i.jpg")
                        img=Y_component(image)
                        cv2.imshow("Original Image",image)
                        cv2.imshow("Grayscale Image", img)
                        if cv2.waitKey(25) == ord('q'):
                            break
                        
                    cv2.destroyAllWindows()
                    char=None


                if char == ord('r'):
                    capture_duration = 5
                    cap = cv2.VideoCapture(0)
                    # Define the codec and create VideoWriter object
                    fourcc = cv2.VideoWriter_fourcc(*'XVID')
                    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
                    start_time = time.time()
                    while( int(time.time() - start_time) < capture_duration ):
                        ret, frame = cap.read()
                        out.write(frame)
                        cv2.imshow('frame', frame)
                        if cv2.waitKey(10) == ord('q'):
                            break
                    # Release everything if job is finished
                    cap.release()
                    out.release()
                    cv2.destroyAllWindows()
                    char=None

                if char == ord('p'):

                    cap = cv2.VideoCapture('output.avi')
                    capture_duration = 4
                    start_time = time.time()
                    while(int(time.time() - start_time) < capture_duration):
                        ret, frame = cap.read()
                        cv2.imshow('frame', frame)
                        if cv2.waitKey(100) == ord('q'):
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    char=None