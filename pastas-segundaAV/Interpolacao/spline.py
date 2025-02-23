import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Dados de entrada
x = np.array([-1, 0, 1, 2])
y = np.array([4, 1, -1, 7])

# Criando a spline cúbica
# bc_type='natural' impõe segunda derivada zero nas extremidades
spline = CubicSpline(x, y, bc_type='natural')

# Criando pontos para o gráfico
x_novo = np.linspace(min(x), max(x), 100)
y_novo = spline(x_novo)

# Plotando a curva spline
plt.plot(x_novo, y_novo, label="Spline Cúbica", color="blue")
plt.scatter(x, y, color="red", label="Pontos Dados")
plt.legend()
plt.grid(True)
plt.title("Interpolação por Spline Cúbica")
plt.show()
