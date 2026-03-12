def ordenar(letras):
    if len(letras) <= 1:
        return letras

    mitad= len(letras) // 2
    izquierda= ordenar(letras[:mitad])
    derecha= ordenar(letras[mitad:])

    return mezclar(izquierda, derecha)


def mezclar(izquierda, derecha):
    resultado= []
    i= 0
    j= 0

    while i< len(izquierda) and j< len(derecha):
        if izquierda[i]<= derecha[j]:
            resultado.append(izquierda[i])
            i+= 1
        else:
            resultado.append(derecha[j])
            j+= 1

    while i< len(izquierda):
        resultado.append(izquierda[i])
        i+= 1

    while j< len(derecha):
        resultado.append(derecha[j])
        j+= 1
    return resultado

palabra= "ALGORITMO"
letras_ordenadas= ordenar(list(palabra))

for letra in letras_ordenadas:
    print(letra, end="")
print()
