#python Wavelet.py
import FormulasWavelet as FW
import numpy as np


t = np.linspace(0, 10,40000)
posic = 5
dilat = 1/4
sinal = FW.MeyerWavelet(t,dilat,posic)
FW.plotly(t,sinal)




# sinal += 4*np.sin(Frequency*2*np.pi*t) 

# alising
# nisquit
# operador hermitiano
# Testar funções
