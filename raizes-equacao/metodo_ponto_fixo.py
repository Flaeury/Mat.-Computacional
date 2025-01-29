def metodo_ponto_fixo(g, x0, tol=1e-6, max_iter=100):
    """
    Método do Ponto Fixo para encontrar as raízes de uma função f(x).

    Parâmetros:
        g (function): Função g(x) que define a transformação x = g(x).
        x0 (float): Chute inicial para o método.
        tol (float): Tolerância para o critério de parada (default: 1e-6).
        max_iter (int): Número máximo de iterações (default: 100).

    Retorna:
        float: Aproximação para a raiz.
        int: Número de iterações realizadas.

    Lança:
        ValueError: Se o método não convergir dentro do número máximo de iterações.
    """
    x_atual = x0

    for i in range(1, max_iter + 1):
        x_proximo = g(x_atual)
        
        # Critério de parada: diferença entre iterações
        if abs(x_proximo - x_atual) < tol:
            return x_proximo, i

        x_atual = x_proximo

    raise ValueError("O método não convergiu dentro do número máximo de iterações.")

# Exemplo de uso para encontrar a raiz de f(x) = x^2 - 5
def g(x):
    return 0.5 * (x + 5 / x)  # g(x) é derivada de f(x) = x^2 - 5

def f(x):
    return x**2 - 5

if __name__ == "__main__":
    # Definições do exemplo
    x0 = 1.0  # Chute inicial
    tol = 1e-6

    try:
        # Executando o método do ponto fixo
        raiz, iteracoes = metodo_ponto_fixo(g, x0, tol)
        print(f"A raiz encontrada é x = {raiz:.6f} após {iteracoes} iterações.")
        
        # Teste para verificar a solução
        f_raiz = f(raiz)
        if abs(f_raiz) < tol:
            print(f"Teste aprovado: f({raiz:.6f}) = {f_raiz:.6e}, está próximo de zero.")
        else:
            print(f"Teste falhou: f({raiz:.6f}) = {f_raiz:.6e}, não está próximo de zero.")
    except ValueError as erro:
        print(erro)
