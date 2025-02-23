import numpy as np


def eliminacao_de_gauss(matriz):
    """
    Realiza a eliminação de Gauss para escalonar uma matriz.

    Parâmetros:
        matriz (list ou numpy.ndarray): Matriz de coeficientes aumentada.

    Retorna:
        numpy.ndarray: Matriz escalonada.
    """
    matriz = np.array(matriz, dtype=float)
    linhas, colunas = matriz.shape

    # -1 para ignorar o termo independente na última coluna
    for i in range(min(linhas, colunas - 1)):
        # Busca o maior pivô em módulo na coluna atual
        max_row = i + np.argmax(np.abs(matriz[i:, i]))

        # Troca a linha atual com a linha do maior pivô
        if matriz[max_row, i] != 0:
            matriz[[i, max_row]] = matriz[[max_row, i]]

            # Eliminação
            for j in range(i + 1, linhas):
                fator = matriz[j, i] / matriz[i, i]
                matriz[j, i:] -= fator * matriz[i, i:]

    return matriz


def substituicao_retroativa(matriz_escalonada):
    """
    Realiza a substituição retroativa para calcular as variáveis a partir da matriz escalonada.

    Parâmetros:
        matriz_escalonada (numpy.ndarray): Matriz escalonada (forma triangular superior).

    Retorna:
        list: Lista com os valores das variáveis.
    """
    linhas, colunas = matriz_escalonada.shape
    x = np.zeros(linhas)

    for i in range(linhas - 1, -1, -1):  # Começa da última linha
        soma = sum(matriz_escalonada[i, j] * x[j]
                   for j in range(i + 1, colunas - 1))
        x[i] = (matriz_escalonada[i, -1] - soma) / matriz_escalonada[i, i]

    return x


# Exemplo de uso
if __name__ == "__main__":
    print("Soma=", sum)
    # Matriz aumentada consistente
    # matriz = [
    #    [2, 1, -1, 8],
    #    [-3, -1, 2, -11],
    #    [-2, 1, 2, -3]
    # ]

    matriz = [
        [128, 371, 300, 77, 15, 68, 118, 275, 262, 5756],
        [2.5, 10, 8, 0.6, 1.1, 2, 25.7, 29.9, 32.1, 401],
        [0.2, 1.3, 3.1, 0.1, 0.2, 2.1, 0.9, 16.3, 13.9, 98.9],
        [28.1, 77.9, 58.6, 18.4, 3.1, 12.3, 0, 0, 0, 782.8],
        [4, 17, 16, 17, 7, 5, 7, 4, 18, 344],
        [0.1, 0.9, 1, 0.2, 0.2, 0.6, 1.3, 2.8, 1.3, 27],
        [1, 7, 648, 3, 1, 2, 30, 51, 62, 1824],
        [0.02, 0.15, 0.13, 0.06, 0.04, 0.19, 0.09, 0.08, 0.09, 2.84],
        [0.5, 0.8, 0.8, 0.1, 0.1, 0.4, 0.4, 6.7, 3.3, 35.8]
    ]

    matriz_escalonada = eliminacao_de_gauss(matriz)
    print("Matriz escalonada:")
    print(matriz_escalonada)

    # Verificação do sistema
    print("\nVerificação do sistema:")
    linhas, colunas = len(matriz), len(matriz[0])
    for i in range(linhas):
        # Expressão com os coeficientes e os valores escalonados
        expressao = " + ".join([f"({matriz_escalonada[i, j]:.2f} * x{j + 1})" for j in range(colunas - 1)])
        resultado = sum(
            matriz_escalonada[i, j] * matriz_escalonada[j, -1] for j in range(colunas - 1))
        print(f"Equação {i + 1}: {expressao} = {matriz_escalonada[i, -1]:.2f}")
        print(f"  Resultado (Ax): {resultado:.6f}")
        print(f"  Termo independente (b): {matriz_escalonada[i, -1]:.6f}")
        print(f"  Diferença: {
              abs(resultado - matriz_escalonada[i, -1]):.6f}\n")

    # Substituição retroativa para encontrar os valores das variáveis
    valores_x = substituicao_retroativa(matriz_escalonada)
    print("Valores das variáveis (x):")
    for i, valor in enumerate(valores_x, start=1):
        print(f"x{i} = {valor:.6f}")
