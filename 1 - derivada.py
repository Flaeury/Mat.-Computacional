import sympy as sp


def menu():
    print("\nEscolha o tipo de derivada:")
    print("1. Derivada Simples")
    print("2. Regra da Cadeia")
    print("3. Derivada Parcial")
    print("0. Sair")
    return int(input("Digite sua escolha: "))


def derivada_com_sympy():
    print("\n[Usando Sympy]")
    x, y, z = sp.symbols('x y z')

    escolha = menu()
    if escolha == 1:  # Derivada simples
        funcao = input("Digite a função em relação a x (ex: x**2 + 3*x): ")
        funcao_sympy = sp.sympify(funcao)
        print("Derivada:", sp.diff(funcao_sympy, x))

    elif escolha == 2:  # Regra da cadeia
        funcao = input("Digite a função externa f(x) (ex: sin(x)): ")
        interna = input("Digite a função interna g(x) (ex: x**2): ")
        f = sp.sympify(funcao)
        g = sp.sympify(interna)
        derivada = sp.diff(f, x).subs(x, g) * sp.diff(g, x)
        print("Resultado da regra da cadeia:", derivada)

    elif escolha == 3:  # Derivada parcial
        funcao = input(
            "Digite a função multivariada (ex: x**2 + y**2 + z**2): ")
        variavel = input("Escolha a variável para derivar (x, y ou z): ")
        funcao_sympy = sp.sympify(funcao)
        print(f"Derivada parcial em relação a {variavel}:", sp.diff(
            funcao_sympy, sp.Symbol(variavel)))

    else:
        print("Opção inválida.")


def derivada_sem_sympy():
    print("\n[Sem Sympy]")
    escolha = menu()

    if escolha == 1:  # Derivada simples
        coeficientes = list(map(float, input(
            "Digite os coeficientes do polinômio (ordem decrescente): ").split()))
        derivada = []
        n = len(coeficientes) - 1
        for i, coef in enumerate(coeficientes):
            if n - i >= 1:
                derivada.append(coef * (n - i))
        print("Derivada do polinômio:", derivada)

    elif escolha == 2:  # Regra da cadeia
        def f_prime(x):
            return float(input("Digite o valor de f'(g(x)): "))

        def g_prime(x):
            return float(input("Digite o valor de g'(x): "))
        g_x = float(input("Digite o valor de g(x): "))
        x = float(input("Digite o valor de x: "))
        print("Resultado da regra da cadeia:", f_prime(g_x) * g_prime(x))

    elif escolha == 3:  # Derivada parcial
        def funcao(vars):
            x, y, z = vars
            return eval(input("Digite a função multivariada (ex: x**2 + y**2 + z**2): "))
        ponto = list(
            map(float, input("Digite os valores das variáveis no ponto (x y z): ").split()))
        var_index = int(
            input("Digite o índice da variável a derivar (0 para x, 1 para y, 2 para z): "))
        h = 1e-5
        variaveis_h = ponto[:]
        variaveis_h[var_index] += h
        derivada = (funcao(variaveis_h) - funcao(ponto)) / h
        print(
            f"Derivada parcial em relação à variável de índice {var_index}:", derivada)

    else:
        print("Opção inválida.")

# Programa principal


def main():
    while True:
        print("\nEscolha o método:")
        print("1. Usar Sympy")
        print("2. Calcular manualmente")
        print("0. Sair")
        metodo = int(input("Digite sua escolha: "))

        if metodo == 1:
            derivada_com_sympy()
        elif metodo == 2:
            derivada_sem_sympy()
        elif metodo == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
