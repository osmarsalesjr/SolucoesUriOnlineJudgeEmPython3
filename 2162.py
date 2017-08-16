##Thanks to Leo for suport

def main():


    numeroDeMedidas = int(input())
    medidas = [int(i) for i in input().split()]

    resultado = -1
    if (numeroDeMedidas < 2):

        print(1)
    else:

        temp = medidas[1]
        if (medidas[0] > medidas[1]):

            for i in range(2, len(medidas)):
                if(i % 2 == 0):
                    if (temp < medidas[i]):
                        temp = medidas[i]
                    else:
                        resultado = 0
                else:
                    if (temp > medidas[i]):
                        temp = medidas[i]
                    else:
                        resultado = 0
        elif(medidas[0] == medidas[1]):

            resultado = 0
        else:

            for i in range(2, len(medidas)):
                if (i % 2 != 0):
                    if (temp < medidas[i]):
                        temp = medidas[i]
                    else:
                        resultado = 0
                else:
                    if (temp > medidas[i]):
                        temp = medidas[i]
                    else:
                        resultado = 0

    if(resultado == -1):
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()