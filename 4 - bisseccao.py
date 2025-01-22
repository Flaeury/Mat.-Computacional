import math
import sys

e = sys.float_info.epsilon


def bissecao(f, a, b, e):
    if f(a) * f(b) > 0:
        return "Intervalo inavlido, f(a) e f(b) deve ter sinais opostos"
    while (b-a)/2 > e:
        c = (a+b)/2
        if f(c) == 0:
            return c
        elif (f(a) > 0 and f(c) > 0) or (f(a) < 0 and f(c) < 0):
            a = c
        elif (f(b) > 0 and f(c) > 0) or (f(b) < 0 and f(c) < 0):
            b = c
    return c


def f1(x):
    return (x**3) - (9*x) + 3


def f2(x):
    return math.sqrt(x) - 5 * math.exp(-x)


def f3(x):
    return x*math.log10(x) - 1


print("Raiz da função f1(x) = x^3 - 9x + 3")
print(bissecao(f1, 2, 3, e))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Raiz da função f2(x) = sqrt(x) - 5e^(-x)")
print(bissecao(f2, 0.1, 2, e))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Raiz da função f3(x) = x*log(x) - 1")
print(bissecao(f3, 1, 3, e))
