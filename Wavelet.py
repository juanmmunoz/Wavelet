#python Wavelet.py
import numpy as np
from matplotlib import pyplot as plt
import FormulasWavelet as FW

t = np.linspace(-10, 20,400)
posic = 5
dilat = 1

sinal = FW.MexicanHat(t,dilat,posic)

tempo = 10
dilat = 5
sinal += FW.HermitianHat(t,dilat,posic) 
FW.GraficoWaveLet(t,sinal)



# sinal += 4*np.sin(Frequency*2*np.pi*t) 

# alising
# nisquit
# operador hermitiano
# Testar funções
