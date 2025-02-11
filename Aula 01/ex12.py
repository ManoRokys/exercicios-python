altpar = float(input("Digite a altura da parede: "))
larpar = float(input("Digite a largura da parede: "))
altazu = float(input("Digite a altura do azulejo: "))
larazu = float(input("Digite a largura do azulejo: "))
areapar = altpar * larpar
areaazu = altazu * larazu
qtdnec = areapar / areaazu
print(f"A quantidade necessaria de azulejos é: {qtdnec}")