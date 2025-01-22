import math


def calcular_ex_serie(x, n):
    """
    Calcula e^x usando a série de Taylor com n termos.
    """
    resultado = 0
    for k in range(n + 1):
        termo = (x ** k) / math.factorial(k)
        resultado += termo
    return resultado


def calcular_ex_negativo(x, n):
    """
    Calcula e^x para x < 0 de duas formas:
    1. Usando o x diretamente na série.
    2. Usando y = -x e aplicando 1/e^x.
    """
    # Direto pela série
    ex_direto = calcular_ex_serie(x, n)

    # Usando y = -x
    y = -x
    ex_indireto = 1 / calcular_ex_serie(y, n)

    return ex_direto, ex_indireto


def testar_valores():
    print("Cálculo de e^x utilizando a série de Taylor\n")

    valores_x = [0, 1, -1, 2, -2, 5, -5]
    valores_n = [5, 10, 20]

    for x in valores_x:
        for n in valores_n:
            print(f"x = {x}, n = {n}")
            if x >= 0:
                resultado = calcular_ex_serie(x, n)
                print(f"e^{x} (usando série): {resultado:.10f}")
            else:
                direto, indireto = calcular_ex_negativo(x, n)
                print(f"e^{x} (usando série diretamente): {direto:.10f}")
                print(f"e^{x} (usando 1/e^-x): {indireto:.10f}")
            print()


def calcular_ex_taylor(x, epsilon=1e-15):
    """
    Calcula e^x usando a série de Taylor sem overflow.
    O cálculo para quando o termo atual é menor que epsilon.
    """
    termo = 1  # Primeiro termo da série: x^0 / 0! = 1
    soma = termo  # Inicializa a soma com o primeiro termo
    k = 1  # Índice do termo

    while abs(termo) > epsilon:
        # Calcula o próximo termo usando o termo anterior
        termo = termo * x / k
        soma += termo
        k += 1

    return soma, k - 1


if __name__ == "__main__":
    testar_valores()

    valores_x = [0, 1, -1, 2, -2, 10, -10]
    epsilon = 1e-15
    for x in valores_x:
        resultado, n_termos = calcular_ex_taylor(x, epsilon)
        print(f"x = {x}, e^x = {resultado:.15f}, termos usados = {n_termos}")

"""
Análise dos Resultados:

1. Precisão com n:
   - Para valores de x próximos a 0, mesmo valores baixos de n fornecem resultados precisos.
   - Para valores maiores de |x|, o erro se torna significativo com n pequeno.

2. Cálculo com x < 0:
   - Usar 1/e^{-x} é geralmente mais preciso para valores negativos grandes (|x| alto),
     pois evita somas acumulativas que podem introduzir erros numéricos.

3. Erro relativo:
   - Comparando os métodos para x < 0, a diferença entre os dois métodos é pequena,
     mas perceptível quando n é baixo e x é grande em valor absoluto.

4. Vantagem da série de Taylor:
   - A série de Taylor é eficiente e fácil de implementar para calcular e^x,
     mas a precisão depende diretamente do número de termos (n).

5. Consideração para grandes valores de |x|:
   - Para valores muito grandes de |x|, a precisão numérica do ponto flutuante
     pode causar erros consideráveis. Nestes casos, métodos alternativos ou bibliotecas
     de precisão estendida podem ser necessários.
"""
