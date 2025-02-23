import matplotlib.pyplot as plt
import numpy as np


def lagrange_interpolation(x, fx, z):
    """
    Realiza a interpolação de Lagrange para calcular f(z).
    """
    n = len(x)
    px = 0.0
    for i in range(n):
        produtorio = 1.0
        for j in range(n):
            if j != i:
                produtorio *= (z - x[j]) / (x[i] - x[j])
        px += fx[i] * produtorio
    return px


def plot_interpolation(x, fx, z=None, fz=None):
    """
    Gera o gráfico dos pontos e da curva interpolada.
    """
    # Pontos fornecidos pelo usuário
    plt.scatter(x, fx, color='red', label='Pontos conhecidos')

    # Curva interpolada
    x_vals = np.linspace(min(x), max(x), 500)  # Gera 500 pontos no intervalo
    y_vals = [lagrange_interpolation(x, fx, xi) for xi in x_vals]
    plt.plot(x_vals, y_vals, label='Curva interpolada', color='blue')

    # Ponto interpolado (se fornecido)
    if z is not None and fz is not None:
        plt.scatter(z, fz, color='green', label=f'f({z}) = {fz:.4f}')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Interpolação de Lagrange')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    print("\n\nInterpolacao de Lagrange\n-------------------------------------------")
    dados = False
    pmax, pmin = 0.0, 0.0
    x = []
    fx = []

    while True:
        if not dados:
            n = int(
                input("\nQuantos pontos voce possui para realizar a interpolacao? "))
            dados = True
            print("\nInforme os valores para os pares [x, f(x)]")
            for i in range(n):
                x.append(float(input(f"x[{i+1}]=")))
                fx.append(float(input(f"f(x[{i+1}])=")))
                if i == 0:
                    pmax = x[i]
                    pmin = x[i]
                if x[i] < pmin:
                    pmin = x[i]
                if x[i] > pmax:
                    pmax = x[i]

        z = float(
            input("\nInforme o ponto para o qual voce deseja calcular o f(x) para x="))
        if z > pmax or z < pmin:
            print(
                f"\nNao e' possivel interpolar f({z}) pois se trata de uma EXTRAPOLACAO!")
        else:
            fz = lagrange_interpolation(x, fx, z)
            print(f"\nO valor de f({z}) = {fz}")

            # Gera o gráfico
            plot_interpolation(x, fx, z, fz)

        tcl = input(
            "\nTecle 'S' caso deseje reiniciar o programa: ").strip().upper()
        if tcl != 'S':
            return
        tcl = input(
            "\nTecle 'S' caso deseje utilizar os mesmos pontos anteriores: ").strip().upper()
        if tcl != 'S':
            dados = False
            x.clear()
            fx.clear()


if __name__ == "__main__":
    main()
