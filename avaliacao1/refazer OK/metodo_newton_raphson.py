import math


def metodo_newton_raphson(funcao, derivada_funcao, x0, tol=0.00000001, max_iter=10000000):  # mudar aqui
    """
    Método de Newton-Raphson para encontrar as raízes de uma função.

    Parâmetros:
        funcao (function): Função para a qual queremos encontrar a raiz (f(x) = 0).
        derivada_funcao (function): Derivada da função f(x).
        x0 (float): Chute inicial.
        tol (float): Tolerância para o critério de parada (default: 1e-12).
        max_iter (int): Número máximo de iterações (default: 1000).

    Retorna:
        float: Aproximação para a raiz.
        int: Número de iterações realizadas.

    Lança:
        ValueError: Se o método não convergir dentro do número máximo de iterações
                    ou se a derivada for zero em algum ponto.
    """
    x_atual = x0

    for i in range(1, max_iter + 1):
        f_valor = funcao(x_atual)
        derivada_valor = derivada_funcao(x_atual)

        if derivada_valor == 0:
            raise ValueError("Derivada zero encontrada. O método falhou.")

        # Atualização de Newton-Raphson
        x_proximo = x_atual - f_valor / derivada_valor

        # Critério de parada
        if abs(x_proximo - x_atual) < tol:
            return x_proximo, i

        x_atual = x_proximo

    raise ValueError(
        "O método não convergiu dentro do número máximo de iterações.")

# Função de exemplo para encontrar a raiz de f(x) = x^2 - 8


def funcao(x):
    return x**2  # FUNCAO E DERIVADA


def derivada_funcao(x):
    return x*(x**2 - 6)*math.sin(x) - 6*x**2*math.cos(x) + (2*(2*math.log(x)**2*x**math.log(x) + x**math.log(x) + x**2))/x**2


if __name__ == "__main__":
    # Chute inicial e tolerância
    x0 = 1  # Chute inicial
    tol = 1e-6

    try:
        # Executando o método de Newton-Raphson
        raiz, iteracoes = metodo_newton_raphson(
            funcao, derivada_funcao, x0, tol)
        print(f"A raiz encontrada é x = {
              raiz:.6f} após {iteracoes} iterações.")

        # Teste para verificar a solução
        f_raiz = funcao(raiz)
        print(f"Teste aprovado: f({raiz:.6f}) = {
              f_raiz:.6e}, está próximo de zero.")

    except ValueError as erro:
        print(erro)


# questao 1
# raiz 1 = 1.5184557222177015  raiz2 = 2.583081  raiz3 = 6.561041, raiz4 = 9.136292, raiz5 = 12.981914, raiz6 = 15.148696
