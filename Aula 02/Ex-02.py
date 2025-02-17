numero = int(input("Digite um numero: "))

if numero %2 == 0:

    numero = pow(numero,2)
    print(f"O resultado desse numero par elevado ao quadrado é: {numero}")
else:
    numero = pow(numero,3)
    print(f"O resultado desse numero impar elevado ao cubo é: {numero}")