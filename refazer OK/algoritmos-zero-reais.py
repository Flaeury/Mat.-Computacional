import math

# ======================================================================================================================
#  FUNÇÃO f(x)
# ======================================================================================================================


def f(x):
    """
    Define a função f(x) = x^log(x) + x^2 - x^3 * sin(x).

    Parâmetros:
    -----------
    x : float
        Valor no qual a função será avaliada (x > 0).

    Retorna:
    --------
    float
        O valor de f(x).

    Possíveis erros:
    ----------------
    - Se x <= 0, ocorrerá um ValueError, pois log(x) não está definido para x <= 0.
      Esse erro é tratado dentro da função para evitar comportamento indefinido.
    - Se x for muito pequeno (próximo de zero), pode haver problemas de precisão em log(x).
    - O uso de math.log(x) em Python é o logaritmo natural (base e).

    Como consertar:
    ---------------
    - Certificar-se de que x > 0 ao chamar a função.
    - Tratar exceções ou evitar chamar f(x) com valores fora do domínio (0, +∞).
    """
    if x <= 0:
        # Levanta um erro explicitamente para evitar cálculo de log(x) quando x <= 0
        raise ValueError(
            "x deve ser maior que 0 para calcular o logaritmo natural.")

    # x**(log(x)) = e^(log(x) * log(x)) = e^((ln x)^2)
    # TERMO É A FUNCAO
    return x**2

# ======================================================================================================================
#  DERIVADA f'(x)
# ======================================================================================================================


def df(x):
    """
    Define a derivada da função f(x).

    Parâmetros:
    -----------
    x : float
        Ponto onde a derivada será avaliada (x > 0).

    Retorna:
    --------
    float
        O valor de f'(x).

    Possíveis erros:
    ----------------
    - Se x <= 0, ocorrerá um ValueError, pois log(x) não está definido para x <= 0.
    - Se x for muito próximo de zero, log(x) será muito negativo, o que pode causar problemas de precisão.
    - Se math.log(x) for zero (por exemplo, x=1), temos que verificar se isso não gera termos nulos
      que possam causar divisão por zero, mas neste caso não causa erro diretamente,
      apenas zera parte do termo da derivada.

    Como consertar:
    ---------------
    - Certificar-se de que x > 0 ao chamar a função.
    - Tratar exceções ou valores-limite adequadamente.
    """
    if x <= 0:
        raise ValueError(
            "x deve ser maior que 0 para calcular o logaritmo natural.")

    # A derivada de x^(log(x)) é 2 * ln(x) * x^(ln(x) - 1).
    # Derivada de x^2 é 2x.
    # Derivada de -x^3 sin(x) é -(3x^2 sin(x) + x^3 cos(x)).
    # A soma desses termos resulta:
    # termo é a derivada de x^2
    return (X**3/2)

# ======================================================================================================================
#  MÉTODO DA BISSECÇÃO
# ======================================================================================================================


def bisseccao(a, b, e, max_iter=1000):  # iteracao maxima
    """
    Método da Bissecção para encontrar raízes de f(x) no intervalo [a, b].

    Parâmetros:
    -----------
    a, b : float
        Extremos do intervalo em que se busca a raiz. Precisa ser [a, b] com a < b, e ambos > 0.
    e : float
        Tolerância de erro para o critério de parada.
    max_iter : int, opcional
        Número máximo de iterações permitidas. Padrão = 1000.

    Retorna:
    --------
    (raiz, iteracoes) : (float, int)
        raiz : estimativa para a raiz de f(x) no intervalo [a, b],
        iteracoes : número de iterações realizadas para obter essa estimativa.

    Possíveis erros:
    ----------------
    - Se a <= 0 ou b <= 0, retornamos (None, 0) pois log(x) não é definido.
    - Se f(a)*f(b) >= 0, significa que não há certeza de mudança de sinal no intervalo [a, b],
      logo não podemos garantir a existência de uma raiz nesse intervalo, retornamos (None, 0).

    Como consertar:
    ---------------
    - Verificar se [a, b] está inteiramente no domínio (0, +∞).
    - Verificar se f(a)*f(b) < 0 para garantir mudança de sinal.
    """
    if a <= 0 or b <= 0:
        # Intervalo inválido para essa função, pois f(x) não é definida em x <= 0
        return None, 0

    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        # Não há mudança de sinal, não podemos aplicar a bissecção corretamente
        return None, 0

    iteracoes = 0
    # Enquanto a distância entre b e a for maior que a tolerância e o número de iterações < max_iter
    while abs(b - a) > e and iteracoes < max_iter:
        c = (a + b) / 2  # ponto médio
        fc = f(c)

        # Se fc == 0, encontramos a raiz exata (raro em ponto flutuante)
        if fc == 0:
            return c, iteracoes

        # Verifica de qual lado está a mudança de sinal
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

        iteracoes += 1

    # Retorna o ponto médio final como estimativa da raiz
    return (a + b) / 2, iteracoes

