salatual = int(input("Digite o valor do salario atual: "))
reajuste = int(input("Digite o percentual de reajuste: "))
reajuste = salatual * reajuste/100
salnovo = salatual + reajuste
print(f"O salario novo após o reajuste será R${salnovo}")