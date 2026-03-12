def estudiantes_dp(entrada):
    estudiantes = entrada.split()
    n = int(estudiantes[0])

    nombres = []
    notas = []
    j = 1

    for _ in range(n):
        nombres.append(estudiantes[j])
        notas.append(float(estudiantes[j + 1]))
        j += 2

    memoizacion = {0: 0.0}

    def dinamic (i):

        if i in memoizacion:
            return memoizacion[i]
        memoizacion[i] = dinamic(i - 1) + notas[i - 1]
        return memoizacion[i]

    suma_total = dinamic(n)
    prom = suma_total / n

    encima = []
    for i in range(n):
        if notas[i] > prom:
            encima.append(nombres[i])

    return prom, encima

def main():

    entrada = "5 ana 3.5 luis 4.2 maria 2.8 juan 4.0 sofia 3.9"

    promedio, encima = estudiantes_dp(entrada)

    print("promedio:", promedio)
    print("encima del promedio:")
    for nombre in encima:
        print(nombre)

main()
