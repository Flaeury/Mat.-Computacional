def fatoracao_LU(A):
    n = len(A)  # Tamanho da matriz quadrada
    L = [[0] * n for _ in range(n)]  # Matriz L (triangular inferior)
    U = [[0] * n for _ in range(n)]  # Matriz U (triangular superior)

    for i in range(n):
        # Verificar se o pivô é zero, caso seja, trocar as linhas
        if A[i][i] == 0:
            for j in range(i + 1, n):
                if A[j][i] != 0:
                    # Troca as linhas i e j
                    A[i], A[j] = A[j], A[i]
                    break

        # Preenche a diagonal principal de U
        for j in range(i, n):
            U[i][j] = A[i][j]  # Copia os valores da linha i de A para U
            for k in range(i):
                U[i][j] -= L[i][k] * U[k][j]

        # Preenche a diagonal inferior de L
        for j in range(i + 1, n):
            L[j][i] = A[j][i]  # Copia os valores da coluna i de A para L
            for k in range(i):
                L[j][i] -= L[j][k] * U[k][i]
            if U[i][i] != 0:
                L[j][i] /= U[i][i]  # Normaliza com o pivô

        # Preenche a diagonal principal de L com 1s
        L[i][i] = 1

    return L, U


# Exemplo de uso
A = [
    [2, 3, 1],
    [4, 6, 2],
    [6, 8, 3]
]

L, U = fatoracao_LU(A)

print("Matriz L (triangular inferior):")
for row in L:
    print(row)

print("\nMatriz U (triangular superior):")
for row in U:
    print(row)
