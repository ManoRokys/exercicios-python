sal = float(input("Digite o valor do salário: "))

cat = input("Qual é a sua categoria?\nA- Categoria A \nB- Categoria B\nC- Categoria C\n")

match cat:
    case "a":
        sal = sal + (sal/100) * 10
        print(f"O seu salário final será: {sal}")
    case "b":
        sal = sal + (sal/100) * 15
        print(f"O seu salário final será: {sal}")
    case "c":
        sal = sal + (sal/100) * 25
        print(f"O seu salário final será: {sal}")
    case _:
        print("Por favor, digite uma categoria válida")