# 1 Lista de Exercícios de COQ791-Modelagem de sistemas
# d)
# Diego Telles 10/12/2020

# Importando Bibliotecas Python
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

# Parâmetros do modelo
V = 0.1         # m3
k0 = 9703*3600  # 1/h
DH = 5960       # kcal/kgmol
E = 11843       # kcal/kgmol
Cp = 500        # kcal/m3/K
hA = 15         # kcal/h/K
R = 1.987       # kcal/kgmol/K
Tc_fixo = 298.5      # K
Tf_fixo = 298.15     # K
Cf = 10         # kgmol/m3


# Objetivo: construir 2 o diagramas de soluções estacionárias do reator. O primeiro
# tendo como parâmetro a Temperatura de entrada da camisa (Tc) e o segundo a Temperatura
# de entrada da carga

# Criando vetor de vazões de entrada do sistema
q = np.linspace(0.01, 0.1, 10)


############################################
#### 1 - Tc Como parâmetro independente ####
############################################

# Criando área de plotagem
fig = plt.figure(1)
ax = fig.gca(projection='3d')

# Definindo loop do numero de curvas de q/v
for idx in range(10):

    # Criando vetor de temperaturas do estado estacionário do sistema
    TEE = np.linspace(300, 400, 101)

    # Calculando vetor de velocidade específica da reação
    k = k0*np.exp(-E/(R*TEE))

    # Calculando vetor de concentrações do estado estacionário do sistema
    CEE = q[idx]*Cf/(q[idx] + V*k)

    # Calculando vetor de Temperaturas da camisa para cada respectivo par TEE e CEE
    Tc = TEE + (q[idx]*Cp*(TEE-Tf_fixo) - DH*V*k*CEE)/hA

    # Criando vetor de q/v (mesma dimensão dos demais com o valor contante utilizado nas contas acima)
    qplot = np.ones(101)*q[idx]/V

    # Carregando esta curva no gráfico 1
    ax.plot(Tc, qplot, TEE)

# configurando grafico 1
ax.set_xlabel('Tc (K)')
ax.set_ylabel('q/V (1/h)')
ax.set_zlabel('T (K)')

############################################
#### 1 - Tf Como parâmetro independente ####
############################################

# Criando área de plotagem
fig = plt.figure(2)
ax = fig.gca(projection='3d')

# Definindo loop do numero de curvas de q/v
for idx in range(10):

    # Criando vetor de temperaturas do estado estacionário do sistema
    TEE = np.linspace(300, 400, 101)

    # Calculando vetor de velocidade específica da reação
    k = k0*np.exp(-E/(R*TEE))

    # Calculando vetor de concentrações do estado estacionário do sistema
    CEE = q[idx]*Cf/(q[idx] + V*k)

    # Calculando vetor de Temperaturas de entrada da carga para cada respectivo par TEE e CEE
    Tf = TEE + (hA*(TEE-Tc_fixo) - DH*V*k*CEE)/(q[idx]*Cp)

    # Criando vetor de q/v (mesma dimensão dos demais com o valor contante utilizado nas contas acima)
    qplot = np.ones(101)*q[idx]/V

    # Carregando esta curva no gráfico 2
    ax.plot(Tf, qplot, TEE)

# configurando grafico 2
ax.set_xlabel('Tf (K)')
ax.set_ylabel('q/V (1/h)')
ax.set_zlabel('T (K)')

# Plotando ambos os gráficos
plt.show()