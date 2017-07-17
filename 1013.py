
def main():
    a, b, c = [int(i) for i in input().split()]

    maiorAB = (a + b + abs(a - b)) / 2
    maior = (maiorAB + c + abs(maiorAB - c)) / 2

    print("%d eh o maior" % maior)


if __name__ == '__main__':
    main()