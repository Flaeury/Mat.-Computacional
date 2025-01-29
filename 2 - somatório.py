def somatorio(x, n):
    # x é o valor a ser somado
    # n é o número de vezes que x será somado, ou seja, de 1 até n.
    total = 0
    for i in range(1, n+1):
        total += x
    return total


print(somatorio(0.5, 30000))
print(somatorio(0.11, 30000))
