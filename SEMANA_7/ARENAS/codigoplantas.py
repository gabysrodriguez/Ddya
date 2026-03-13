import sys

q = int(input())

stack1 = []
stack2 = []

i = 0
while i < q:
    consulta = list(map(int, input().split()))
    tipo = consulta[0]

    if tipo == 1:
        x = consulta[1]
        stack1.append(x)

    elif tipo == 2:
        if len(stack2) == 0:
            while len(stack1) > 0:
                stack2.append(stack1.pop())
        stack2.pop()

    elif tipo == 3:
        if len(stack2) == 0:
            while len(stack1) > 0:
                stack2.append(stack1.pop())
        print(stack2[-1])

    i += 1
