# Ap1X - Questão 3


palavras = []


# Foi usado o QuickSort pois é um algoritmo mais eficiente do que os demais, executando em n log2(n) onde
# o fator log2(n) se deve a divisão recursiva do vetor original.

def trocar(valores, posX, posY):
    temp = valores[posX]
    valores[posX] = valores[posY]
    valores[posY] = temp
    return None


def particiona(valores, inicio, fim):
    pivo = valores[inicio]
    i = inicio + 1
    j = fim
    while i < j:
        while i < fim and valores[i] < pivo:
            i += 1
        while j > inicio and valores[j] >= pivo:
            j -= 1
        if i < j:
            trocar(valores, i, j)
    if pivo > valores[j]:
        trocar(valores, inicio, j)
    return j


def quickSort(valores, inicio, fim):
    if inicio < fim:
        posPivo = particiona(valores, inicio, fim)
        quickSort(valores, inicio, posPivo - 1)
        quickSort(valores, posPivo + 1, fim)
    return None


def ordenar(valores):
    quickSort(valores, 0, len(valores) - 1)
    return None


# Programa Principal
N = int(input())
if N > 0:
    for item in range(N):
        palavras.append(input().split())
    ordenar(palavras)
    for item in range(len(palavras)):
        print(*palavras[item])
