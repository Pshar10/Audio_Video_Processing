import pyaudio
import wave
import numpy as np
from scipy.fft import fft
import scipy.signal
from ctypes import *
import getch
import scipy
import scipy.fftpack
from matplotlib import pyplot as plt
import scipy.io.wavfile as wavfile
import scipy
import getch
import numpy as np
import cv2
import time

#importing from the scripts.......
from Upsampling import upsample as u
from Quantization import quantization as q
from filter import show_filter as s
from Img_Video import VideoProcessing as v
from pk import Pickle_Processing as p


# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 32000  # "RATE" is the number of samples collected per second.

# CHUNK = 512  #"CHUNK" is the  number of frames the (signals are split 
# RECORD_SECONDS = 5

# WAVE_OUTPUT_FILENAME = "file.wav"
 
# audio = pyaudio.PyAudio()

# print("Please press space to Record your sound")


# char = None
# #print(char)
# while(char != ord(' ')):
    
#     char = getch.getch()
#     char = ord(char)
 
# # start Recording
# stream = audio.open(format=FORMAT, channels=CHANNELS,
#                 rate=RATE, input=True,
#                 frames_per_buffer=CHUNK)
# print ("recording...")
# frames = []
 
# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)



# # stop Recording
# print ("finished recording \n\n\n\n\n")
# stream.stop_stream()
# stream.close()
# audio.terminate()

# waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# waveFile.setnchannels(CHANNELS)
# waveFile.setsampwidth(audio.get_sample_size(FORMAT))
# waveFile.setframerate(RATE)
# waveFile.writeframes(b''.join(frames))
# waveFile.close()

fs, x = wavfile.read("file.wav")

char = None
while(char != ord(' ')):
    print("\n\n*********************************************Welcome to the Audio/Video Processing Segment*****************************************************\n\nFor UPSAMPLING: Press u\n\nFor Showing FILTERED Response: Press s\n\nFor QUANTIZATION/DE-QUANTIZATION: Press q\n\nPress v for Image/Video Processing Options\n\nPress p for Pickle Segment\n\nPress space to quit\n\n\n\n")


    while((char != ord('u')) and (char != ord(' ')) and (char != ord('p')) and (char != ord('q')) and (char != ord('s') and (char != ord('v')))): 
        char = getch.getch()
        char = ord(char)

    if char == ord('u'):
        n= u.upsample(fs,x)
        char= None

    if char == ord('q'):    
        q.quantization(fs,x)
        char= None

    if char == ord('s'):    
        s.show_filter(fs,x,n)
        char= None
    
    if char == ord('v'):   
        v.Process()
        char=None

    if char == ord('p'):   
        p.process()
        char=None
    