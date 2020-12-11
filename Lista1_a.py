# 1 Lista de Exercícios de COQ791-Modelagem de sistemas
# a)
# Diego Telles 10/12/2020

# Importando Bibliotecas Python
import matplotlib.pyplot as plt
import numpy as np

# Parâmetros do modelo
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

# Objetivo: Calcular as curvas do Calor Gerado (Qg) e Remoovido (Qr) em 
# função da Temperatura de forma a observar os 3 estados estacionários 
# do sistma quando Qg = Qr 

# No estado estacionário dC/dt = dT/dt = 0 a Concentração do Estado estácionário
# pode ser calculada de forma analítica para uma dada Temperatura

# Gerando vetor de Temperaturas no Estado Estacionário no domínio dado (300 < TEE < 400K)
TEE = np.linspace(300,400,num = 101)        # K

# Calculando a Concentração do Estado estácionário 
CEE = q*Cf/(q + V*k0*np.exp(-E/(R*TEE)))    # kgmol/m3

# Calculando Calor Gerado (Qg) e Remoovido (Qr) para TEE e CEE
Qg = DH*V*k0*np.exp(-E/(R*TEE))*CEE         # kcal/h
Qr = (q*Cp + hA)*TEE - (q*Cp*Tf + hA*Tc)    # kcal/h

# Plotando gráfico
plt.plot(TEE,Qg,label='Gerado')
plt.plot(TEE,Qr,label='Removido')
plt.xlabel('Temperatura (K)')
plt.ylabel('Calor (kcal/h)')
plt.xlim(left=300,right=400)
plt.ylim(bottom=0)
plt.legend()
plt.grid()
plt.show()