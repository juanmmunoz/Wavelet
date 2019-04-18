#python Wavelet.py
import numpy as np
from PyLets import MatPlotWavelets as mwl
from PyLets import Others as ot
from PyLets import SignalsAnalyses as sia
from PyLets import Wavelets as wale


t = np.linspace(0, 10,1000)
dilat = np.linspace(0, 0.5,1000)
WaveletSinal = wale.HermitianWavelet1(t,0.25,5)
sinal = wale.SinalBasico(t,1,1) +wale.SinalBasico(t,2,1)
Wavelet= wale.HermitianWavelet1
mwl.WaveLetMatPlot(t,WaveletSinal)
mwl.WaveLetMatPlot(t,sinal)
TransWaveMatrix = sia.TransWaveletCont(t,dilat,sinal,Wavelet)
print(TransWaveMatrix)
mwl.TransWaveletContGraph(TransWaveMatrix)






# alising
# nisquit
# operador hermitiano
# Testar funções
