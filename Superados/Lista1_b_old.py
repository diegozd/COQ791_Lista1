# 1 Lista de Exercícios de COQ791-Modelagem de sistemas
# b)
# Diego Telles 10/12/2020

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

q = 0.1         # m3/h
V = 0.1         # m3
k0 = 9703*3600  # 1/h
DH = 5960       # kcal/kgmol
E = 11843       # kcal/kgmol
Cp = 500        # kcal/m3/K
hA = 15         # kcal/h/K
R = 1.987       # kcal/kgmol/K
Tc = 298.5      # K
Tf = 298.15     # K
Cf = 10         # kgmol/m3

limitIter = 100
e = 1          # K Tolerância 
dT = 0.0001         # K

# TEE = np.array([350])         # K
# TEE = np.array([np.linspace(300,400,num = 11)],ndmin=2)


for i in range(11):
    
    TEE = np.array([300 + i*10])         # K

    idx = 0
    while True:
        
        CEE = q*Cf/(q + V*k0*np.exp(-E/(R*TEE[idx])))      # kgmol/m3

        FT = q*Cp*(Tf - TEE[idx]) + DH*V*k0*np.exp(-E/(R*TEE[idx]))*CEE - hA*(TEE[idx] - Tc)
        FTdT = q*Cp*(Tf-(TEE[idx]+dT)) + DH*V*k0*np.exp(-E/(R*(TEE[idx]+dT)))*CEE - hA*((TEE[idx]+dT)-Tc)
        FlT = (FTdT - FT)/dT
        TEE = np.append(TEE, TEE[idx] - FT/FlT)
        idx += 1
        
        # if (abs(TEE[idx]-TEE[idx-1]) < e) or (idx > limitIter):
        if (abs(FT) < e) or (idx > limitIter):
            break
        
    # print(TEE[idx], CEE, FT)
    # plt.plot(TEE)


# Tteste = 369
# CEE = q*Cf/(q + V*k0*np.exp(-E/(R*Tteste))) 
# print(q*Cp*(Tf - Tteste) + DH*V*k0*np.exp(-E/(R*Tteste))*CEE - hA*(Tteste - Tc), CEE)


def func (x):
    return [q*(Cf-x[1]) - V*k0*np.exp(-E/(R*x[0]))*x[1],
            q*Cp*(Tf - x[0]) + DH*V*k0*np.exp(-E/(R*x[0]))*x[1] - hA*(x[0] - Tc)]

for i in range(20):

    TEE2 = np.array([np.random.rand()*100 + 300])         # K
    CEE2 = np.array([np.random.rand()*10])  
    root = fsolve(func, [TEE2, CEE2])
    if i == 0:
        Mroot = np.array([root])
    else:
        Mroot = np.vstack((Mroot, root)) 
    # print(root)
    # plt.plot(root[0])

print(Mroot)
plt.plot(Mroot[:,1],Mroot[:,0], 'bo')

# plt.plot(TEE)
# plt.ylim(bottom=300,top=420)
plt.show()
