import math
import sys

e = sys.float_info.epsilon


def posicao_falsa(f, a, b, e, max_iter=100000):
    if f(a) * f(b) > 0:
        return "Intervalo inválido: f(a) e f(b) devem ter sinais opostos"

    iter_count = 0  # contador de iterações

    while abs(b - a) > e and iter_count < max_iter:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

        iter_count += 1  # incrementa contador de iterações

    if iter_count == max_iter:
        return c

    return c


def f1(x):
    return (x**3) - (9*x) + 3


def f2(x):
    return math.sqrt(x) - 5 * math.exp(-x)


def f3(x):
    if x <= 0:
        return float('inf')
    return x * math.log10(x) - 1


print("Raiz da função f1(x) = x^3 - 9x + 3")
print(posicao_falsa(f1, 2, 3, e))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Raiz da função f2(x) = sqrt(x) - 5e^(-x)")
print(posicao_falsa(f2, 0.1, 2, e))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Raiz da função f3(x) = x*log(x) - 1")
print(posicao_falsa(f3, 1, 3, e))
