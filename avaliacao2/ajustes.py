import math

t_max = 300

m = 0
inf_w = 0
grau = 1
x = [0.0] * t_max
fx = [0.0] * t_max
w = [0.0] * t_max
a = [[0.0 for _ in range(t_max + 1)] for _ in range(t_max)]
c = [0.0] * t_max


def correlacao(metodo):
    rsup = 0.0
    sfxi = 0.0
    sfxi2 = 0.0
    r = 0.0
    if metodo == 1 or metodo == 3:
        for i in range(m):
            rsup += (fx[i] - faj(x[i], metodo)) ** 2
            sfxi += fx[i]
            sfxi2 += fx[i] ** 2
    else:
        for i in range(m):
            rsup += (math.log(fx[i]) - math.log(faj(x[i], metodo))) ** 2
            sfxi += math.log(fx[i])
            sfxi2 += math.log(fx[i]) ** 2
    r = math.sqrt(1 - (rsup / (sfxi2 - (sfxi ** 2 / m))))
    print(f"\n\n\nCoeficiente de correlacao r={r:10.4f}")


def le_dados():
    global m, inf_w, grau
    print(
        "\n\nDe quantos pontos [x, f(x)] voce dispoe para realizar o ajuste? ")
    m = int(input())
    print("Tecle 'S' caso deseje fornecer os pesos. Qualquer outra tecla para pesos = 1: ")
    tcl = input().strip().upper()
    if tcl == 'S':
        inf_w = 1
    else:
        print("\nAssumindo todos os pesos = 1.\n")
    print("\nPor favor forneça os valores para os pares ordenados: ")
    i = 0
    while i < m:
        x_val = float(input(f"x[{i+1}]="))
        fx_val = float(input(f"f(x[{i+1}])="))
        if x_val > 0 and fx_val > 0:  # Apenas aceita valores positivos
            x[i] = x_val
            fx[i] = fx_val
            if inf_w:
                w[i] = float(input(f"w[{i+1}]="))
            else:
                w[i] = 1.0
            i += 1
        else:
            print(
                "Valores de x e f(x) devem ser positivos para o ajuste de potência. Ignorando ponto.")
    grau += 1


def print_sistema(c1):
    print("\nSistema de equacoes: \n\n")
    for i in range(grau):
        for j in range(grau + 1):
            if j < grau:
                print(f"{a[i][j]:10.4f} ", end="")
                if j == 0:
                    print(f"{c1}1", end="")
                else:
                    print(f"c{j+1}", end="")
                if j < grau - 1:
                    print("+", end="")
            else:
                print(f"= {a[i][j]:10.4f}\n")


def base(indice, x, metodo):
    if metodo == 1:
        return x ** indice
    else:
        return math.log(x) ** indice


def faj(x, metodo):
    y = 0.0
    if metodo == 1:
        for i in range(grau):
            y += c[i] * (x ** i)
    elif metodo == 2:
        y = c[0] * math.exp(c[1] * x)
    elif metodo == 3:
        y = c[0] + c[1] * math.log(x)
    elif metodo == 4:
        y = c[0] * (x ** c[1])
    return y


def resolve_sel():
    for i in range(grau):
        if a[i][i] != 1:
            aux = a[i][i]
            for j in range(grau + 1):
                a[i][j] /= aux
        for k in range(grau):
            if k == i:
                k += 1
                if k >= grau:
                    break
            aux2 = a[k][i]
            for j in range(grau + 1):
                a[k][j] -= aux2 * a[i][j]
    for i in range(grau):
        c[i] = a[i][grau]


