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
    for matriz in matrizes:
        for i in range(len(matriz)):
            print("%3d" % matriz[i][0], end="")
            for j in range(1, len(matriz[i])):
                print("%4d" % matriz[i][j], end="")
            print("")
        print("")


if __name__ == "__main__":
    main()