# Ap1X - Questão 1

vogaisMinusculas = ["a", "e", "i", "o", "u"]
Numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
LidasComMaisVogaisQueNumeros = []


def numeros(lida):
    QntNumeros = 0
    for m in lida:
        if m in Numeros:
            QntNumeros += 1
    return QntNumeros


def vogais(lida):
    QntVogais = 0
    for m in lida:
        if m in vogaisMinusculas:
            QntVogais += 1
    return QntVogais


def stringlida(lida):
    linhasLidas = 0
    LinhasComMaisDigitos = 0
    while True:
        if lida == "":
            for item in range(len(LidasComMaisVogaisQueNumeros)):
                print(LidasComMaisVogaisQueNumeros[item])
            print("Total de linhas lidas:", linhasLidas)
            return LinhasComMaisDigitos
        else:
            linhasLidas += 1
            vogal = vogais(lida)
            numero = numeros(lida)
            if vogal > numero:
                LinhasComMaisDigitos += 1
                LidasComMaisVogaisQueNumeros.append(lida)
            lida = input()


# Programa Principal
lida = input()
print("Total de linhas com mais vogais que dígitos:", stringlida(lida))
