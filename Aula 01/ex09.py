branco = int(input("Digite o numero de votos em branco: "))
nulo = int(input("Digite o numero de votos nulos: "))
valido = int(input("Digite o numero de votos validos: "))
totalvotos = branco + nulo + valido
branco = (branco*100) / totalvotos
nulo = (nulo*100) / totalvotos
valido = (valido*100) / totalvotos
print(f"O total de votos em porcentagem foi: \nbranco: {branco:.2f}%\nnulo: {nulo:.2f}%\nvalido: {valido:.2f}%")