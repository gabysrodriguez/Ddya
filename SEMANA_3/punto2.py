def numero_faltante(A):
    menor = 0
    mayor = len(A) - 1

    while menor <= mayor:
        mid = menor + (mayor - menor) // 2

        if A[mid] == mid + 1:
            menor = mid + 1
        else:
            mayor = mid - 1

    return menor + 1
A=[1,2,3,4,6,7,8]
print (numero_faltante(A))
