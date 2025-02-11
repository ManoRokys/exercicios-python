desc = input("Digite a descrição do produto: ")
precoun = float(input("Digite o preço unitario do produto: "))
qtdcomp = int(input("Digite a quantidade comprada do produto: "))
valortotal = qtdcomp * precoun
print(f"O produto: {desc} custou: R${valortotal}")