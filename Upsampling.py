import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack    
import numpy as np
from matplotlib import pyplot as plt
from playsound import playsound


class upsample(object):


    def upsample(fs_rate,signal):
        print ("Frequency sampling", fs_rate)
        l_audio = len(signal.shape)
        print ("Channels", l_audio)
        
        N = input("Enter your Upsampling Factor: ")
        n= int(N)
        a = len(signal)
        a = n*a
        upsample = np.zeros(a)
        upsample[::n] = signal
        print("Rate of original signal: ",len(signal),"and Rate of upsampled signal",len(upsample))

        FFT = abs(scipy.fft.fft(signal))#original
        freqs = scipy.fftpack.fftfreq(signal.size)#original

        FFTups = abs(scipy.fft.fft(upsample)) #upsampled
        freqsups = scipy.fftpack.fftfreq(upsample.size) #upsampled


        plt.subplot(411)
        p1 = plt.plot(upsample, "g" ,label="Upsampled Signal") # plotting the signal
        plt.ylabel('Amplitude')
        plt.legend(loc="upper left")

        plt.subplot(412)
        p2 = plt.plot(freqs, FFT, "r",label="Original Spectrum") # plotting the complete fft spectrum of original
        plt.xlabel('Normalised Frequency response of Original Signal (Hz)')
        plt.ylabel('Count dbl-sided')
        plt.legend(loc="upper left")

        plt.subplot(413)
        p3 = plt.plot(freqsups, FFTups, "r",label="Upsampled Spectrum") # plotting the complete fft spectrum of upsampled
        plt.xlabel('Normalised Frequency response of Upsampled Signal in (Hz)')
        plt.ylabel('Count dbl-sided')
        plt.legend(loc="upper left")

        plt.subplots_adjust(bottom=0.048, hspace=1)

        plt.show()

        fs_rate= fs_rate*2
        # wavfile.write("up.wav",fs_rate,upsample)
        # playsound("up.wav")
        return n