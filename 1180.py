
def main():
    n = int(input())
    x = [int(i) for i in input().split()]

    index = 0
    numero = x[0]

    for i in range(1, n):
        if x[i] < numero:
            numero = x[i]
            index = i


    print("Menor valor: %d\nPosicao: %d" % (numero, index))

if __name__ == '__main__':
    main()