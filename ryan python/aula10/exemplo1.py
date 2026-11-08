try:
    resultado = 10/0
except ZeroDivisionError:
    print("Valor nao pode ser dividido por zero.")
finally:
    print(f"O resultado e:{resultado}")
    print("encerrando a sessao.")