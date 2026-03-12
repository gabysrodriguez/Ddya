def aprobar(datos):
    if len(datos)== 2:
        return [datos[0]] if datos[1] >= 3.0 else []
    mitad= len(datos)//2
    mitad= mitad- (mitad%2)
    izquierda= aprobar(datos[:mitad])
    derecha= aprobar(datos[mitad:])
    return izquierda + derecha
def main():
    lista= input("ingrese nombre y nota separados por espacios: ").split()
    datos= []
    for i in range(0, len(lista), 2):
        datos.append(lista[i])
        datos.append(float(lista[i + 1]))
    apr= aprobar(datos)
    print("Los estudiantes que pasaron son:", apr)

main()
