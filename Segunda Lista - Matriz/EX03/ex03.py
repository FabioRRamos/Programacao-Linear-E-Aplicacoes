matriza = [[0, 3], [2, -5]]
matrizb = [[-2, 4], [0, -1]]
matrizc = [[4, 2], [-6, 0]]
matrizresult = [[0, 0], [0, 0]]


for i in range(2):
    for j in range(2):
        matrizresult[i][j] = matriza[i][j] + matrizb[i][j] - (matrizc[i][j] * 4)


for i in range(2):
    for j in range(2):
        print(f'[{matrizresult[i][j]:^5}]', end='')
    print()
