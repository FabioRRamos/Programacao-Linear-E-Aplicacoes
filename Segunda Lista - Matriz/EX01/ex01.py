matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print('*-**-**-**-**-**-**')
for linha in range(3):

    for coluna in range(2):

       if linha == coluna:
           matriz[linha][coluna] = 1


       else:
            matriz[linha][coluna] = (linha+1) ** 2


for l in range(3):

    for c in range(2):

        print('[{:^7}]'.format(matriz[l][c]), end='')

    print()
print('*-**-**-**-**-**-**')
