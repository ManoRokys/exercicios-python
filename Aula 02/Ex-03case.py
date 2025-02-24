U = float(input("Digite o valor da tensão: "))
R = float(input("Digite o valor da resistencia: "))
i = float(input("Digite o valor da corrente: "))

calc = int(input("Para descobrir alguma das grandezas eletricas abaixo digite uma das opções:\n1- Tensão(em Volt)\n2- Resistencia(em Ohm)\n3- Corrente(em Ampere)\n"))

match calc:
    case 1:
        U = R * i
        print(f"A tensão foi {U}")
    case 2:    
        R = U / i
        print(f"A Resistencia foi {R}")
    case 3:
        i = U / R
        print(f"A Corrente foi {i}")
    case _:
        print("Digite uma opção válida")    