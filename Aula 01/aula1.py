nome = "Rokys"
idade = "19"

print("meu nome é " + nome + " e tenho " + idade + " anos") 

primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))
valortotal = primeiro_valor + segundo_valor
print(valortotal)


valorProduto = float(input("Digite o valor do produto: "))
valorDesconto = float(input("Digite o valor do desconto em %: "))
valorDesconto = valorProduto * valorDesconto/100
valorVenda = valorProduto - valorDesconto
print(f"O valor final da venda é: {valorVenda}")