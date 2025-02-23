import numpy as np


def resolver_sistema_linear_gauss_jacobi(matriz, vetor, precisao=10, max_iteracoes=10000):
    """
    Resolve um sistema linear Ax = b usando o método iterativo de Gauss-Jacobi.

    Parâmetros:
        matriz (numpy array): Matriz dos coeficientes.
        vetor (numpy array): Vetor dos termos independentes.
        precisao (int): Precisão para o critério de parada (p). Default: 8.
        max_iteracoes (int): Número máximo de iterações. Default: 500.

    Retorna:
        solucao (numpy array): Vetor solução.
        iteracoes (int): Número de iterações realizadas.

    Lança:
        Exception: Caso o método não convirja após o número máximo de iterações.
    """
    tamanho, _ = np.shape(matriz)
    inv_diagonal = np.linalg.inv(matriz * np.eye(tamanho))
    B = np.eye(tamanho) - inv_diagonal @ matriz
    d = inv_diagonal @ vetor

    # Chute inicial
    solucao_antiga = np.zeros_like(vetor)

    iteracoes = 0
    erro = 1

    while erro >= 10**(-precisao) and iteracoes <= max_iteracoes:
        solucao_nova = B @ solucao_antiga + d
        erro = np.max(np.abs(solucao_nova - solucao_antiga)) / \
            np.max(np.abs(solucao_nova))
        solucao_antiga = np.copy(solucao_nova)
        iteracoes += 1

    if iteracoes > max_iteracoes:
        raise Exception(
            "O método não convergiu após o número máximo de iterações.")

    return solucao_nova, iteracoes


def verificar_matriz_adequada(matriz):
    """
    Avalia se a matriz é adequada para o método de Gauss-Jacobi.

    Parâmetros:
        matriz (numpy array): Matriz dos coeficientes.

    Retorna:
        bool: True se a matriz for estritamente diagonal dominante, False caso contrário.
    """
    tamanho = matriz.shape[0]
    for i in range(tamanho):
        elemento_diagonal = abs(matriz[i, i])
        soma_fora_diagonal = sum(abs(matriz[i, j])
                                 for j in range(tamanho) if j != i)
        if elemento_diagonal <= soma_fora_diagonal:
            return False
    return True


# Exemplo de uso
if __name__ == "__main__":
    # Matriz estritamente diagonal dominante e vetor dos termos independentes
    matriz = np.array([
        [10, 1, 1, 2, 1, 3],
        [2, 10, 1, 2, 1, 3],
        [1, 1, 10, 5, 1, 1],
        [2, 1, 4, 10, 1, 1],
        [1, 2, 4, 1, 10, 1],
        [1, 1, 1, 4, 2, 10],

    ])
    vetor = np.array([[12], [13], [14], [15], [16], [17]])

    print("\nMatriz A (coeficientes):")
    print(matriz)
    print("\nVetor b (termos independentes):")
    print(vetor)

    if verificar_matriz_adequada(matriz):
        # print("\nA matriz é adequada para o método de Gauss-Jacobi.")
        try:
            solucao, iteracoes = resolver_sistema_linear_gauss_jacobi(
                matriz, vetor)
            print("\nSolução encontrada:")
            print(solucao)
            print(f"Número de iterações realizadas: {iteracoes}")
        except Exception as erro:
            print("\nErro:", erro)
    else:
        print("\nA matriz NÃO é adequada para o método de Gauss-Jacobi.")
