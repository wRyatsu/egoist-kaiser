produto = {"nome": "Smartphone X", "preço": 1500.00 , "estoque": 50}

produto.pop("estoque")

# acesso e atualização
print(produto["nome"])
produto["preço"] = 1450.00
produto["cor"] = "Preto"

# interação
for chave, valor in produto.items(): print(f"{chave}: {valor}")

# remoção