#  MÉTODO DE NEWTON-RAPHSON


def newton_raphson(x0, e, max_iter=1000):
    """
    Método de Newton-Raphson para encontrar raízes de f(x).

    Parâmetros:
    -----------
    x0 : float
        Chute inicial (x0 > 0).
    e : float
        Tolerância de erro para o critério de parada.
    max_iter : int, opcional
        Número máximo de iterações permitidas. Padrão = 1000.

    Retorna:
    --------
    (raiz, iteracoes) : (float, int)
        raiz : estimativa da raiz encontrada,
        iteracoes : número de iterações até atingir a tolerância ou o max_iter.

    Possíveis erros:
    ----------------
    - Se x0 <= 0, retorna (None, 0), pois não faz sentido calcular f(x) ou df(x) em valores não positivos.
    - Se df(x0) == 0, não é possível prosseguir com o método (divisão por zero); retorna (None, iteracoes).
    - Se x1 <= 0 após alguma iteração, retornamos, pois a função não é definida em x <= 0.

    Como consertar:
    ---------------
    - Garantir x0 > 0.
    - Escolher um x0 dentro do domínio e onde df(x0) != 0.
    """
    if x0 <= 0:
        return None, 0

    iteracoes = 0
    while iteracoes < max_iter:
        fx0, dfx0 = f(x0), df(x0)
        if dfx0 == 0:
            # Derivada zero -> não é possível dividir -> método falha
            return None, iteracoes

        # Próximo valor de x usando a fórmula de Newton-Raphson: x1 = x0 - f(x0)/f'(x0)
        x1 = x0 - fx0 / dfx0

        # Se x1 <= 0, saímos por não ser válido no domínio da função
        if x1 <= 0 or abs(x1 - x0) < e:
            return x1, iteracoes + 1

        x0 = x1
        iteracoes += 1

    # Se não convergiu em max_iter, retorna None
    return None, iteracoes

#  MÉTODO DA SECANTE


def secante(x0, x1, e, max_iter=1000):
    """
    Método da Secante para encontrar raízes de f(x).

    Parâmetros:
    -----------
    x0, x1 : float
        Dois chutes iniciais distintos, ambos > 0.
    e : float
        Tolerância de erro para o critério de parada.
    max_iter : int, opcional
        Número máximo de iterações permitidas.

    Retorna:
    --------
    (raiz, iteracoes) : (float, int)
        raiz : estimativa da raiz,
        iteracoes : número de iterações realizadas.

    Possíveis erros:
    ----------------
    - Se x0 <= 0 ou x1 <= 0, retorna (None, 0).
    - Se fx1 - fx0 == 0, não é possível calcular a próxima iteração (divisão por zero).

    Como consertar:
    ---------------
    - Escolher x0 e x1 > 0 e f(x0) != f(x1) para evitar divisão por zero.
    """
    if x0 <= 0 or x1 <= 0:
        return None, 0

    iteracoes = 0
    while iteracoes < max_iter:
        fx0, fx1 = f(x0), f(x1)

        if fx1 - fx0 == 0:
            # Evita divisão por zero
            return None, iteracoes

        # Fórmula do método da secante
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

        if x2 <= 0 or abs(x2 - x1) < e:
            return x2, iteracoes + 1

        x0, x1 = x1, x2
        iteracoes += 1

    return None, iteracoes

#  MÉTODO DE PONTO FIXO


