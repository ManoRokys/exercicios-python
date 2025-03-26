nomes = []

for i in range(1,8):
    nome = input(f"Digite o {i}º nome: ")
    nomes.append(nome)
    i += 1
print("Nomes digitados: ")
for nome in nomes:
    for i in range(1,8):
    print(f"O {i}º nome armazenado é {nome}")    
        i+= 1    