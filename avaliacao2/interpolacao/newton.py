import matplotlib.pyplot as plt
import numpy as np


def diferencas_divididas(x, fx):
    """
    Calcula a tabela de diferenças divididas para interpolação de Newton.
    """
    n = len(x)
    tabela = np.zeros((n, n))
    tabela[:, 0] = fx  # Primeira coluna recebe os valores de f(x)

    # Construção da tabela de diferenças divididas
    for j in range(1, n):
        for i in range(n - j):
            tabela[i][j] = (tabela[i + 1][j - 1] - tabela[i]
                            [j - 1]) / (x[i + j] - x[i])
    return tabela


def newton_interpolation(x, fx, z):
    """
    Realiza a interpolação de Newton para calcular f(z).
    """
    n = len(x)
    tabela = diferencas_divididas(x, fx)
    resultado = tabela[0][0]  # Primeiro termo da tabela

    # Calcula o polinômio interpolador
    for i in range(1, n):
        termo = tabela[0][i]
        for j in range(i):
            termo *= (z - x[j])
        resultado += termo
    return resultado


def plot_interpolation(x, fx, z=None, fz=None, metodo='newton'):
    """
    Gera o gráfico dos pontos e da curva interpolada.
    """
    # Pontos fornecidos pelo usuário
    plt.scatter(x, fx, color='red', label='Pontos conhecidos')

    # Curva interpolada
    x_vals = np.linspace(min(x), max(x), 500)  # Gera 500 pontos no intervalo
    if metodo == 'newton':
        y_vals = [newton_interpolation(x, fx, xi) for xi in x_vals]
        label_curva = 'Curva interpolada (Newton)'
    else:
        y_vals = [lagrange_interpolation(x, fx, xi) for xi in x_vals]
        label_curva = 'Curva interpolada (Lagrange)'
    plt.plot(x_vals, y_vals, label=label_curva, color='blue')

    # Ponto interpolado (se fornecido)
    if z is not None and fz is not None:
        plt.scatter(z, fz, color='green', label=f'f({z}) = {fz:.4f}')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Interpolação de Newton' if metodo ==
              'newton' else 'Interpolação de Lagrange')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    print("\n\nInterpolacao de Newton\n-------------------------------------------")
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
            fz = newton_interpolation(x, fx, z)
            print(f"\nO valor de f({z}) = {fz}")

            # Gera o gráfico
            plot_interpolation(x, fx, z, fz, metodo='newton')

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
