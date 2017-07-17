
def main():

    numeroDeTestes = int(input())
    resultados = []

    for t in range(1, numeroDeTestes + 1):

        numeroDePelotoes = int(input())
        string = input().upper()
        string += string

        matriz = getMatriz(64)

        for tam in range(3, numeroDePelotoes + 1, 3):

            for i in range(numeroDePelotoes):

                f = i + (tam - 1)
                for y in range(i + 1, f + 1):

                    for z in range(y + 1, f + 1):

                        c = 0

                        c += int(string[i] == "R") + int(string[y] == "R") + int (string[z] == "R")

                        if c > 1:
                            continue

                        v1 = 1 if y == i + 1 else matriz[i + 1][y - 1]
                        v2 = 1 if z == y + 1 else matriz[y + 1][z - 1]
                        v3 = 1 if f == z else matriz[z + 1][f]
                        matriz[i][f] += v1 * v2 * v3

        resultados.append(matriz[0][numeroDePelotoes - 1])

    imprimeResultados(resultados)

def getMatriz(length):


    matriz = []

    for i in range(length):

        matriz.append([0])

        for j in range(length - 1):

            matriz[i].append(0)

    return matriz


def imprimeResultados(resultados):

    for i in range(len(resultados)):
        print("Case %d: %d" % (i + 1, resultados[i]))




if __name__ == '__main__':
    main()
