def f(x):
    # Defina aqui a função f(x) que o usuário deseja analisar.
    # Exemplo: f(x) = x^2 - 4 (Raízes em x=2 e x=-2)
    return x**2 - 4


def mostrar_tabela(intervalo_inferior, intervalo_superior, passo):
    # Inicializando a variável para o primeiro valor de f(x)
    x_anterior = intervalo_inferior
    f_anterior = f(x_anterior)

    # Exibindo o cabeçalho da tabela
    print(" x       | f(x)      | Troca de Sinal?")
    print("------------------------------")

    # Percorrendo o intervalo
    for x in range(intervalo_inferior, intervalo_superior + 1, passo):
        f_x = f(x)

        # Verificando se houve troca de sinal entre f(x) e f(x_anterior)
        if f_x * f_anterior < 0:
            troca_sinal = "Sim"
            print(f" {x:8} | {f_x:8}   | {troca_sinal}")
        f_anterior = f_x

# Função principal


def main():
    # Entrada do usuário para o intervalo e passo
    intervalo_inferior = int(
        input("Digite o valor inferior do intervalo (padrão -10): ") or -10)
    intervalo_superior = int(
        input("Digite o valor superior do intervalo (padrão 10): ") or 10)
    passo = int(input("Digite o valor do passo (padrão 1): ") or 1)

    # Mostrar tabela com os valores de x e f(x) para o intervalo fornecido
    mostrar_tabela(intervalo_inferior, intervalo_superior, passo)


# Executando o programa
if __name__ == "__main__":
    main()
