import math

def main():
    print("Escolha uma opção\n 1 - Bisseccao \n 2 - Calcular e^x pela Série de Taylor")
    escolha = int(input("Escolha: "))

    if escolha == 1:
        bisseccao(f, a, b, e)
    elif escolha == 2:
        calcular_ex(x, n)


main()


def bisseccao(f, a, b, e):
    i=0
    ai=a
    bi=b

    while abs(bi-ai) > e:
        pi = (ai+bi)/2
        print("a{}: {};  b{}: {};  p{}: {};".format(i,ai,i,bi,i,pi))
        if f(ai)*f(pi)<0:
            bi = pi
        else:
            ai = pi
        i+=1

    return (ai+bi)/2


bisseccao(lambda x:x**3-9*x+3, -4,-2, 0.000000001)
bisseccao(lambda x:x**3-9*x+3, 0,2, 0.000000001)
bisseccao(lambda x:x**3-9*x+3, 2,4, 0.000000001)
bisseccao(lambda x:math.sqrt(x)-5*math.exp(-x), 1,2, 0.000000001)
# bisseccao(lambda x:x*math.log10(x)-1, 2,3, 0.00000000001)

def calcular_ex(x, n):
    resultado = 1  # O primeiro termo da série é sempre 1
    termo = 1      # O primeiro termo é 1 (x^0 / 0!)
    
    for i in range(1, n):  
        termo *= x / i    
        resultado += termo 
    
    return resultado
 
x = float(input("Digite o valor de x: "))
n = int(input("Digite o número de termos (n): "))

resultado = calcular_ex(x, n)

print(f"O valor de e^{x} com {n} termos é: {resultado}")

def newton(f, df, x0, tol=1e-5, max_iter=100):
    iter_count = 0
    while iter_count < max_iter:
        fx = f(x0)
        dfx = df(x0)
        if abs(fx) < tol:
            return x0
        if dfx == 0:
            print("Derivada nula. Método falhou.")
            return None
        x0 = x0 - fx / dfx
        iter_count += 1
    return x0

def secante(f, x0, x1, tol=1e-5, max_iter=100):
    iter_count = 0
    while iter_count < max_iter:
        fx0 = f(x0)
        fx1 = f(x1)
        if abs(fx1 - fx0) < tol:
            return x1
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        x0, x1 = x1, x2
        iter_count += 1
    return x1

def f1(x):
    return x**6 - 2*x**5 + x**4 - 2*x + 1

def f2(x):
    return math.log(x) - 2

def f3(x):
    return math.exp(x) - 5

def f4(x):
    return math.sin(x) - 0.5

def f5(x):
    return x**2 - 4

# Derivadas das funções:
def df1(x):
    return 6*x**5 - 10*x**4 + 4*x**3 - 2

def df2(x):
    return 1/x

def df3(x):
    return math.exp(x)

def df4(x):
    return math.cos(x)

def df5(x):
    return 2*x

def teste_sinal(f, a, b, passos=100):
    intervalo = []
    for i in range(passos + 1):
        x = a + i * (b - a) / passos
        if f(x) == 0:
            intervalo.append(x)
        elif i > 0 and f(x) * f(a + (i-1) * (b - a) / passos) < 0:
            intervalo.append((a + (i-1) * (b - a) / passos, x))
    return intervalo
