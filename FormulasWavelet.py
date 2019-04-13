#python FormulasWavelet.py
import math
import numpy as np
from matplotlib import pyplot as plt
from plotly.offline import plot
import plotly.graph_objs as go

def FNysquistForBits (FrequenciaHzs,NiveisBits):
    value = int(2*FrequenciaHzs*math.log(NiveisBits, 2))   
    print("Frequencia de %i Hzs com %i Niveis"%(FrequenciaHzs,NiveisBits))
    print("Amostragem Minima de %i bits por segundo"%(value))
    return(value)

def MexicanHat (tempo,dilat,posic):
    inputFourier = ((tempo-posic)/dilat)
    return (1-inputFourier**2)*math.e**((inputFourier**2/2)*-1)
    
def HermitianHat (tempo,dilat,posic):
    inputFourier = ((tempo-posic)/dilat)
    return 2/(5**2)*math.pi**-(1/4)*inputFourier*(1+inputFourier)*math.e**((-1/2)*inputFourier**2)

def MeyerWavelet (tempo,dilat,posic):
    inputFourier = ((tempo-posic)/dilat)
    v = np.array([])
    outputArray = np.array([])
    for x in inputFourier:
        if x == 0:
            output = 2/3 + 4/(3*math.pi)
        else: 
            output = (np.sin(2*math.pi/3*x)+4/3*x*np.cos(4*math.pi/3*x))/(math.pi*x-(16*math.pi/9*x**3))
        outputArray = np.append(output, outputArray)
    return outputArray
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
    T = tempo[1] - tempo[0]  # sampling interval 
    N = sinal.size

    # 1/T = frequency
    f = np.linspace(0, 1 / T, N)
    return [f[:N // 2],2*np.abs(fft)[:N // 2] * 1 / N, 1.5]

def FourierAnaliseGraph(FourierAnalise):
    plt.figure()
    plt.ylabel("Amplitude")
    plt.xlabel("Frequency [Hz]")
    plt.bar(FourierAnalise[0],FourierAnalise[1], width=FourierAnalise[2])  # 1 / N is a normalization factor
    plt.show()

def plotly(tempo, sinal):
    trace = go.Scatter(
        y = sinal,
        x = tempo, 
        mode = 'lines+markers',
        line = dict(  color = "rgb(200, 0, 0)",
                  width = 4,
                  dash = 'dot'))

    layout = {
        "title": "Wavelets", 
        "xaxis": {
        "showgrid": False, 
        "title": "time"
    }, 
    "yaxis": {
        "showline": False, 
    "title": "Frequency"
        }
    }

    fig = go.Figure(data=[trace], layout=layout)

    plot(fig, filename= "Wavelet.html")




#   for x in inputFourier:
#         if x <= 0:
#             v = np.append(v, [0])
#         elif 0 < x and x <= 1:
#             v = np.append (v, [x])
#         elif 1 < x:
#             v = np.append (v, [1])
#         if 2*math.pi/3 < math.fabs(x) and math.fabs(x)<4*math.pi/3:
#             output = 1/((2*math.pi)**1/2)*np.sin(math.pi/2*v*((3*math.fabs(x)/(2*math.pi))-1))*math.e**1j*x/2
#             outputArray = np.append(outputArray, output) 
#         elif 4*math.pi/3 < math.fabs(x) and math.fabs(x)<8*math.pi/3:
#             output =  1/((2*math.pi)**1/2)*np.cos(math.pi/2*v*((3*math.fabs(x)/(4*math.pi))-1))*math.e**1j*x/2
#             outputArray = np.append(outputArray, output)
#         else:
#             outputArray = np.append(outputArray, 0)
#     return outputArray