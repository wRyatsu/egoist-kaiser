dias = int(input("Quantos Dias"))
horas = int(input("Quantas Horas"))
minutos = int(input("Quantos minutos"))
segundos = int(input("Quantos segundos"))

diascv = dias * 86400
horascv = horas * 3600
minutoscv = minutos * 60
segundoscv = diascv + horascv + minutoscv + segundos

print(f"a contagem total de segundos é {segundoscv}")