def main():
    matrizes = []

    while (True):

        numero = int(input())

        if (numero <= 0):
            break

        matriz = gerarMatriz(numero)

        if (numero > 2):
            reformularMatriz(matriz, numero)

        matrizes.append(matriz)

    imprimir(matrizes)


def gerarMatriz(numero):
    matriz = []

    for i in range(numero):
        matriz.append([1] * numero)

    return matriz


def reformularMatriz(matriz, numero):
    if (numero % 2 == 0):
        limite = int(numero / 2) + 1
    else:
        limite = int(numero / 2) + 2

    inicio = 1
    fim = numero - 1

    for n in range(2, limite):
        for i in range(inicio, fim):
            for j in range(inicio, fim):
                matriz[i][j] = n

        inicio = inicio + 1
        fim = fim - 1


def imprimir(matrizes):
    for i in range(len(matrizes)):
        for j in range(len(matrizes[i])):
            print(("  ") + "   ".join([str(z) for z in matrizes[i][j]]))
        print("")


if __name__ == "__main__":
    main()