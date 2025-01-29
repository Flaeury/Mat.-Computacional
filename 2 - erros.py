import math


def erro_overflow():
    try:
        grande_numero = math.exp(1000)
        print(f"Número muito grande: {grande_numero}")
    except OverflowError:
        print("Erro de Overflow detectado! O número é muito grande para ser representado.")


def erro_arredondamento():
    numero1 = 0.1
    numero2 = 0.2
    resultado = numero1 + numero2
    print(f"Esperado: 0.3, Obtido: {resultado}")
    print("Erro de arredondamento detectado devido à precisão limitada dos floats.")


if __name__ == "__main__":
    print("Demonstrando erros de Overflow e Arredondamento\n")

    print("1. Erro de Overflow:")
    erro_overflow()

    print("\n2. Erro de Arredondamento:")
    erro_arredondamento()
