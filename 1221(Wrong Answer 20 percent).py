
def main():

    qtdTestes = int(input())
    resultados = []

    for i in range(qtdTestes):

        numero = int(input())

        if (isPrime(3, numero, int(numero/2))):
            resultados.append("Prime")
        else:
            resultados.append("Not Prime")

    imprime(resultados)

def imprime(resultados):

    for i in resultados:
        print("%s" % i)

def isPrime(i, numero, temp):

    if temp <= 2:
        return True

    elif numero % i == 0:
        return False
    else:
        return isPrime(i + 1, numero, int(temp/2))


if __name__ == '__main__':
    main()