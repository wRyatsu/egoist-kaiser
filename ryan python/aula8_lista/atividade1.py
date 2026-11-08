nome = input("Qual Seu Nome? ")

print(f"Olá {nome}")

estoque = []

# TUPLA
categorias = ("Alimento", "Bebida", "Limpeza", "Higiene")

while True:

    print("-" * 40)
    print(f"{'CONTROLE DE ESTOQUE':^40}")
    print("-" * 40)

    print("1 - Adicionar Item")
    print("2 - Excluir Item")
    print("3 - Mostrar Estoque")
    print("4 - Sair")

    menu = int(input("Escolha Uma Opção: "))
    print()

    # ADICIONAR
    if menu == 1:

        nome_item = input("Nome do Produto: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: R$ "))

        print("\nCategorias:")
        for c in categorias:
            print("-", c)

        categoria = input("Escolha uma categoria: ")

        # DICIONÁRIO
        produto = {
            "nome": nome_item,
            "quantidade": quantidade,
            "preco": preco,
            "categoria": categoria
        }

        estoque.append(produto)

        print("Produto adicionado!")

    # REMOVER
    elif menu == 2:

        remover = input("Qual item deseja remover? ")

        for item in estoque:
            if item["nome"] == remover:
                estoque.remove(item)
                print("Item removido!")
                break

    # MOSTRAR
    elif menu == 3:

        print("\nESTOQUE\n")

        for item in estoque:

            print(f"""
Produto: {item["nome"]}
Quantidade: {item["quantidade"]}
Preço: R$ {item["preco"]:.2f}
Categoria: {item["categoria"]}
            """)

    # SAIR
    elif menu == 4:
        print("Encerrando Programa")
        break

    else:
        print("Opção Inválida")