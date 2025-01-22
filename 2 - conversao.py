def binario_para_decimal(binario):
    """
    Converte um número binário (string) para decimal (inteiro).
    """
    try:
        decimal = int(binario, 2)
        return decimal
    except ValueError:
        return "Entrada inválida. Certifique-se de que o número binário contém apenas 0s e 1s."


def decimal_para_binario(decimal):
    """
    Converte um número decimal (inteiro) para binário (string).
    """
    try:
        decimal = int(decimal)
        binario = bin(decimal)[2:]  # Remove o prefixo '0b'
        return binario
    except ValueError:
        return "Entrada inválida. Certifique-se de que o número decimal seja um inteiro."


# Menu de interação com o usuário
if __name__ == "__main__":
    print("Conversor Binário <-> Decimal")
    print("1. Binário para Decimal")
    print("2. Decimal para Binário")
    escolha = input("Escolha uma opção (1 ou 2): ")

    if escolha == "1":
        binario = input("Digite um número binário: ")
        print(f"O número binário {binario} em decimal é: {
              binario_para_decimal(binario)}")
    elif escolha == "2":
        decimal = input("Digite um número decimal: ")
        print(f"O número decimal {decimal} em binário é: {
              decimal_para_binario(decimal)}")
    else:
        print("Opção inválida. Escolha 1 ou 2.")
