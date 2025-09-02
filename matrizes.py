# def criar_matriz(linhas, colunas):
#     matriz = []
#     for i in range(linhas):
#         linha = []
#         for j in range(colunas):
#             linha.append('.')
#         matriz.append(linha)
#     return matriz

# def diagonal_inversa(n):
#     m = criar_matriz(n,n)
#     coluna = n-1
#     for linha in range(0,n): #0,1,2,3...n-1
#         m[linha][coluna] = 'x'
#         coluna = coluna -1
#     return m 

def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append('.')
        matriz.append(linha)
    return matriz

def m_borda(linhas, colunas):
    matriz = criar_matriz(linhas, colunas)
    # preencher a primeira linha 
    for i in range(colunas):
        matriz[0][i] = 'x'
        matriz[linhas-1][i] = 'x'
        for i in range(linhas):
            matriz[i][0] = 'x'
            matriz[i][colunas-1] = 'x'
    return matriz

print (m_borda(4,3))
