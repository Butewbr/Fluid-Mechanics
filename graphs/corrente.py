import matplotlib.pyplot as plt
import numpy as np

from formulas import linha_de_corrente


# Valores de x para traçar as linhas de corrente
x_values = np.linspace(0, 10, 100) 

# Gerando as linhas de corrente para t=0s, t=7s, e t=10s
plt.figure(figsize=(10, 6), dpi=400)

for t in [0, 7, 10]:
    y_corrente = linha_de_corrente(x_values, t)
    plt.plot(x_values, y_corrente, label=f'Linha de corrente em t={t}s')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Linhas de corrente nos instantes t=0s, t=7s e t=10s')
plt.legend()
plt.grid(True)
plt.show()

plt.savefig("corrente.png")