#python FormulasWavelet.py
import math
import numpy as np
from matplotlib import pyplot as plt


def FNysquistForBits (FrequenciaHzs,NiveisBits):
    value = int(2*FrequenciaHzs*math.log(NiveisBits, 2))   
    print("Frequencia de %i Hzs com %i Niveis"%(FrequenciaHzs,NiveisBits))
    print("Amostragem Minima de %i bits por segundo"%(value))
    return(value)

def MexicanHat (tempo,dilat,posic):
    inputFourier = ((tempo-posic)/dilat)
    return (1-inputFourier**2)*math.e**((inputFourier**2/2)*-1)
    
def hermitianHat (tempo,dilat,posic):
    inputFourier = ((tempo-posic)/dilat)
    return 2/(5**2)*math.pi**-(1/4)*inputFourier*(1+inputFourier)*math.e**((-1/2)*inputFourier**2)

def find_gcd(NumpyArray):
    def gcd(x, y): 
        while y > 0: 
            x, y = y, x % y
        return x
    Ngcd = NumpyArray[0]
    for i in range(1, len(NumpyArray)): 
        Ngcd = gcd(Ngcd, NumpyArray[i])
    return Ngcd
      
def find_lcm(NumpyArray):
    def gcd(x, y): 
        while y > 0: 
            x, y = y, x % y
        return x
    def lcm(x, y):
        return x * y / gcd(x, y) 
    Nlcm = NumpyArray[0]

    for i in range(1, len(NumpyArray)): 
        Nlcm = lcm(Nlcm, NumpyArray[i])
    return Nlcm

def GraficoWaveLet(tempo, sinal):
    plt.figure()
    plt.ylabel("Amplitude")
    plt.xlabel("Time [s]")
    plt.plot(tempo, sinal)
    plt.show()


def FourierAnalise(tempo, sinal):
    fft = np.fft.fft(sinal)
    T = t[1] - t[0]  # sampling interval 
    N = sinal.size

    # 1/T = frequency
    f = np.linspace(0, 1 / T, N)
    return [f[:N // 2], 2*np.abs(fft)[:N // 2] * 1 / N, width=1.5]

def FourierAnaliseGraph(FourierAnalise):
    plt.figure()
    plt.ylabel("Amplitude")
    plt.xlabel("Frequency [Hz]")
    plt.bar()  # 1 / N is a normalization factor
    plt.show()





