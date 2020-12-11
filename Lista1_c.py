# 1 Lista de Exercícios de COQ791-Modelagem de sistemas
# c)
# Diego Telles 10/12/2020

# Importando Bibliotecas Python
import matplotlib.pyplot as plt
import numpy as np
# from scipy.integrate import odeint # também pode ser resolvido pelo pacote odeident
from scipy.integrate import solve_ivp

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

# Objetivo: Resolver o sistema de forma dinâmica para valores aleatórios de Concentração e 
# Tempertauras e inciais e apresentar um plano de fases que indique o caminho do sistema até
# atingir o Estado Estacionário

# Vetor das coordenadas do Estado Estaionário obtido nos exercícios anteriores
CEE = np.array([2.29464183, 5.6865874, 8.50357778])
TEE = np.array([368.88297641, 337.78144478, 311.95180991])

# Definindo função que representa o sistema de equações diferenciais.
# O parâmetro y dessa função é um vetor de duas posições cuja primeira 
# represeta a concentração e a segunda a temperatura
# def CSTR(y, t): # Declaração da função para uso do odeint
def CSTR(t, y): # Declaração da função para uso dosolve_ivp

    # Decompondo o parâmetro y
    C, T = y

    # Calculando a velocidade específica da reação
    k = k0*np.exp(-E/(R*T))

    # Calculando os termos diferenciais no ponto (C, T)
    dCdt = q*(Cf - C)/V - k*C
    dTdt = q*(Tf - T)/V + DH*k*C/Cp - hA*(T - Tc)/(V*Cp)

    return dCdt, dTdt



# Definindo loop do numero de vezes que este sistema será resolvido
for i in range(50):

    # Definindo chute inicial de Tempeteratura de forma aleatória dentro do domínio 
    # proposto de 300 a 400K
    T0 = np.random.rand()*100 + 300  # K

    # Definindo chute inicial de Concentração de forma aleatória dentro do domínio 
    # proposto de 0 a 10 kgmol/m3
    C0 = np.random.rand()*10        # kgmol/m3

    # Definindo intervalo de tempo que o solver utilizará para resolver as EDOS
    t_span = np.array([0, 30])

    # Definindo vetor de condições iniciais
    y0 = np.array([C0, T0])

    # Utilizando o pacote solve_ivp para resolução do sistema de equações diferencias
    # e armazenando o resultados nas variáveis C, T e t
    sol = solve_ivp(CSTR, t_span, y0, t_eval=np.linspace(0, 30, 101))
    C, T = sol.y
    t = sol.t

    # Identificando para qual estado estacionário o sistema convergiu
    DT = np.array([abs(T[len(C)-1] - TEE[0]), abs(T[len(C)-1] - TEE[1]), abs(T[len(C)-1] - TEE[2])]) 
    minidx = np.where(DT == np.min(DT))

    # Definindo esquema de cores em função do EE que o sistema convergiu 
    # (azul para a menor, preto para a intermediária e vermelho para a maior temperatura)
    if (minidx[0][0] == 0):
        corLabel = 'r-'
    elif (minidx[0][0] == 1):
        corLabel = 'k-'
    else:
        corLabel = 'b-'

    # Carregando esta curva no gráfico
    plt.plot(C, T, corLabel)

# Inserindo os pontos de estado estacionário em verde, configurando plotando o grafico 
plt.plot(CEE, TEE, 'go')
plt.xlabel('Concentracao (kgmol/m³)')
plt.ylabel('Temperatura (K)')
plt.grid()
plt.show()


# odeint
# y0 = np.array([C0, T0])
# t = np.linspace(0, 30, 1001)
# sol = odeint(CSTR, y0, t)
# print(sol)
# plt.plot(t, sol[:, 0], 'b', label='C(t)')
# plt.plot(t, sol[:, 1], 'g', label='T(t)')
# plt.legend(loc='best')
# plt.xlabel('t')
# plt.grid()
# plt.show()