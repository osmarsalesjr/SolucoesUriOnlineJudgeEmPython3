
def main():
    a, b, c = [float(i) for i in input().split()]

    triangulo = (a * c) / 2
    circulo = (c ** 2) * 3.14159
    trapezio = ((a + b) * c) / 2
    quadrado = b ** 2
    retangulo = a * b

    print("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f" % (triangulo, circulo, trapezio, quadrado, retangulo))


if __name__ == '__main__':
    main()