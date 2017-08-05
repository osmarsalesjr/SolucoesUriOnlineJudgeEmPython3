def main():


    numeroDeMedidas = int(input())
    medidas = [int(i) for i in input().split()]

    lista = []

    if (medidas[0] > medidas[1]):

        lista.append(1)
        lista.append(0)
        resultado = verificaMedidas(lista, medidas)
    elif (medidas[0] > medidas[1]):

        lista.append(0)
        lista.append(1)
        resultado = verificaMedidas(lista, medidas)
    else:

        resultado = 0

    print("%d" % resultado)


def verificaMedidas(lista, medidas):

    for i in range(2, len(medidas)):

        if (medidas[i] > medidas[i - 1]):

            lista.append(1)
        else:

            lista.append(0)

    temp = lista[0]

    for i in range(1, len(lista)):

        if (lista[i] == 1 and temp != 0):

            return 0
        elif (lista[i] == 0 and temp != 1):

            return 0
        else:
            temp = lista[i]

    return 1


if __name__ == '__main__':
    main()