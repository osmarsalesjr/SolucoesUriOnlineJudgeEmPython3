import math

def main():

    qtdTestes = int(input())
    resultados = []

    for i in range(qtdTestes):

        numero = int(input())

        if (isPrime(numero)):
            resultados.append("Prime")
        else:
            resultados.append("Not Prime")

    imprimeLista(resultados)

def imprimeLista(resultados):

    for i in resultados:
        print("%s" % i)


def isPrime(numero):

    if numero == 0 or numero == 1:
        return False

    if numero == 2:
        return True

    i = 2
    temp = math.sqrt(numero) + 1

    while(True):

        if (i > temp):

            return True
        if (numero % i == 0):

            return False

        i += 1


if __name__ == '__main__':
    main()