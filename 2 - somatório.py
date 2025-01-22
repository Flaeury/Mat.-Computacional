def somatorio(x, n):
    total = 0
    for i in range(1, n+1):
        total += x
    return total


print(somatorio(0.5, 30000))
print(somatorio(0.11, 30000))
