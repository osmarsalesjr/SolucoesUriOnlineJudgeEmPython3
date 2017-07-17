# -*- coding: utf-8 -*-

def main():
    vetor = []
    vetor.append(int(input()))

    for i in range(1, 10):
        vetor.append(vetor[i - 1] * 2)

    for i in range(10):
        print("N[%d] = %d" % (i, vetor[i]))


if __name__ == "__main__":
    main()