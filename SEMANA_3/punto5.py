def encontrar_N(X):
    suma= 0
    N= 0

    while suma < X:
        N += 1

        remplazo= N
        while remplazo > 0:
            if remplazo % 2 == 1:
                suma += 1
            remplazo = remplazo // 2
    return N

print(encontrar_N(5))
