num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

opcao = int(input("Escolha uma das opções: \n1-Fazer Media Ponderada, com pesos 2 e 3, respectivamente. \n2-Fazer o Quadrado da soma dos 2 numeros. \n3-Cubo do menor numero.\n "))

if opcao == 1:
    resultado = (num1 * 2 + num2 * 3) / 5
    print(f"O resultado da opção escolhida foi: {resultado}")
elif opcao == 2:
    resultado = num1 + num2
    resultado = pow(resultado,2)
    print(f"O resultado da opção escolhida foi: {resultado}")
elif opcao == 3:
    if num1 > num2:
        num2 = pow(num2,3)
        print(f"O resultado da opção escolhida foi: {num2}")
    elif num2 > num1:
        num1 = pow(num1,3)
        print(f"O resultado da opção escolhida foi: {num1}")
    else:
        print("Os dois numeros são iguais.")    
else: 
    print("Digite uma opção valida")           