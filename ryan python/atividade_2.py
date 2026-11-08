aluno = {"nome" : "maria"}
print(aluno["idade"])


while True:

 try:
    aluno = {"nome" : "maria"}
    print(aluno["idade"])
 except KeyError:
    print("a idade nao foi feita o cadastro.")
    break
 finally:
    print("execution finaly.")
