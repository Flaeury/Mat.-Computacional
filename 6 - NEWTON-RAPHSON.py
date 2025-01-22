def newton_Raphson(f, df, x0, e, n_Max):
    n = 0
    x_n = x0
    while n < n_Max:
        fn = f(x_n)
        dfn = df(x_n)
        if dfn == 0:
            print(f"A derivada é igual a zero em x = {x_n}. Método falhou.")
            return None

        x_n1 = x_n - fn / dfn

        if abs(x_n1 - x_n) < e:
            print(f"Raiz encontrada: {x_n1}")
            return x_n1

        x_n = x_n1

        n += 1
    print(f"Raiz não encontrada após {n_Max} iterações.")
    return None


def f(x):
    return x**3 - 2*x - 2


def df(x):
    return 2*(x**2) - 2


newton_Raphson(f, df, 1.5, 1e-3, 100000)
