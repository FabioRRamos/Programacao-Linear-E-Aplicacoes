matriz = [[1, -1, 0],
          [2, 3, 4],
          [0, 1, -2]]

matrizresult = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

matrizt = list(map(list, zip(*matriz)))


print('Matriz A:')
for j in matriz:
    print(f'{j}')
print()

print('Matriz A Transposta:')
for j in matrizt:
    print(j)

for l in range(0, 3):
    for c in range(0, 3):
        matrizresult[l][c] = matriz[l][c] + matrizt[l][c]


print()

print('Matriz B = A + A Transposta:')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print('[{:^5}]'.format(matrizresult[linha][coluna]), end='')

    print()
