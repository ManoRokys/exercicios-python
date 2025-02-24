peso = float(input("Digite o seu peso: "))

planet = int(input("Escolha o planeta que você quer consultar seu peso\n1-Mercúrio\n2-Vênus\n3-Marte\n4-Júpiter\n5-Saturno\n"))

match planet:
    case 1: 
        peso = peso * 0.37
        print(f"O seu peso em Mercúrio é: {peso}")
    case 2: 
        peso = peso * 0.88
        print(f"O seu peso em Vênus é: {peso}")
    case 3: 
        peso = peso * 0.38
        print(f"O seu peso em Marte é: {peso}")
    case 4: 
        peso = peso * 2.64
        print(f"O seu peso em Júpiter é: {peso}")
    case 5: 
        peso = peso * 1.15
        print(f"O seu peso em Saturno é: {peso}")    
    case _:
        print("Por favor, digite um planeta válido")                

