
def main():
    n = int(input())

    horas = int(n / 3600)
    n = int(n % 3600)

    minutos = int(n / 60)
    n = int(n % 60)

    print("%d:%d:%d" % (horas, minutos, n))


if __name__ == '__main__':
    main()