def linear():
    global grau
    print("\n\nAjuste de curvas - Metodo de ajuste linear\n\n")
    print("Entre com o grau da funcao que voce deseja ajustar? ")
    grau = int(input())
    grau += 1
    for r in range(grau):
        for s in range(grau):
            a[r][s] = 0.0
            if r == s:
                for i in range(m):
                    a[r][r] += base(r, x[i], 1) * base(r, x[i], 1)
            else:
                for i in range(m):
                    a[r][s] += base(r, x[i], 1) * base(s, x[i], 1)
        a[r][grau] = 0.0
        for i in range(m):
            a[r][grau] += w[i] * fx[i] * base(r, x[i], 1)
    print_sistema('c')
    resolve_sel()
    print("\nFuncao de ajuste:\n\nfaj(x)=", end="")
    for i in range(grau):
        print(f"{c[i]}x^{i}", end="")
        if i < grau - 1 and c[i+1] > 0:
            print("+", end="")
    correlacao(1)


def expone():
    global grau
    print("\n\nAjuste de curvas - Metodo de ajuste exponencial\n\n")
    grau = 2
    for r in range(grau):
        for s in range(grau):
            a[r][s] = 0.0
            if r == s:
                for i in range(m):
                    a[r][r] += base(r, x[i], 1) * base(r, x[i], 1)
            else:
                for i in range(m):
                    a[r][s] += base(r, x[i], 1) * base(s, x[i], 1)
        a[r][grau] = 0.0
        for i in range(m):
            a[r][grau] += w[i] * math.log(fx[i]) * base(r, x[i], 1)
    print_sistema('k')
    resolve_sel()
    c[0] = math.exp(c[0])
    print(f"\nFuncao de ajuste:\n\nfaj(x)={c[0]:6.4f}*exp({c[1]:6.4f}x)")
    correlacao(2)


def logari():
    global grau
    print("Ajuste de curvas - Metodo de ajuste logaritmico\n\n")
    grau = 2
    for r in range(grau):
        for s in range(grau):
            a[r][s] = 0.0
            if r == s:
                for i in range(m):
                    a[r][r] += base(r, x[i], 2) * base(r, x[i], 2)
            else:
                for i in range(m):
                    a[r][s] += base(r, x[i], 2) * base(s, x[i], 2)
        a[r][grau] = 0.0
        for i in range(m):
            a[r][grau] += w[i] * fx[i] * base(r, x[i], 2)
    print_sistema('c')
    resolve_sel()
    print(f"\nFuncao de ajuste:\n\nfaj(x)={c[0]:6.4f}+{c[1]:6.4f}ln(x)")
    correlacao(3)


def potenc():
    global grau
    print("Ajuste de curvas - Metodo de ajuste de potencia\n\n")
    grau = 2
    for r in range(grau):
        for s in range(grau):
            a[r][s] = 0.0
            if r == s:
                for i in range(m):
                    a[r][r] += base(r, x[i], 2) * base(r, x[i], 2)
            else:
                for i in range(m):
                    a[r][s] += base(r, x[i], 2) * base(s, x[i], 2)
        a[r][grau] = 0.0
        for i in range(m):
            a[r][grau] += w[i] * math.log(fx[i]) * base(r, x[i], 2)
    print_sistema('k')
    resolve_sel()
    c[0] = math.exp(c[0])
    print(f"\nFuncao de ajuste:\n\nfaj(x)={c[0]:6.4f}*x^{c[1]:6.4f}")
    correlacao(4)


def main():
    dados = 0
    while True:
        print("\n\nAjuste de Curvas\n---------------------------------\n\n1 - Ajuste linear\n2 - Ajuste exponencial\n3 - Ajuste Logaritmico\n4 - Ajuste de Potencia\n5 - Sair\n\nSelecione o metodo a ser usado: ")
        opcao = input().strip()
        if not dados and opcao != '5':
            le_dados()
            dados = 1
        if opcao == '1':
            linear()
        elif opcao == '2':
            expone()
        elif opcao == '3':
            logari()
        elif opcao == '4':
            potenc()
        elif opcao == '5':
            return
        else:
            print("\nOpcao invalida! Selecione o metodo desejado: ")
        print("\n\nTecle 'S' caso deseje utilizar os mesmos dados para resolver por outro metodo.")
        opcao = input().strip().upper()
        if opcao != 'S':
            dados = 0


if __name__ == "__main__":
    main()
