

def main():
    cds = [int(i) for i in input().split()]
    diferenca = max(cds) - min(cds)

    while True:

        if cds[0] % diferenca == 0 and cds[1] % diferenca == 0:
            break
        diferenca -= 1

    print(diferenca)



if __name__ == '__main__':
    main()