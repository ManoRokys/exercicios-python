num = int(input("Digite o número que você quer saber a tabuada: "))
ini = int(input("Digite onde começa essa tabuada: "))
fim = int(input("Digite até onde essa tabuada vai: "))
count = 1
print(f"Tabuada do: {ini}\nDe: {ini}\nAté: {fim}")

while (ini <= fim):
    resultado = num * ini
    print(f"{num} X {ini} = {resultado}")
    ini += 1