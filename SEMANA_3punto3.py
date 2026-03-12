def potencia(a, n):
    if n == 0:
        return 1

    mitad = potencia(a, n // 2)

    if n % 2 == 0:
        return mitad * mitad
    else:
        return a * mitad * mitad
a=4
n=2
print(potencia(4,2))
