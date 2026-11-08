nota1 = float(input("Qual Sua Primeira Nota?"))
nota2 = float(input("Qual Sua Segunda Nota?"))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Você foi aprovado com a nota {media}")
else:
    print(f"Você foi reprovado com a nota {media}")
