import math

# Funções de teste


def f1(x):
    return x**6 - 2*x**4 + x - 5  # Polinômio de grau > 5


def f2(x):
    return math.log(x + 3) - math.sin(x)  # Logaritmo + seno


def f3(x):
    return math.exp(-x) - x**3  # Exponencial + polinômio


def f4(x):
    return math.sin(x) - 0.5*x  # Seno + multiplicação


def f5(x):
    return 1 / (x**2 + 1) - 0.5  # Divisão + raiz

# Algoritmo de testagem do sinal


def test_sign(f, a, b, step=0.1):
    intervals = []
    x = a
    while x < b:
        if f(x) * f(x + step) < 0:  # Mudança de sinal
            intervals.append((x, x + step))
        x += step
    return intervals

# Método da Bisseção


def bisection(f, a, b, tol):
    if f(a) * f(b) >= 0:
        raise ValueError("O intervalo não contém uma raiz.")
    results = []
    while abs(b - a) > tol:
        c = (a + b) / 2
        results.append((a, b, c, f(c)))
        if abs(f(c)) < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, results

# Método da Secante


def secante(f, x0, x1, tol, max_iter=100):
    results = []
    for _ in range(max_iter):
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        results.append((x0, x1, x2, f(x2)))
        if abs(f(x2)) < tol:
            return x2, results
        x0, x1 = x1, x2
    raise ValueError("O método não convergiu.")

# Método de Newton-Raphson


def newton_raphson(f, df, x0, tol, max_iter=100):
    results = []
    for _ in range(max_iter):
        x1 = x0 - f(x0) / df(x0)
        results.append((x0, x1, f(x1)))
        if abs(f(x1)) < tol:
            return x1, results
        x0 = x1
    raise ValueError("O método não convergiu.")

# Função auxiliar para derivada


def df1(x):
    return 6*x**5 - 8*x**3 + 1
