from math import pi

raio = float(input("Digite o raio do cilindo: "))
altura = float(input("Digite a altura do cilindo: "))
volume = pi * pow(raio, 2) * altura
print(f"O Volume desse cilindro é: {volume:.2f}")