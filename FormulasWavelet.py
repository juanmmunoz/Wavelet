#python FormulasWavelet.py
import math
import numpy as np
import scipy.integrate as integrate
from matplotlib import pyplot as plt
from plotly.offline import plot
import plotly.graph_objs as go

#Sinais Functions
def SinalBasico(Tempo, Frequencia, Amplitude):
    return Amplitude*np.sin(Frequencia*2*np.pi*Tempo) 

def HermitianHat (tempo,dilat,posic ):
    """Retornar um array das posições de uma OndaLet(Chápeu de Hermitian) em relação ao tempo
    
    Argumentos:
        tempo: um Numpy Array com os pontos do sinal que serão exibido
        dilat: O valor de dilatação da Wavelet
        posic: O valor da posição em relação ao tempo da Wavelet

    Retorno:
        Retorna um Array 2D com os valores de Amplitude em relação ao tempo."""

    inputFourier = ((tempo-posic)/dilat)
    return 2/(5**(1/2))*math.pi**-(1/4)*inputFourier*(1+inputFourier)*math.e**((-1/2)*inputFourier**2)

def MexicanHat (tempo,dilat,posic):
    """Retornar um array das posições de uma OndaLet(Chápeu de mexicano) em relação ao tempo
    
    Argumentos:
        tempo: um Numpy Array com os pontos do sinal que serão exibido
        dilat: O valor de dilatação da Wavelet
        posic: O valor da posição em relação ao tempo da Wavelet

    Retorno:
        Retorna um Array 2D com os valores de Amplitude em relação ao tempo."""
    inputFourier = ((tempo-posic)/dilat)
    return (1-inputFourier**2)*math.e**((inputFourier**2/2)*-1)
    
def MeyerWavelet (tempo,dilat,posic ):
    """Retornar um array das posições de uma OndaLet(Meyer) em relação ao tempo
    
    Argumentos:
        tempo: um Numpy Array com os pontos do sinal que serão exibido
        dilat: O valor de dilatação da Wavelet
        posic: O valor da posição em relação ao tempo da Wavelet

    Retorno:
        Retorna um Array 2D com os valores de Amplitude em relação ao tempo.
        
        Formando a imagem correta(provavelmente), mas com problemas no deslocamento do eixo do tempo, indo da direita pra esquerda"""

    inputFourier = ((tempo-posic)/dilat)
    outputArray = np.array([])
    for x in inputFourier:
        if x == 0:
            output = 2/3 + 4/(3*math.pi)
        else: 
            output = ((np.sin((2*math.pi)/(3)*x)+(4/3)*x*np.cos(((4*math.pi)/3)*x))/(math.pi*x-(16*math.pi/9)*(x**3)))
            output = output 
        outputArray = np.append(output, outputArray)
    return outputArray

#Gráficos

#    MatPlot
def WaveLetMatPlot(tempo, sinal):
    """Gera um gráfico em Matplotlib de linha feito para demonstração grafica de sinais
    Argumentos: 
        Tempo: Um numpy array com os valores do tempo
        Sinal: Um numpy Array com os valores do sinal em relação ao tempo
    Retorno:
        Exibe um Grafico
    
    """
    

    plt.figure()
    plt.ylabel("Amplitude")
    plt.xlabel("Time [s]")
    plt.plot(tempo, sinal)
    plt.show()

def FourierAnaliseGraph(FourierAnalise):
    """Gera um gráfico em Matplotlib de Barras feito para Analise de Fourier"""
    plt.figure()
    plt.ylabel("Amplitude")
    plt.xlabel("Frequency [Hz]")
    plt.bar(FourierAnalise[0],FourierAnalise[1], width=FourierAnalise[2])  # 1 / N is a normalization factor
    plt.show()

#   Plot.ly
def MakeAPlotlyScatter(sinal, tempo):
    return go.Scatter(
        y = sinal,
        x = tempo, 
        mode = 'lines+markers',
        line = dict(  color = "rgb(200, 0, 0)",
                  width = 4,
                  dash = 'dot'))

def WaveletPlotly(tempo, data, name):
    """Gera um gráfico em pyplot de linha feito para demonstração grafica de sinais
     Argumentos: 
        Tempo: Um numpy array com os valores do tempo
        Sinal: Um numpy Array com os valores do sinal em relação ao tempo
    Retorno:
        Salva um Grafico em html na pasta do arquivo"""

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

    fig = go.Figure(data=data, layout=layout)

    plot(fig, filename= name + ".html")


#Transformada de Sinais
def TransFourier(tempo, sinal):
    """Analisa as frequencias de um sinal a partir da transformada de fourier
    """
    fft = np.fft.fft(sinal)
    T = tempo[1] - tempo[0]  # sampling interval 
    N = sinal.size

    # 1/T = frequency
    f = np.linspace(0, 1 / T, N)
    return [f[:N // 2],2*np.abs(fft)[:N // 2] * 1 / N, 1.5]

def TransWaveletCont (tempo, RealSinal, dilatRange, WaveletFunction ):
    matrix = np.matrix([])
    for a in dilatRange:
        linha = np.array([])
        for b in tempo:
            WaveletSinal = WaveletFunction(tempo, a, b)
            WaveletTransform = integrate.simps(WaveletSinal*RealSinal, tempo)
            linha = np.append( (1/(a**1/2))*WaveletTransform, linha)
        print(100/dilatRange[-1]*a)
        matrix = np.append(linha, matrix)
    matrix = matrix.reshape(len(RealSinal), len(dilatRange))
    return matrix

#Outras
def find_gcd(NumpyArray):
    """Retorna o Maximo Divisor Comum de um Numpy Array"""
    def gcd(x, y): 
        while y > 0: 
            x, y = y, x % y
        return x
    Ngcd = NumpyArray[0]
    for i in range(1, len(NumpyArray)): 
        Ngcd = gcd(Ngcd, NumpyArray[i])
    return Ngcd
      
def find_lcm(NumpyArray):
    """Retorna o Minimo Multiplo Comum de um Numpy Array"""
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

def FNysquistForBits (FrequenciaHzs,NiveisBits):
    "Exibe a quantidade de bits por segundo necessária pra amostrar e depois quantizar um sinal"
    value = int(2*FrequenciaHzs*math.log(NiveisBits, 2))   
    print("Frequencia de %i Hzs com %i Niveis"%(FrequenciaHzs,NiveisBits))
    print("Amostragem Minima de %i bits por segundo"%(value))
    return(value)
