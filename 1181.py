
def main():

    matriz = []
    soma = 0
    linha = int(input())
    operacao = input()

    for i in range(12):
        matriz.append([])
        for j in range(12):
            matriz[i].append(float(input()))

    for i in range(linha, linha + 1):
        for j in range(12):
            soma += matriz[i][j]

    if operacao == "S":
        print("%.1f" % soma)
    else:
        print("%.1f" % (soma / 12))



if __name__ == '__main__':
    main()