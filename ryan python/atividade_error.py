numero = int("12a")

try:
    numero = int("12a")
except ValueError:
    print("somente numero inteiro")
finally:
    print("execution finally")
