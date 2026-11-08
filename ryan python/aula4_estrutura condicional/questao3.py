quantidade = int(input("Digite a quantidade de produtos: "))

if quantidade <= 3:
    preço = 40
else:
    preço = 35

total = quantidade * preço

print(f"O valor total da compra é R$ {total:.2f}")