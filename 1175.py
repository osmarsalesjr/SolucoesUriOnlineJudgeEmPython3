# -*- coding: utf-8 -*-

def main():
    vetor = []

    for i in range(20):
        vetor.append(int(input()))

    for i in range(10):
        valor = vetor[i]
        vetor[i] = vetor[19 - i]
        vetor[19 - i] = valor

    for i in range(20):
        print("N[%d] = %d" % (i, vetor[i]))


if __name__ == "__main__":
    main()