import math
def metodo_posicao_falsa(func, a, b, tol=0.000001, max_iter=600):
    """
    Método da Posição Falsa para encontrar raízes de uma função.

    Parameters:
    func (function): Função para a qual a raiz será encontrada.
    a (float): Limite inferior do intervalo.
    b (float): Limite superior do intervalo.
    tol (float): Tolerância para o critério de parada.
    max_iter (int): Número máximo de iterações.

    Returns:
    float: Aproximação da raiz encontrada ou None se não convergir.
    """
    if func(a) * func(b) >= 0:
        print("Erro: A função deve ter sinais opostos em a e b.")
        return None

    iter_count = 0
    c = a  # Inicializa a variável para o cálculo da raiz

    while iter_count < max_iter:
        # Calcula o ponto de interseção linear (posição falsa)
        c = b - (func(b) * (b - a)) / (func(b) - func(a))
        fc = func(c)

        if abs(fc) < tol:  # Critério de parada: raiz encontrada
            return c

        # Atualiza os limites do intervalo com base no sinal de fc
        if func(a) * fc < 0:
            b = c
        else:
            a = c

        iter_count += 1

    print("Aviso: Número máximo de iterações atingido.")
    return c  # Retorna a melhor aproximação encontrada

# Função a ser testada
def example_function(x):
    return x**math.log(x) + x**2 - (x**3)*math.sin(x)   # Aqui você pode alterar facilmente a função a ser testada

if __name__ == "__main__":
    # Intervalo inicial
    a = 1
    b = 14

    # Chamando o método da posição falsa
    root = metodo_posicao_falsa(example_function, a, b)

    if root is not None:
        print(f"A raiz aproximada é: {root}")
        # Teste para verificar a solução
        f_root = example_function(root)
        if abs(f_root) < 1e-6:
            print(f"Teste aprovado: f(root) = {f_root}, está próximo de zero dentro da tolerância.")
        else:
            print(f"Teste falhou: f(root) = {f_root}, não está próximo de zero.")
    else:
        print("A raiz não foi encontrada dentro do número máximo de iterações.")


print(example_function(2.583081))

#raiz 1 = 1.5184557222177015  raiz2 = 2.583081  raiz3 = 6.561041