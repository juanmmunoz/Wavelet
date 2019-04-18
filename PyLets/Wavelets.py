import math
import numpy as np
import scipy.integrate as integrate

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
