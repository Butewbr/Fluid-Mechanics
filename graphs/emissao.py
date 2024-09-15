import numpy as np
import matplotlib.pyplot as plt

from formulas import trajetoria_x, trajetoria_y

# Intervalo de tempo de 0 a 10 s para a trajetória
valores_t_trajetoria = np.linspace(0, 10, 100)

# Calculando valores de trajetória entre t=0 e t=10s
x_traj = trajetoria_x(valores_t_trajetoria, 1.9, 7)
y_traj = trajetoria_y(valores_t_trajetoria, 3.25, 7)


# Intervalo de tempo de 0 a 7s para a linha de emissao T=7
valores_t_o_emissao7 = np.linspace(0, 7, 100)

# Intervalo de tempo de 0 a 10  para a linha de emissao T=10
valores_t_o_emissao10 = np.linspace(0, 10, 100)


# Calculando valores de emissao 7
x_emissao7 = trajetoria_x(7, 0.9435, valores_t_o_emissao7)
y_emissao7 = trajetoria_y(7, 3.2135, valores_t_o_emissao7)


# Calculando valores de emissao 10
x_emissao10 = trajetoria_x(10, 0.9435, valores_t_o_emissao10)
y_emissao10 = trajetoria_y(10, 3.2135, valores_t_o_emissao10)


# Criando o gráfico
plt.figure(figsize=(10, 6), dpi=400)


# Plotando a emissao 7
plt.plot(x_emissao7, y_emissao7, label='Emissão 7')

# Plotando a # Plotando a emissao 10
plt.plot(x_emissao10, y_emissao10, label='Emissão 10')

# Plotando a trajetória completa da partícula
plt.plot(x_traj, y_traj, label='Trajetória da Partícula')

# Configurações do gráfico
plt.title('Linhas de emissão para t=7 e t=10')
plt.xlabel('Posição x')
plt.ylabel('Posição y')
plt.grid(True)
plt.legend()

# Mostrando o gráfico
plt.show()

plt.savefig("emissao.png")