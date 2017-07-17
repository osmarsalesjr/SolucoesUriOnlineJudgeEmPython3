# -*- coding: utf-8 -*-


def main():
    valor = float(input())
    notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
    moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

    print("NOTAS:")
    for nota in notas:
        qtd = int(valor / nota)
        valor = valor % nota
        print("%d nota(s) de R$ %.2f" % (qtd, nota))

    valor = valor * 100.00
    print("MOEDAS:")
    for moeda in moedas:
        qtd = int(valor / (moeda * 100))
        valor = valor % (moeda * 100)
        print("%d moeda(s) de R$ %.2f" % (qtd, moeda))


if __name__ == '__main__':
    main()