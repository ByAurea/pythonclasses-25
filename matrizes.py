#exercício 1 
#Fazer uma função que produz uma das diagonais da matriz 
#A função chamaria matriz_diagonal, se eu chamar matriz_diagonal(5), ela produz
# x....
# .x...
# ..x..
# ...x.
# ....x
#Ela tem um unico argumento (no caso 5), e produz uma matriz quadrada

def matrizQualquer(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append = '.'
            matriz.append(linha)
    return matriz

def matrizDiagonal(tamanho):
    matriz=matrizQualquer(tamanho)
    for i in range(tamanho):
        matriz[i][i]='x'
    return matriz