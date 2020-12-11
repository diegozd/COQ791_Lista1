# 1 Lista de Exercícios de COQ791-Modelagem de sistemas
# b)
# Diego Telles 10/12/2020

# Importando Bibliotecas Python
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

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


# Objetivo: Encontrar as raízes do sistema de equações no Estado Estacionário
# para dirversos chutes iniciais de C e T de modo a observar que o sistema 
# possui 3 possíveis Estados Estacionário

# Definindo função que representa o sistema de equações no estado estacionário (dC/dt = dT/dt = 0) 
# ao qual as raízes serão calculadas. O parâmetro x dessa função é um vetor
# de duas posições cuja primeira represeta a temperatura e a segunda a concentração
def func (x):
    return [q*(Cf-x[1]) - V*k0*np.exp(-E/(R*x[0]))*x[1],
            q*Cp*(Tf - x[0]) + DH*V*k0*np.exp(-E/(R*x[0]))*x[1] - hA*(x[0] - Tc)]

# Definindo loop do numero de vezes que este sistema será resolvido
for i in range(20):

    # Definindo chute inicial de Tempeteratura de forma aleatória dentro do domínio 
    # proposto de 300 a 400K
    TEE = np.array([np.random.rand()*100 + 300])   # K

    # Definindo chute inicial de Concentração de forma aleatória dentro do domínio 
    # proposto de 0 a 10 kgmol/m3
    CEE = np.array([np.random.rand()*10])          # kgmol/m3

    # Encontrando as raízes do sistema a partir do chute inicial proposto
    root = fsolve(func, [TEE, CEE])

    # Criando e atualizando matriz de raízes encontradas 
    # (número de análises nas linhas, raiz da Temperatura na 1ª Coluna e raiz da Concentração na 2ª)
    if i == 0:
        Mroot = np.array([root])
    else:
        Mroot = np.vstack((Mroot, root)) 

# Mostra matriz com raízes no terminal
print("Temperatura (K)", "Concentração (kgmol/m3)")
print(Mroot)

# Plotando gráfico
plt.plot(Mroot[:,0], 'bo')
plt.ylabel('Temperatura (K)')
plt.grid()
plt.show()