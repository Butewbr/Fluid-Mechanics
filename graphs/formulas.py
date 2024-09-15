import numpy as np

def linha_de_corrente(x, t):
    return 3.25 * (x / 1.9) ** (0.01 * (0.46 + 0.33 * t))

def trajetoria_x(t, Xo, To):
    return Xo * np.exp(0.1 * (t - To))

def trajetoria_y(t, Yo, To):
    return Yo * np.exp(0.00046 * (t - To) + 0.000165 * (t**2 - To**2))