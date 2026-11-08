saldo = 500
produto1 = 20
produto2 = 30

produto_escolhido = input("Escolha um produto")

if produto_escolhido == "produto1":
    compra = saldo - produto1
    print(f"saldo atual {compra}")

elif produto_escolhido == "produto2":
    compra = saldo - produto2
    print(f"saldo atual {compra}")

else:
    print("Saldo Insuficiente ou Produto Escolhido Inexistente")