import numpy as np

def gauss_jacobi(A, b, x0, tol=1e-5, max_iter=1000):
    n = len(b)
    x = x0.copy()
    for k in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            sum_ = np.dot(A[i, :], x) - A[i, i] * x[i]
            x_new[i] = (b[i] - sum_) / A[i, i]
        
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k + 1
        x = x_new
    
    return x, max_iter


def gauss_seidel(A, b, x0, tol=1e-5, max_iter=1000):
    n = len(b)
    x = x0.copy()
    for k in range(max_iter):
        for i in range(n):
            sum_ = np.dot(A[i, :], x) - A[i, i] * x[i]
            x[i] = (b[i] - sum_) / A[i, i]
        
        if np.linalg.norm(np.dot(A, x) - b, ord=np.inf) < tol:
            return x, k + 1
    
    return x, max_iter

def comparar_metodos(A, b, x0, tol=1e-5):

    x_jacobi, it_jacobi = gauss_jacobi(A, b, x0, tol)
    print(f"Gauss-Jacobi: {x_jacobi} em {it_jacobi} iterações")

    x_seidel, it_seidel = gauss_seidel(A, b, x0, tol)
    print(f"Gauss-Seidel: {x_seidel} em {it_seidel} iterações")

A = np.array([[4, -1, 0, 0],
              [-1, 4, -1, 0],
              [0, -1, 4, -1],
              [0, 0, -1, 3]])

b = np.array([15, 10, 10, 10])

x0 = np.zeros(len(b))

comparar_metodos(A, b, x0)
