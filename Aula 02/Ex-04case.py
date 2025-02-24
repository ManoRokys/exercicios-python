valor = float(input("Digite o valor do pagamento: "))

metodo = int(input("Qual foi o método de pagamento?\n1- À Vista\n2- Débito\n3- Crédito\n"))

match metodo:
    case 1:
        valor = valor - (valor/100) * 15
        print(f"O valor final da compra foi: {valor}")
    case 2:
        valor = valor - (valor/100) * 10
        print(f"O valor final da compra foi: {valor}")
    case 3:
        valor = valor - (valor/100) * 5
        print(f"O valor final da compra foi: {valor}")
    case _:
        print("Por favor, digite um número válido")