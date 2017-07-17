# -*- coding: utf-8 -*-

def main():
    n = []
    numero = float(input())

    for i in range(10):
        if i == 0:
            n.append(numero)
        else:
            n.append(n[i - 1] / 2)

    for i in range(10):
        print("N[%d] = %.4f" % (i, n[i]))


if __name__ == "__main__":
    main()