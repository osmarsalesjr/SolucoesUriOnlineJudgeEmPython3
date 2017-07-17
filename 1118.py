
def main():
    valor = int(input())

    cem = int(valor / 100)
    valor = valor - (cem * 100)

    cinquenta = int(valor / 50)
    valor = valor - (cinquenta * 50)

    vinte = int(valor / 20)
    valor = valor - (vinte * 20)

    dez = int(valor / 10)
    valor = valor - (dez * 10)

    cinco = int(valor / 5)
    valor = valor - (cinco * 5)

    dois = int(valor / 2)
    valor = valor - (dois * 2)

    um = int(valor % 2)

    print(valor)
    print("%d nota(s) de R$ 100,00 " % cem)
    print("%d nota(s) de R$ 50,00 " % cinquenta)
    print("%d nota(s) de R$ 20,00 " % vinte)
    print("%d nota(s) de R$ 10,00 " % dez)
    print("%d nota(s) de R$ 5,00 " % cinco)
    print("%d nota(s) de R$ 2,00 " % dois)
    print("%d nota(s) de R$ 1,00 " % um)



if __name__ == '__main__':
    main()