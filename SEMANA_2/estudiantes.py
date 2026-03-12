def principal():
    A = input("ingrese los elementos de la lista separados por espacio: ").split()

    for i in range(len(A)):
        A[i] = int(A[i])

    for j in range(1, len(A)):
        llave = A[j]
        i = j - 1

        while i >= 0 and A[i] > llave:
            A[i + 1] = A[i]
            i -= 1

        A[i + 1] = llave

    print("La lista ordenada es:", A)

principal()
