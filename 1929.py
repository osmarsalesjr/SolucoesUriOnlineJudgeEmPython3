
def main():
    lados = [int(i) for i in input().split()]
    valido = False

    for i in range(len(lados) - 1, -1, -1):
        if valida_triangulo(lados[i], lados[i - 1], lados[i - 2]):
            valido = True
            break

    if valido == True:
        print("S")
    else:
        print("N")


def valida_triangulo(a, b, c):
    if (abs(b - c) < a < (b + c)) or (abs(a - c) < b < (a + c)) or (abs(a - b) < c < (a + b)):
        return True
    else:
        return False



if __name__ == '__main__':
    main()