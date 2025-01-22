import math


def secante(f, x0, x1, epsilon1, epsilon2, max_iter=100):
    """
    Método da Secante para encontrar uma raiz de f(x) = 0.

    Parâmetros:
    - f: função para a qual se quer encontrar a raiz.
    - x0, x1: aproximações iniciais.
    - epsilon1: tolerância para f(x).
    - epsilon2: tolerância para diferença entre as aproximações.
    - max_iter: número máximo de iterações (padrão 100).

    Retorna:
    - Raiz aproximada da função.
    """
    if abs(f(x0)) < epsilon1:
        return x0

    if abs(f(x1)) < epsilon1 or abs(x1 - x0) < epsilon2:
        return x1

    k = 1
    while k <= max_iter:
        # Cálculo do próximo x2 usando a fórmula da Secante
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

        # Verificação de critérios de parada
        if abs(f(x2)) < epsilon1 or abs(x2 - x1) < epsilon2:
            return x2

        # Atualização dos valores
        x0 = x1
        x1 = x2
        k += 1

    # Se atingir o número máximo de iterações
    raise ValueError(
        "O método não convergiu após o número máximo de iterações.")


# Exemplo de uso

# Definindo uma função exemplo f(x) = x^2 - 2

def f(x):
    return x**2 - 2


# Aproximações iniciais
x0 = 1.0
x1 = 2.0

# Precisões
epsilon1 = 1e-6
epsilon2 = 1e-6

# Chamando o método da secante
try:
    raiz = secante(f, x0, x1, epsilon1, epsilon2)
    print(f"A raiz aproximada é: {raiz}")
except ValueError as e:
    print(e)
