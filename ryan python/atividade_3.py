try:
    numero = 10/2
except ZeroDivisionError:
    print("Numero nao divisivel por zero")
else:
    print(f"O resultado e: {numero}")
finally:
    print("sessao encerrada")