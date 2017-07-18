
def main():

    qtdTestes = int(input())
    resultados = []

    for i in range(qtdTestes):

        numero = int(input())

        if (isPrime(numero)):
            resultados.append("Prime")
        else:
            resultados.append("Not Prime")

    imprime(resultados)

def imprime(resultados):

    for i in resultados:
        print("%s" % i)


def isPrime(numero):

    counter = 3
    i = 2
    while(True):

        if (counter/float(numero) >= 0.30):

            return True
        if (numero % i == 0):

            return False

        i += 1
        counter += 1



if __name__ == '__main__':
    main()