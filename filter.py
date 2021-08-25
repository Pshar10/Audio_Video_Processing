import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack    
import numpy as np
from matplotlib import pyplot as plt
from playsound import playsound


class show_filter(object):


    def show_filter(fs_rate,signal,n):

        [b,a]=scipy.signal.iirfilter(4, 1900/16000,rp=60,btype='lowpass')
        mem=np.zeros(4)
    # fs_rate, signal = wavfile.read("file.wav")
        print ("Frequency sampling", fs_rate)
        l_audio = len(signal.shape)
        print ("Channels", l_audio)
        a = len(signal)
        a = n*a
        upsample = np.zeros(a)
        # upsample = np.zeros(2*max(signal.shape))
        # print(len(upsample))
        upsample[::n] = signal

        [samples,mem]=scipy.signal.lfilter(b, a, upsample, zi=mem)

        print("Rate of original signal: ",len(signal),"and Rate of upsampled signal",len(upsample))

        FFT = abs(scipy.fft.fft(signal))#original
        freqs = scipy.fftpack.fftfreq(signal.size)#original

        FFTups = abs(scipy.fft.fft(upsample)) #upsampled
        freqsups = scipy.fftpack.fftfreq(upsample.size) #upsampled

        FFTsam = abs(scipy.fft.fft(samples)) #filtered
        freqssam = scipy.fftpack.fftfreq(samples.size) #filtered


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
        
        plt.subplot(414)
        p4 = plt.plot(freqssam, FFTsam, "r",label="Filtered Spectrum") # plotting the complete fft spectrum of filtered
        plt.xlabel('Normalised Frequency response of filtered Signal in (Hz)')
        plt.ylabel('Count dbl-sided')
        plt.legend(loc="upper left")

        plt.subplots_adjust(bottom=0.048, hspace=1)

        plt.show()

        