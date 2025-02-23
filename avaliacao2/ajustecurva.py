import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func_linear(x, a, b):
    return a * x + b


def func_exponencial(x, a, b):
    return a * np.exp(b * x)


def func_logaritmica(x, a, b):
    return a + b * np.log(x)


def func_potencia(x, a, b):
    return a * x ** b


def ajuste_curva(x, y, tipo):
    if tipo == 'linear':
        popt, _ = curve_fit(func_linear, x, y)
        return popt, func_linear
    elif tipo == 'exponencial':
        popt, _ = curve_fit(func_exponencial, x, y)
        return popt, func_exponencial
    elif tipo == 'logaritmica':
        popt, _ = curve_fit(func_logaritmica, x, y)
        return popt, func_logaritmica
    elif tipo == 'potencia':
        popt, _ = curve_fit(func_potencia, x, y)
        return popt, func_potencia
    else:
        raise ValueError(
            "Tipo de ajuste não reconhecido. Escolha entre 'linear', 'exponencial', 'logaritmica' ou 'potencia'.")


def plot_ajuste(x, y, tipo):
    popt, func = ajuste_curva(x, y, tipo)
    x_ajuste = np.linspace(min(x), max(x), 100)
    y_ajuste = func(x_ajuste, *popt)

    plt.scatter(x, y, label='Pontos Originais', color='red')
    plt.plot(x_ajuste, y_ajuste,
             label=f'Ajuste {tipo.capitalize()}', color='blue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Ajuste de Curva - {tipo.capitalize()}')
    plt.legend()
    plt.show()

    equacao = " + ".join([f"{coef:.4f} * x^{i}" for i,
                         coef in enumerate(popt)])
    print(f"Equação Ajustada ({tipo}): {equacao}")


# Exemplo de uso:
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([2.1, 2.9, 3.8, 5.1, 6.5, 8.0, 9.6, 11.4, 13.5])

plot_ajuste(x, y, 'linear')  # Ajuste linear
plot_ajuste(x, y, 'exponencial')  # Ajuste exponencial
