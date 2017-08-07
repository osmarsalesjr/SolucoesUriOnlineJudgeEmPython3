

def main():
    while True:
        n = int(input())

        if n <= 0:
            break

        contadores = []
        wds = []

        for i in range(n):
            wds.append(input())

        wds.sort(key = len)
        size = len(wds)

        for j in range(size):
            word = wds[j]
            contador = 1

            for i in range(j + 1, size):
                if word in wds[i]:
                    contador += 1
                    word = wds[i]

            contadores.append(contador)

            maior = max(contadores)
            if maior > (size - (j + 1)):
                break

        print(maior)




if __name__ == '__main__':
    main()