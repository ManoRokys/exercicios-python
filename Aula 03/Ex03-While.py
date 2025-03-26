num = int(input("Digite o número que você quer saber a tabuada: "))
count = 1
print(f"Tabuado do: {num}")
while (count <= 10):
    resultado = num * count
    print(f"{num} X {count} = {resultado}")
    count += 1