
def main():

    numeros = [int(i) for i in input().split()]
    numerosSorted = sorted(numeros)

    for i in range(len(numerosSorted) - 1):
        print("%d"%numerosSorted[i])

    print("%d\n" % numerosSorted[len(numerosSorted) - 1])

    for i in range(len(numeros) - 1):
        print("%d"%numeros[i])

    print("%d" % numeros[len(numeros) - 1])



if __name__ == '__main__':
    main()