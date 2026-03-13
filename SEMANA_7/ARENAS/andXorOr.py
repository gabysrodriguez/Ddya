def andXorOr(lista):
    pila = []
    mayor = 0

    posicion = 0
    while posicion < len(lista):

        while len(pila) > 0:
            resultado = pila[-1] ^ lista[posicion]

            if resultado > mayor:
                mayor = resultado

            if pila[-1] > lista[posicion]:
                pila.pop()
            else:
                break

        pila.append(lista[posicion])
        posicion += 1

    return mayor
