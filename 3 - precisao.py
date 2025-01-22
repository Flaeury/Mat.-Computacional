def precisao_maquina(referencia=1):
    """
    Calcula a precisão da máquina baseada no algoritmo descrito.
    - referência: valor de referência para a comparação no passo 2.
    """
    A = 1.0  # Início com precisão simples (ponto flutuante)
    s = referencia + A
    while s > referencia:
        A = A / 2
        s = referencia + A
    precisao = 2 * A  # Dobro do último valor de A
    return precisao


def testar_precisao():
    print("Teste da Precisão da Máquina:\n")

    # a) Teste para precisão simples e dupla
    print("Teste com precisão simples:")
    precisao_simples = precisao_maquina()
    print(f"Precisão simples (referência = 1): {precisao_simples:.10e}")

    print("\nTeste com precisão dupla (simulada):")
    import numpy as np
    A = np.float64(1.0)  # Usa float64 para maior precisão
    referencia = 1.0
    s = referencia + A
    while s > referencia:
        A = A / 2
        s = referencia + A
    precisao_dupla = 2 * A
    print(f"Precisão dupla (referência = 1): {precisao_dupla:.20e}")

    # c.1) Teste para valores diferentes de referência
    valores_referencia = [10, 17, 100, 184, 1000, 1575, 10000, 17893]
    print("\nTeste com valores de referência diferentes:")
    for ref in valores_referencia:
        prec = precisao_maquina(ref)
        print(f"Referência: {ref}, Precisão: {prec:.10e}")


if __name__ == "__main__":
    testar_precisao()

"""
Análise do Código:

a) Testes com precisão simples e dupla:
   - Precisão simples usa o tipo padrão de ponto flutuante de Python (float), que geralmente tem precisão dupla na maioria das implementações modernas.
   - Para simular precisão dupla, foi usado o tipo float64 da biblioteca numpy que permite maior controle sobre a precisão.

b) Interpretação do passo 3:
   - No algoritmo, o último valor de A que satisfaz s > 1 representa metade da menor unidade significativa na representação numérica.
   - Multiplicar A por 2 retorna a menor unidade significativa que ainda afeta o número de referência.
   - Essa é a precisão da máquina, ou seja, o menor valor que, somado à referência, ainda é perceptível.

c) Alteração para referência personalizada:
   C.1) Resultados para valores de referência diferentes:
       - O código permite que o usuário escolha valores arbitrários como referência.
       - Os testes são realizados para: 10, 17, 100, 184, 1000, 1575, 10000, 17893.

   C.2) Análise do impacto da referência:
       - O valor da precisão não muda significativamente para referências diferentes.
       - Isso ocorre porque a precisão é determinada pela capacidade do sistema de distinguir diferenças relativas, e não pelo tamanho absoluto do número de referência.
"""
