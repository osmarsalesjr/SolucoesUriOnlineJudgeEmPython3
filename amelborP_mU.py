
def main():
    n = int(input())
    contador = 10 ** (n - 1)
    qtd = 0
    wd = str(contador)[:: - 1]

    while True:
        if len(wd) > n:
            break

        wd = str(contador)[:: - 1]

        if contador < int(wd):
            qtd += 1

        contador += 1

        print(qtd, contador)




if __name__ == '__main__':
    main()