
def main():

    partidasInter = 0
    partidasGremio = 0
    qtdEmpates = 0
    qtdGrenais = 0

    while(True):

        gols = [int(i) for i in input().split()]
        novoGrenal = int(input())

        if (gols[0] > gols[1]):

            partidasInter += 1
        elif (gols[0] < gols[1]):

            partidasGremio += 1
        else:
            qtdEmpates += 1

        qtdGrenais += 1

        if (novoGrenal != 1):
            break

    for i in range(qtdGrenais):
        print("Novo grenal (1-sim 2-nao)")

    print("%d grenais" % qtdGrenais)
    print("Inter:%d" % partidasInter)
    print("Gremio:%d" % partidasGremio)
    print("Empates:%d" % qtdEmpates)

    if (partidasInter > partidasGremio):

        print("Inter venceu mais")
    elif (partidasInter < partidasGremio):

        print("Gremio venceu mais")
    else:

        print("Nao houve vencedor")


if __name__ == '__main__':
    main()