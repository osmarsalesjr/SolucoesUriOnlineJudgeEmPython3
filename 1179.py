# -*- coding: utf-8 -*-

def main():
    par = []
    impar = []

    for i in range(15):
        n = int(input())

        if n % 2 == 0:
            par.append(n)
            if len(par) >= 5:
                for i in range(5):
                    print("par[%d] = %d" % (i, par[i]))
                par.clear()
        else:
            impar.append(n)
            if len(impar) >= 5:
                for i in range(5):
                    print("impar[%d] = %d" % (i, impar[i]))
                impar.clear()

    for i in range(len(par)):
        print("par[%d] = %d" % (i, par[i]))

    for i in range(len(impar)):
        print("impar[%d] = %d" % (i, impar[i]))


if __name__ == "__main__":
    main()