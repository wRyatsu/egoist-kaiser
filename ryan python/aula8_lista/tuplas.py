coordenadas = (10 , 20) ; print(f"x: (coordenadas[0])")

# Prova de instabilidade
try:
    coordenadas[0] = 30
except TypeError:
    print(f"Erro: não é possivel atribuir a uma tupla")

# Desempacotamento
nome, idade = ("Ana", 22) ; print(f"{nome} tem {idade} anos")