def ponto_fixo(g, x0, e, max_iter=1000):
    """
    Método de Ponto Fixo para encontrar raízes de f(x),
    dadas por uma função de iteração x_{n+1} = g(x_n).

    Parâmetros:
    -----------
    g : function
        Função de iteração que deve satisfazer x = g(x) na raiz.
    x0 : float
        Chute inicial, deve ser > 0 para essa função específica.
    e : float
        Tolerância de erro para o critério de parada.
    max_iter : int, opcional
        Número máximo de iterações permitidas.

    Retorna:
    --------
    (raiz, iteracoes) : (float, int)
        raiz : valor que satisfaz x = g(x),
        iteracoes : número de iterações até convergir ou chegar em max_iter.

    Possíveis erros:
    ----------------
    - Se x0 <= 0, retorna (None, 0).
    - A função g pode levar a um x1 <= 0, o que invalida o domínio de f(x).

    Como consertar:
    ---------------
    - Escolher adequadamente g(x) e x0 para garantir convergência (|g'(x)| < 1).
    - Garantir x0 > 0.
    """
    if x0 <= 0:
        return None, 0

    iteracoes = 0
    while iteracoes < max_iter:
        x1 = g(x0)  # aplica a função de iteração

        # Se x1 <= 0, não é válido no domínio de f(x)
        if x1 <= 0 or abs(x1 - x0) < e:
            return x1, iteracoes + 1

        x0 = x1
        iteracoes += 1

    return None, iteracoes

#  MÉTODO DA POSIÇÃO FALSA


def posicao_falsa(a, b, e, max_iter=1000):
    """
    Método da Posição Falsa (Regula Falsi) para encontrar raízes de f(x) no intervalo [a, b].

    Parâmetros:
    -----------
    a, b : float
        Extremos do intervalo [a, b], ambos > 0.
    e : float
        Tolerância de erro para o critério de parada.
    max_iter : int, opcional
        Número máximo de iterações permitidas.

    Retorna:
    --------
    (raiz, iteracoes) : (float, int)
        raiz : estimativa da raiz,
        iteracoes : número de iterações realizadas.

    Possíveis erros:
    ----------------
    - Se a <= 0 ou b <= 0, retornamos (None, 0).
    - Se f(a)*f(b) >= 0, não há garantia de mudança de sinal no intervalo, retorna (None, 0).
    - Podem ocorrer problemas de convergência lenta em alguns casos.

    Como consertar:
    ---------------
    - Verificar se a < b e ambos > 0.
    - Verificar se f(a)*f(b) < 0 para garantir mudança de sinal.
    """
    if a <= 0 or b <= 0:
        return None, 0

    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        return None, 0

    iteracoes = 0
    while abs(b - a) > e and iteracoes < max_iter:
        # c é calculado usando a fórmula do método da Posição Falsa
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)

        if fc == 0:
            return c, iteracoes

        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

        iteracoes += 1

    return (a + b) / 2, iteracoes

#  FUNÇÃO PARA ENCONTRAR MÚLTIPLAS RAÍZES


def encontrar_raizes(metodo, intervalo, e, num_subintervalos=100, **kwargs):
    """
    Encontra múltiplas raízes de f(x) usando um método numérico específico, 
    testando vários subintervalos dentro de 'intervalo'.

    Parâmetros:
    -----------
    metodo : function
        Função que implementa um dos métodos numéricos (bisseccao, posicao_falsa, newton_raphson, secante, ponto_fixo).
    intervalo : (float, float)
        Tupla com o intervalo (a, b) onde procuramos as raízes (a < b, ambos > 0).
    e : float
        Tolerância de erro para o critério de parada.
    num_subintervalos : int
        Quantidade de subintervalos em que [a, b] será dividido para buscar raízes.
    **kwargs : dict
        Parâmetros adicionais que podem ser passados ao método (por exemplo, função g para ponto fixo).

    Retorna:
    --------
    (raizes, iteracoes_totais) : (list, int)
        raizes : lista de tuplas (raiz, iteracoes) para cada raiz encontrada,
        iteracoes_totais : soma das iterações de todos os subintervalos.

    Possíveis erros:
    ----------------
    - Se método não for uma das funções esperadas, pode dar comportamento inesperado.
    - Se a <= 0 ou b <= 0, o próprio método deve falhar.

    Como consertar:
    ---------------
    - Garantir que o método seja um dos métodos listados.
    - Ajustar subintervalos caso seja necessário maior resolução.
    - Se o método for ponto_fixo, passar a função 'g' em kwargs.
    """
    a, b = intervalo
    subintervalo_tamanho = (b - a) / num_subintervalos
    raizes = []
    iteracoes_totais = 0

    for i in range(num_subintervalos):
        a_sub = a + i * subintervalo_tamanho
        b_sub = a + (i + 1) * subintervalo_tamanho

        try:
            # Verifica qual método está sendo chamado e chama com os parâmetros adequados
            if metodo.__name__ in ["bisseccao", "posicao_falsa"]:
                raiz, iteracoes = metodo(a_sub, b_sub, e, **kwargs)
            elif metodo.__name__ == "newton_raphson":
                x0 = (a_sub + b_sub) / 2
                raiz, iteracoes = metodo(x0, e, **kwargs)
            elif metodo.__name__ == "secante":
                x0, x1 = a_sub, b_sub
                raiz, iteracoes = metodo(x0, x1, e, **kwargs)
            elif metodo.__name__ == "ponto_fixo":
                x0 = (a_sub + b_sub) / 2
                g = kwargs.get("g")
                if not g:
                    # Se a função g não for fornecida, não há como executar o método de ponto fixo
                    raise ValueError(
                        "Função 'g' não fornecida para o método de ponto fixo.")

                # Remove 'g' de kwargs para evitar conflitos ao repassar kwargs
                kwargs_sem_g = {k: v for k, v in kwargs.items() if k != "g"}
                raiz, iteracoes = metodo(g, x0, e, **kwargs_sem_g)
            else:
                # Caso surja algum método desconhecido, ignoramos
                continue

            # Se raiz não for None, significa que o método retornou alguma solução
            if raiz is not None:
                # Adicionamos à lista e somamos as iterações
                raizes.append((raiz, iteracoes))
                iteracoes_totais += iteracoes

        except ValueError:
            # Se ocorrer algum ValueError (por exemplo, x <= 0), ignoramos esse subintervalo
            continue

    return raizes, iteracoes_totais


