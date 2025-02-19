# Ap1X - Questão 2


def NumerosPerfeitos(inteiro):
    soma = 0
    for x in range(1, inteiro):
        if inteiro % x == 0:
            soma += x
    if soma == inteiro:
        return inteiro


# Programa Principal
numeros = input().split()
if numeros == []:
    print("Nenhum Número Foi Lido!!!")
else:
    print("Relação de Números Perfeitos:")
    for item in numeros:
        inteiro = int(item)
        if NumerosPerfeitos(inteiro):
            print(inteiro)
    print("Fim da Relação.")
