localizar = input("Digite o nome da pessoa que quer encontrar: ")
nomes = ["Maria","Joao","Paulo","Magali"]

for nome in nomes:
    if nome == localizar:
        print(f"Encontrado: {localizar}")
        break
    else:
        print(f"{localizar} não encontrado.")  
        break      