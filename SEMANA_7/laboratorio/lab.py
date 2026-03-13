def sistema_pacientes():

    cola_normales = []
    cola_criticos = []

    n = int(input())

    i = 0
    while i < n:

        entrada = input().split()
        accion = entrada[0]

        if accion == "N":

            nombre = entrada[1]
            cola_normales.append(nombre)
            print("Paciente N nuevo :", nombre)

        elif accion == "C":

            nombre = entrada[1]
            cola_criticos.append(nombre)
            print("Paciente C nuevo :", nombre)

        elif accion == "A":

            if len(cola_criticos) > 0:

                paciente = cola_criticos[0]
                cola_criticos.pop(0)
                print("Se atiende a", paciente)

            elif len(cola_normales) > 0:

                paciente = cola_normales[0]
                cola_normales.pop(0)
                print("Se atiende a", paciente)

            else:

                print("no hay pacientes")

        i = i + 1


sistema_pacientes()
