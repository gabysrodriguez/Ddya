def plantas(p):
    stack = []
    maximo_dias = 0
    i = 0

    while i < len(p):
        pesticida = p[i]
        dias = 0

        while len(stack) > 0 and pesticida <= stack[-1][0]:
            ultimo = stack.pop()
            if ultimo[1] > dias:
                dias = ultimo[1]

        if len(stack) == 0:
            dias = 0
        else:
            dias = dias + 1

        if dias > maximo_dias:
            maximo_dias = dias

        stack.append((pesticida, dias))
        i += 1

    return maximo_dias
