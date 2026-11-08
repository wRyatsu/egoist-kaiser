tempo_de_serviço = int(input("Quantos Anos De Empresa você tem?"))
salario = float(input("Quanto Você recebe atualmente?"))

if tempo_de_serviço >= 5:
    bonus = salario * 0.20
else:
    bonus = salario * 0.10

reajuste = salario + bonus

print(f"Seu Salário Após o reajuste é {reajuste}")

