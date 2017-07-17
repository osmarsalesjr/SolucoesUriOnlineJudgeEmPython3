
def main():
    n = int(input())
    somas = [0, 0, 0, 0]

    for i in range(n):
        qtd_cobaias, tipo = [i for i in input().split()]
        if tipo.lower() == "c":
            somas[0] += float(qtd_cobaias)
        elif tipo.lower() == "r":
            somas[1] += float(qtd_cobaias)
        else:
            somas[2] += float(qtd_cobaias)
        somas[3] += float(qtd_cobaias)

    percentuais = [((somas[i] /somas[3]) * 100) for i in range(len(somas) - 1)]

    print("Total: %d cobaias" % somas[3])
    print("Total de coelhos: %d" % somas[0])
    print("Total de ratos: %d" % somas[1])
    print("Total de sapos: %d" % somas[2])

    print("Percentual de coelhos: %.2f %%" % percentuais[0])
    print("Percentual de ratos: %.2f %%" % percentuais[1])
    print("Percentual de sapos: %.2f %%" % percentuais[2])


if __name__ == '__main__':
    main()