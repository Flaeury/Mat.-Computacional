import numpy as np

def resolver_sistema_linear_gauss_seidel(matriz, vetor, precisao=13, max_iteracoes=500):
    """
    Resolve um sistema linear Ax = b usando o método iterativo de Gauss-Seidel.

    Parâmetros:
        matriz (numpy array): Matriz dos coeficientes.
        vetor (numpy array): Vetor dos termos independentes.
        precisao (int): Precisão para o critério de parada (p). Default: 13.
        max_iteracoes (int): Número máximo de iterações. Default: 500.

    Retorna:
        solucao (numpy array): Vetor solução.
        iteracoes (int): Número de iterações realizadas.

    Lança:
        Exception: Caso o método não convirja após o número máximo de iterações.
    """
    tamanho = len(vetor)
    solucao = np.zeros_like(vetor, dtype=float)  # Chute inicial

    iteracoes = 0
    erro = 1

    while erro >= 10**(-precisao) and iteracoes <= max_iteracoes:
        solucao_antiga = np.copy(solucao)

        for i in range(tamanho):
            soma = sum(matriz[i, j] * solucao[j] for j in range(tamanho) if j != i)
            solucao[i] = (vetor[i] - soma) / matriz[i, i]

        erro = np.max(np.abs(solucao - solucao_antiga)) / np.max(np.abs(solucao))
        iteracoes += 1

    if iteracoes > max_iteracoes:
        raise Exception("O método não convergiu após o número máximo de iterações.")

    return solucao, iteracoes

def verificar_matriz_adequada(matriz):
    """
    Avalia se a matriz é adequada para o método de Gauss-Seidel.

    Parâmetros:
        matriz (numpy array): Matriz dos coeficientes.

    Retorna:
        bool: True se a matriz for estritamente diagonal dominante, False caso contrário.
    """
    tamanho = matriz.shape[0]
    for i in range(tamanho):
        elemento_diagonal = abs(matriz[i, i])
        soma_fora_diagonal = sum(abs(matriz[i, j]) for j in range(tamanho) if j != i)
        if elemento_diagonal <= soma_fora_diagonal:
            return False
    return True

# Exemplo de uso
if __name__ == "__main__":
    # Matriz fixa e vetor que garantem a convergência
    matriz = np.array([
        [1, 1, 2],
        [-1, 11, -1],
        [2, -1, 10]
    ], dtype=float)
    vetor = np.array([6, 25, -11], dtype=float)

    print("\nMatriz A (coeficientes):")
    print(matriz)
    print("\nVetor b (termos independentes):")
    print(vetor)

    if verificar_matriz_adequada(matriz):
        print("\nA matriz é adequada para o método de Gauss-Seidel.")
        try:
            solucao, iteracoes = resolver_sistema_linear_gauss_seidel(matriz, vetor)
            print("\nSolução encontrada:")
            print(solucao)
            print(f"Número de iterações realizadas: {iteracoes}")

            # Verificação da solução encontrada
            print("\nComparação entre termo independente (b) e resultado (Ax):")
            for i in range(len(vetor)):
                resultado = sum(matriz[i, j] * solucao[j] for j in range(len(vetor)))
                print(f"Equação {i + 1}:")
                print(f"  Resultado (Ax): {resultado:.13f}")
                print(f"  Termo independente (b): {vetor[i]:.13f}")
                print(f"  Diferença: {abs(resultado - vetor[i]):.13f}\n")
        except Exception as erro:
            print("\nErro:", erro)
    else:
        print("\nA matriz NÃO é adequada para o método de Gauss-Seidel.")
