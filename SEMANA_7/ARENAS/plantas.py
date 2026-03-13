import math
import os
import random
import re
import sys

def poisonousPlants(p):
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


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()

        stack.append((pesticida, dias))
        i += 1

    return maximo_dias
