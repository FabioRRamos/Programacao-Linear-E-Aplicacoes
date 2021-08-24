matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 4):
        if i == j:
            matriz[i][j] = ((i + 1) + (j + 1))
        else:
            matriz[i][j] = ((2 * i) + 1) - ((2 * j) + 1)

a = int(matriz[1][1])
b = int(matriz[2][3])

print('=-' * 15)

for i in range(0, 3):
    for j in range(0, 4):
        print(f'[{matriz[i][j]:^7}]', end='')
    print()

print('\nA soma do valor de a22 e a34 é', a+b)
