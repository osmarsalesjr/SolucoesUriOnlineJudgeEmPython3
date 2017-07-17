
def main():
    n = int(input())
    contador = 0
    for i in range(n):
        for j in range(3):
            contador += 1
            if contador % 4 == 0:
                contador += 1
            print("%d" % contador, end=" ")
        print("PUM")



if __name__ == '__main__':
    main()