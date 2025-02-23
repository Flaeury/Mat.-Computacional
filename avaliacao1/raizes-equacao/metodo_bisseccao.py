import math

def metodo_bisseccao(funcao, a, b, tol=1e-6, max_iter=1000):
    """
    Método de Bisseção para encontrar raízes de uma função.

    Parâmetros:
        funcao (function): Função para a qual a raiz será encontrada.
        a (float): Limite inferior do intervalo.
        b (float): Limite superior do intervalo.
        tol (float): Tolerância para o critério de parada.
        max_iter (int): Número máximo de iterações.

    Retorna:
        float: Aproximação da raiz encontrada.
        None: Caso o método não converja.
    """
    if funcao(a) * funcao(b) >= 0:
        print("Erro: A função deve ter sinais opostos em a e b.")
        return None

    cont_iteracoes = 0
    while (b - a) / 2 > tol and cont_iteracoes < max_iter:
        c = (a + b) / 2  # Ponto médio
        fc = funcao(c)

        if fc == 0:  # Encontrou a raiz exata
            return c

        # Verifica em qual subintervalo a raiz está
        if funcao(a) * fc < 0:
            b = c
        else:
            a = c

        cont_iteracoes += 1

    # Retorna a aproximação da raiz
    return (a + b) / 2

# Função de exemplo
def funcao_exemplo(x):
    return x**math.log(x) + x**2 - (x**3)*math.sin(x)  

if __name__ == "__main__":
    # Intervalo inicial
    a = 12
    b = 13
    tol = 1e-6

    print(funcao_exemplo(20))

    # Chamando o método de bisseção
    raiz = metodo_bisseccao(funcao_exemplo, a, b, tol)

    if raiz is not None:
        print(f"A raiz aproximada é: {raiz:.6f}")

        # Teste para verificar a solução
        f_raiz = funcao_exemplo(raiz)
        if abs(f_raiz) < tol:
            print(f"Teste aprovado: f({raiz:.6f}) = {f_raiz:.6e}, está próximo de zero.")
        else:
            print(f"Teste falhou: f({raiz:.6f}) = {f_raiz:.6e}, não está próximo de zero.")
    else:
        print("A raiz não foi encontrada dentro do número máximo de iterações.")
