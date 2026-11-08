valor = float(input("Qual Valor Do Empréstimo? "))
numero_de_parcelas = float(input("Quantas parcelas? "))
salario = float(input("Quanto você recebe? "))

valor_parcelas = valor / numero_de_parcelas
emprestimo = salario * 0.30

if emprestimo >= valor_parcelas:
    print("Seu Emprestimo Foi Aprovado")
else:
    print("O seu Emprestimo Não Foi Aprovado")



