linhas = 2
colunas = 3
matriz = []
for i in range(linhas):
    linha = []
    matriz.append(linha)
    for j in range(colunas):
        capital = input(f"Digite uma capital para a posição ({1}, {j}) da matriz: ")
        linha.append(capital)
        
for linha in matriz:
    print(' '.join(map(str, linha)))