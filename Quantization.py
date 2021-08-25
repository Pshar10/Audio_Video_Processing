from scipy.fft import fft 
import scipy.signal
from ctypes import *
import struct
import numpy as np
import getch
import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack
import numpy as np
from matplotlib import pyplot as plt
import wave
import pyaudio
from playsound import playsound
import sounddevice as sd
import soundfile as sf


class quantization(object):
    def quantization(fs_rate, signal):
        print(fs_rate)
        fs_original, original = wavfile.read("file.wav")


#start block-wise signal processing:

        N = input("Enter your Bit depth: ")
        N = int(N)
        stepsize=int((2**15-(-2**15))/(2**N))

        quant_rise_ind=np.floor(signal/stepsize)
        quant_tread_ind=np.round(signal/stepsize)

        quant_rise_rec=quant_rise_ind*stepsize+stepsize/2
        quant_tread_rec=quant_tread_ind*stepsize
        


        FFT_q = abs(scipy.fft.fft(quant_rise_rec))#q
        freqs_q = scipy.fftpack.fftfreq(quant_rise_rec.size)#q

        FFT = abs(scipy.fft.fft(original))#original
        freqs = scipy.fftpack.fftfreq(original.size)#original

        plt.plot(original, "b" , label="Original Signal")
        plt.plot(quant_rise_rec, "r",label="Quantised Signal")
        plt.legend(loc="upper left")
        plt.show()




        # wavfile.write("quant.wav",fs_rate,quant_rise_rec)
        # playsound("quant.wav")
        