def main():
    """
    Função principal para executar todos os métodos numéricos no intervalo (1.0, 20.0), 
    usando tolerância de e = 1e-6 e 100 subintervalos.

    - Aplica cada método numérico (Bissecção, Newton-Raphson, Secante, Ponto Fixo, Posição Falsa)
      e imprime as raízes encontradas juntamente com o número de iterações.

    Possíveis erros:
    ----------------
    - Se não houver mudança de sinal em nenhum subintervalo, pode não encontrar raízes.
    - Se a função 'g' em ponto fixo não for bem escolhida, pode não convergir.

    Como consertar:
    ---------------
    - Ajustar o intervalo se necessário.
    - Aumentar num_subintervalos para uma busca mais refinada.
    - Verificar a definição de g(x) para o método de ponto fixo.
    """
    intervalo = (1.0, 20.0)
    e = 1e-6
    num_subintervalos = 100

    # Método da Bissecção
    print("Método da Bissecção:")
    raizes, iteracoes = encontrar_raizes(
        bisseccao, intervalo, e, num_subintervalos)
    for raiz, it in raizes:
        print(f"Raiz: {raiz:.6f}, Iterações: {it}")
    print(f"Iterações totais: {iteracoes}\n")

    # Método de Newton-Raphson
    print("Método de Newton-Raphson:")
    raizes, iteracoes = encontrar_raizes(
        newton_raphson, intervalo, e, num_subintervalos)
    for raiz, it in raizes:
        print(f"Raiz: {raiz:.6f}, Iterações: {it}")
    print(f"Iterações totais: {iteracoes}\n")

    # Método da Secante
    print("Método da Secante:")
    raizes, iteracoes = encontrar_raizes(
        secante, intervalo, e, num_subintervalos)
    for raiz, it in raizes:
        print(f"Raiz: {raiz:.6f}, Iterações: {it}")
    print(f"Iterações totais: {iteracoes}\n")

    # Método de Ponto Fixo
    print("Método de Ponto Fixo:")

    def g(x):
        # Aqui estamos escolhendo g(x) = x - f(x)/df(x), algo como uma única iteração de Newton;
        # nem sempre converge como método de ponto fixo puro, mas serve como exemplo.
        return x - f(x) / df(x)

    raizes, iteracoes = encontrar_raizes(
        ponto_fixo, intervalo, e, num_subintervalos, g=g)
    for raiz, it in raizes:
        print(f"Raiz: {raiz:.6f}, Iterações: {it}")
    print(f"Iterações totais: {iteracoes}\n")

    # Método da Posição Falsa
    print("Método da Posição Falsa:")
    raizes, iteracoes = encontrar_raizes(
        posicao_falsa, intervalo, e, num_subintervalos)
    for raiz, it in raizes:
        print(f"Raiz: {raiz:.6f}, Iterações: {it}")
    print(f"Iterações totais: {iteracoes}\n")


# Chama a função principal somente se esse arquivo for executado diretamente.
if __name__ == "__main__":
    main()
