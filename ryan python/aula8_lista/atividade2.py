nome = input("Qual Seu Nome? ")

print(f"Olá {nome}")

estoque = []
#  tuplas
categorias = ("Alimento", "Bebidas", "Limpezas", "Higiene")

while True:
    
    print("-"*40)
    print(f"{"Controle De Estoque":^40}")
    print("-"*40)
    
    print("1-Adicionar Item ")
    print("2-Excluir Item ")
    print("3-Mostrar Estoque ")
    print("4-Sair ")
    
    menu = int(input("Escolha Uma Opção: "))
    print()
    
    # adicionar

    if menu == 1:
        nome_item = input("Nome Do Produto:")
        quantidade = int(input("Quantidade:"))
        preço = float(input("Preço: R$ "))
        
        print("Categorias")
        for c in categorias:
            print("-", c)

        categoria = input("Escolha Uma categoria:")

    # dicionario
    produto = {
        "nome": nome_item,
        "quantidade": quantidade,
        "preço": preço,
        "categoria": categoria
    }

    estoque.append(produto)

    print("Produto Adicionado")

    elif
    
#remover
    


