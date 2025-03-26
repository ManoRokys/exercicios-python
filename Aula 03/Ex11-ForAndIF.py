decisao = 2
while (decisao != 0):
    decisao = int(input("Gostaria de buscar um nome? Digite 1\nSair do Aplicativo? Digite 0\n"))

    if decisao == 1:
        localizar = input("Digite o nome da pessoa que quer encontrar: ")
        nomes = ["Maria","Joao","Paulo","Magali"]

        for nome in nomes:
            if nome == localizar:
                print(f"Encontrado: {localizar}")
        
            else:
                print(f"{localizar} não encontrado.")
    elif decisao == 0:
        break

    else: 
        print("Digite uma opção válida")              
              

