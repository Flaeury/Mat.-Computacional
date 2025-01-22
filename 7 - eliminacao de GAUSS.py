import numpy as np


def eliminacao_gauss(matriz_a):
    n = len(matriz_a)

    for i in range(n):
        if matriz_a[i][i] == 0:
            for j in range(i + 1, n):
                if matriz_a[j][i] != 0:
                    matriz_a[i], matriz_a[j] = matriz_a[j], matriz_a[i]
                    break

        matriz_a[i] = matriz_a[i] / matriz_a[i][i]

        for j in range(i + 1, n):
            fator = matriz_a[j][i]
            matriz_a[j] -= fator * matriz_a[i]

    solucao = np.zeros(n)
    for i in range(n - 1, -1, -1):
        solucao[i] = matriz_a[i][n]
        for j in range(i + 1, n):
            solucao[i] -= matriz_a[i][j] * solucao[j]

    return solucao


matriz_a = np.array([
    [1, 1, 0, 3, 4],
    [2, 1, -1, 1, 1],
    [3, -1, -1, 2, -3],
    [-1, 2, 3, -1, 4]
], dtype=float)

solucao = eliminacao_gauss(matriz_a)
print("Solução:", solucao)
