linhas = 4
colunas = 4
quantidade = 0
matriz = []
for i in range(linhas):
    linha = []
    matriz.append(linha)
    for j in range(colunas):
        numero = float(input(f"Digite o numero para a posição ({1}, {j}) da matriz: "))
        linha.append(numero)
        if numero > 10:
            quantidade += 1


print(f"Quantidade de numeros acima de 10 = {quantidade}")
for linha in matriz:
    print(' '.join(map(str, linha)))
