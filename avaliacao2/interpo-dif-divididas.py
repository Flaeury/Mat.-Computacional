import numpy as np


def diferencas_divididas(x, y):
    """
    Calcula a tabela de diferenças divididas para interpolação de Newton.

    Parâmetros:
    x (list ou np.array): Valores de x (pontos conhecidos).
    y (list ou np.array): Valores de y (f(x) nos pontos conhecidos).

    Retorna:
    np.array: Tabela de diferenças divididas.
    """
    n = len(x)
    tabela = np.zeros((n, n))
    tabela[:, 0] = y  # Primeira coluna recebe os valores de y

    # Construção da tabela de diferenças divididas
    for j in range(1, n):
        for i in range(n - j):
            tabela[i][j] = (tabela[i + 1][j - 1] - tabela[i]
                            [j - 1]) / (x[i + j] - x[i])

    return tabela


def interpolacao_newton(x, y, valor):
    """
    Realiza a interpolação de Newton para um valor específico.

    Parâmetros:
    x (list ou np.array): Valores de x (pontos conhecidos).
    y (list ou np.array): Valores de y (f(x) nos pontos conhecidos).
    valor (float): Valor de x para o qual se deseja calcular o y interpolado.

    Retorna:
    float: Valor interpolado de y para o valor de x fornecido.
    """
    n = len(x)
    # Calcula a tabela de diferenças divididas
    tabela = diferencas_divididas(x, y)

    # Inicializa o resultado com o primeiro termo da tabela
    resultado = tabela[0][0]

    # Calcula o polinômio interpolador
    for i in range(1, n):
        termo = tabela[0][i]
        for j in range(i):
            termo *= (valor - x[j])
        resultado += termo

    return resultado


# Exemplo de uso
if __name__ == "__main__":
    # Pontos conhecidos (x, y)
    x = [1, 2, 3, 4]
    y = [1, 4, 9, 16]

    # Valor para interpolar
    valor = 2.5

    # Realiza a interpolação
    resultado = interpolacao_newton(x, y, valor)
    print(f"O valor interpolado para x = {valor} é y = {resultado}")
