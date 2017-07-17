
def main():
    qtd_divisores = [0, 0, 0, 0]
    qtd_numeros = int(input())
    lista = [int(i) for i in input().split()]

    for numero in lista:
        if numero % 2 == 0:
            qtd_divisores[0] += 1

        if numero % 3 == 0:
            qtd_divisores[1] += 1

        if numero % 4 == 0:
            qtd_divisores[2] += 1

        if numero % 5 == 0:
            qtd_divisores[3] += 1

    print("%d Multiplo(s) de 2" % qtd_divisores[0])
    print("%d Multiplo(s) de 3" % qtd_divisores[1])
    print("%d Multiplo(s) de 4" % qtd_divisores[2])
    print("%d Multiplo(s) de 5" % qtd_divisores[3])






if __name__ == '__main__':
	main()