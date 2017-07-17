# -*- coding: utf-8 -*-

def main():
    sequency = []
    numero = int(input())
    y = 0

    for i in range(10):
        if numero == y:
            y = 0
        sequency.append(y)
        y += 1



    for i in range(10):
        print("N[%d] = %d" % (i, sequency[i]))


if __name__ == "__main__":
    main()