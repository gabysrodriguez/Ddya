def minimo(A):
    menor = 0
    mayor = len(A) - 1

    while menor < mayor:
        mid = menor + (mayor - menor) // 2

        # Si estamos en la parte decreciente
        if A[mid] > A[mid + 1]:
            menor= mid + 1
        else:
            mayor = mid

    return A[menor]
A = [8, 5, 3, 4, 4, 10]
print(minimo(A))
