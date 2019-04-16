#python Wavelet.py
import FormulasWavelet as FW
import numpy as np
import matplotlib.pyplot as plt
dilat = np.linspace(0, 5,1000)
t = np.linspace(0, 5,1000)
sinal = FW.SinalBasico(t,0.5,1)
Wavelet = FW.MexicanHat
TransWaveMatrix = FW.TransformadaWavelet(t,sinal,dilat,Wavelet)
print(TransWaveMatrix)
plt.imshow(TransWaveMatrix)
plt.show()






# alising
# nisquit
# operador hermitiano
# Testar funções
