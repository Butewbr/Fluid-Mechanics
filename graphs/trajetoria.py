import matplotlib.pyplot as plt
import numpy as np

from formulas import trajetoria_x, trajetoria_y

# Intervalo de tempo
t_values = np.linspace(0, 10, 1000)

# Parâmetros iniciais
t0 = 7  # Ponto inicial (1.9, 3.25) no instante t0 = 7s

# Calculando os pontos da trajetória
x_traj = trajetoria_x(t_values, 1.9, t0)
y_traj = trajetoria_y(t_values, 3.25, t0)

# Gerando o gráfico
plt.figure(figsize=(10, 6), dpi=400)
plt.plot(x_traj, y_traj, label=f'Trajetória a partir de t0={t0}s')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trajetória da partícula que passa por (1.9, 3.25) no instante t0=7s entre t=0s e t=10s')
plt.legend()
plt.grid(True)
plt.show()

plt.savefig("trajetoria.png")