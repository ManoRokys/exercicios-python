valor = 1
count = 1
total = 0
while (valor != 0):
    valor = float(input(f"Produto:{count} R$"))
    total = total + valor
    count += 1
print(f"Valor final da compra: {total}")
pagar = float(input("Digite o preço pago: "))
if pagar == total:
    print(f"Dinheiro pago: R${pagar}\nObrigado pela compra!")
elif pagar > total: 
    troco = pagar - total
    print(f"Dinheiro pago: R${pagar}\nTroco: R${troco}\nObrigado pela compra!")
else:
    print("Pagamento insuficiente :(")     
      
