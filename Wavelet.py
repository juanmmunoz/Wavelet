#python Wavelet.py
import numpy as np
from PyLets import MatPlotWavelets as mwl
from PyLets import Others as ot
from PyLets import SignalsAnalyses as sia
from PyLets import Wavelets as wale
from matplotlib import pyplot as plt


t = np.linspace(0, 10,100)
dilat = np.linspace(0, 1,100)
WaveletSinal = wale.MexicanHat(t,0.5,1)
sinal = wale.SinalBasico(t,1,1) +wale.SinalBasico(t,2,1)
Wavelet= wale.MexicanHat
mwl.WaveLetMatPlot(t,WaveletSinal)
mwl.WaveLetMatPlot(t,sinal)
TransWaveMatrix = sia.TransWaveletCont(t,dilat,sinal,Wavelet)
print(TransWaveMatrix)







# alising
# nisquit
# operador hermitiano
# Testar funções
