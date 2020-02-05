import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model
import sklearn.preprocessing
import sklearn.model_selection
from itertools import combinations
f = open("coin.txt",'r')
data=f.read()
def FOH(data,H):
    NS=0
    NC=0
    for i in data:
        if i=="c":
            NC=NC+1
        else:
            NS=NS+1
    POH=H**NC*(1-H)**NS
    return POH
HL=np.linspace(0.001,1,1000)
POH=FOH(data,HL)
POH=POH/(np.sum(POH)*0.001)
#PD=np.zeros(999)
#SD=np.zeros(999)
#for i in range(999):
#    PD[i]=(POH[i+1]-POH[i])*1000
#for i in range(998):
#    SD[i]=(PD[i+1]-PD[i])*1000
HMAX=HL[POH==np.max(POH)]
#POS=np.where(HL==HMAX)
Sigma=np.sqrt(HMAX*(1-HMAX)/(NC+NS))
plt.plot(HL,POH)
plt.title(data+"\n"+r"$H_0=$%4.3f"%HMAX+r"$\pm$%4.3f"%Sigma)
plt.xlabel("H")
plt.ylabel(r"$P(H|{obs})$")
plt.show()