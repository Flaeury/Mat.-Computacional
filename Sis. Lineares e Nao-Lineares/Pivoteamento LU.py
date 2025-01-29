import numpy as np


def fatoracao_lu_com_pivoteamento_parcial(A):
    """
    Realiza a fatoração LU com pivoteamento parcial.

    Parâmetros:
        A (numpy.ndarray): Matriz quadrada de dimensão n x n.

    Retorna:
        P (numpy.ndarray): Matriz de permutação.
        L (numpy.ndarray): Matriz triangular inferior.
        U (numpy.ndarray): Matriz triangular superior.
    """
    n = A.shape[0]
    P = np.eye(n)  # Matriz de permutação
    L = np.zeros_like(A, dtype=float)  # Inicializa L
    U = A.copy().astype(float)  # Copia A para U

    for k in range(n):
        # Pivoteamento parcial
        linha_max = k + np.argmax(np.abs(U[k:, k]))
        if linha_max != k:
            U[[k, linha_max]] = U[[linha_max, k]]
            P[[k, linha_max]] = P[[linha_max, k]]
            if k > 0:
                L[[k, linha_max], :k] = L[[linha_max, k], :k]

        # Eliminação
        for i in range(k + 1, n):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] -= L[i, k] * U[k, k:]

    np.fill_diagonal(L, 1)
    return P, L, U


def resolver_com_lu(P, L, U, b):
    """
    Resolve o sistema linear Ax = b usando a fatoração LU e a matriz de permutação P.

    Parâmetros:
        P (numpy.ndarray): Matriz de permutação.
        L (numpy.ndarray): Matriz triangular inferior.
        U (numpy.ndarray): Matriz triangular superior.
        b (numpy.ndarray): Vetor de termos independentes.

    Retorna:
        x (numpy.ndarray): Solução do sistema.
    """
    b_ajustado = np.dot(P, b)

    # Substituição direta para L * y = b_ajustado
    n = L.shape[0]
    y = np.zeros_like(b, dtype=float)
    for i in range(n):
        y[i] = b_ajustado[i] - np.dot(L[i, :i], y[:i])

    # Substituição retroativa para U * x = y
    x = np.zeros_like(b, dtype=float)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x


def escalonamento_por_FatLU(A, b):
    P, L, U = fatoracao_lu_com_pivoteamento_parcial(A)

    # Resolver o sistema linear
    x = resolver_com_lu(P, L, U, b)
    print("\nSolução x:")
    print(x)

    # Verificação simples
    print("\nVerificação do sistema:")
    for i in range(len(b)):
        resultado = sum(A[i, j] * x[j] for j in range(len(x)))
        print(f"Equação {i + 1}:")
        print(f"  Resultado (Ax): {resultado}")
        print(f"  Termo independente (b): {b[i]}")
        print(f"  Diferença: {abs(resultado - b[i])}\n")


if __name__ == "__main__":
    matriz = np.array([
        [10, 1, 1, 2, 1, 3],

    ])
    vetor = np.array([[12], [13], [14], [15], [16], [17]])
    escalonamento_por_FatLU(matriz, vetor)
