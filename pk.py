import numpy as np
import cv2
import pickle   #for python3
import time




class Pickle_Processing(object):
    def process():
        char =None
        cap = cv2.VideoCapture(0)

        f_Y=open('Y.bin', 'wb')
        f_Cb=open('Cb.bin', 'wb')
        f_Cr=open('Cr.bin', 'wb')

        #Process 30 frames:

        capture_duration = 5
        start_time = time.time()
        while(int(time.time() - start_time) < capture_duration):

            ret, frame = cap.read()
            
            if ret==True:
                #show captured frame:
                cv2.imshow('frame',frame)
                Y=(0.114*frame[:,:,0]+0.587*frame[:,:,1]+0.299*frame[:,:,2])/255
                Cb=(0.437*frame[:,:,0]-0.289*frame[:,:,1]-0.147*frame[:,:,2])/255
                Cr=(-0.100*frame[:,:,0]-0.515*frame[:,:,1]+0.615*frame[:,:,2])/255


                pickle.dump(Y,f_Y)
                pickle.dump(Cb,f_Cb)
                pickle.dump(Cr,f_Cr)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        # Release everything if job is finished
        cap.release()
        f_Y.close()
        f_Cb.close()
        f_Cr.close()

        cv2.destroyAllWindows()

        while(True):
            opt = input("Wlcome to the Pickle Operation\n\nFor Playing Y.bin press 1 \n\nFor Playing Cb.bin press 2\n\nFor Playing Cr.bin press 3\n\nTo quit press 4")

            opt = int(opt)


            if opt ==1:

                try:
                    f_Y=open('Y.bin', 'rb')
                    while(True):
                    #load next frame from file f and "de-pickle" it, convert from a string back to matrix or tensor:
                        reduced_Y = pickle.load(f_Y)
                        # reduced_Cb = pickle.load(f_Cb)
                        # reduced_Cr = pickle.load(f_Cr)

                        #here goes the decoding:
                        framedec_Y=reduced_Y.copy() 
                        # framedec_Cb=reduced_Cb.copy() 
                        # framedec_Cr=reduced_Cr.copy() 

                        cv2.imshow('Video',framedec_Y)
                        # cv2.imshow('Video',framedec_Cb)
                        # cv2.imshow('Video',framedec_Cr)
                        #Wait for key for 50ms, to get about 20 frames per second playback 
                        #(depends also on speed of the machine, and recording frame rate, try out):
                        if cv2.waitKey(60) & 0xFF == ord('q'):
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    # Release everything if job is finished
                    f_Y.close()
                    # f_Cb.close()
                    # f_Cr.close()
                except EOFError:
                    {}

            if opt ==2:

                try:
                    f_Cb=open('Cb.bin', 'rb')
                    while(True):
                    #load next frame from file f and "de-pickle" it, convert from a string back to matrix or tensor:
                        # reduced_Y = pickle.load(f_Y)
                        reduced_Cb = pickle.load(f_Cb)
                        # reduced_Cr = pickle.load(f_Cr)

                        #here goes the decoding:
                        # framedec_Y=reduced_Y.copy() 
                        framedec_Cb=reduced_Cb.copy() 
                        # framedec_Cr=reduced_Cr.copy() 

                        # cv2.imshow('Video',framedec_Y)
                        cv2.imshow('Video',framedec_Cb)
                        # cv2.imshow('Video',framedec_Cr)
                        #Wait for key for 50ms, to get about 20 frames per second playback 
                        #(depends also on speed of the machine, and recording frame rate, try out):
                        if cv2.waitKey(60) & 0xFF == ord('q'):
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    # Release everything if job is finished
                    # f_Y.close()
                    f_Cb.close()
                    # f_Cr.close()
                except EOFError:
                    {}

            if opt == 3:
                try:
                    f_Cr=open('Cr.bin', 'rb')
                    while(True):
                    #load next frame from file f and "de-pickle" it, convert from a string back to matrix or tensor:
                        # reduced_Y = pickle.load(f_Y)
                        # reduced_Cb = pickle.load(f_Cb)
                        reduced_Cr = pickle.load(f_Cr)

                        #here goes the decoding:
                        # framedec_Y=reduced_Y.copy() 
                        # framedec_Cb=reduced_Cb.copy() 
                        framedec_Cr=reduced_Cr.copy() 

                        # cv2.imshow('Video',framedec_Y)
                        # cv2.imshow('Video',framedec_Cb)
                        cv2.imshow('Video',framedec_Cr)
                        #Wait for key for 50ms, to get about 20 frames per second playback 
                        #(depends also on speed of the machine, and recording frame rate, try out):
                        if cv2.waitKey(60) & 0xFF == ord('q'):
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    # Release everything if job is finished
                    # f_Y.close()
                    # f_Cb.close()
                    f_Cr.close()
                except EOFError:
                    {}

            if opt==4:
                break