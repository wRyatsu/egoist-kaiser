nome = input("Qual Seu Nome ")

print(f"Olá {nome}")

lista = []

while True:
    print("Digite 1 para adicionar ")
    print("Digite 2 para excluir ")
    print("Digite 3 para mostrar ")
    print("Digite 4 para sair ")
    menu = int(input("Escolha Uma Opção: "))
    if menu == 1:
        tarefa = input("Adicione uma tarefa ")
        lista.append (tarefa)
    elif menu == 2:
        remover = input("Qual Tarefa Você Deseja Remover? ")
        lista.remove (remover)
    elif menu == 3:
        for i in lista:
            print(i)
    elif menu == 4:
        print("Encerrando Programa")
        break

    else:
        print("Opção Inválida")


