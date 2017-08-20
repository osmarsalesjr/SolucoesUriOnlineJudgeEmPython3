from time import time

def main():

    dimensaoMatriz, ultimoFeijao = [int(i) for i in input().split()]

    contador = 0
    temp = 0
    limite = dimensaoMatriz
    limiteLateralEsquerda = -1
    encontrado = False

    inicio = time()
    while(True):

        if (encontrado):
            break
        print("\nContador:",contador)
        print("1º For")
        for i in range(temp, temp + 1):
            for j in range(temp, limite):
                contador += 1
                if (contador >= ultimoFeijao):
                    indexI = i
                    indexJ = j
                    encontrado = True
                    break
                ##contador += 1

            if(encontrado):
                break
        if (encontrado):
            break
        print("2º For")
        for i in range(temp + 1, limite):
            for j in range(limite - 1, limite - 2, - 1):
                contador += 1
                if (contador >= ultimoFeijao):
                    indexI = i
                    indexJ = j
                    encontrado = True
                    break
                ##contador += 1
            if (encontrado):
                break

        if (encontrado):
            break
        print("3º For")
        limite -= 1
        for i in range(limite, limite - 1, -1):
            for j in range(limite - 1, limiteLateralEsquerda, -1):
                contador += 1
                if (contador >= ultimoFeijao):
                    indexI = i
                    indexJ = j
                    encontrado = True
                    break
                ##contador += 1
            if (encontrado):
                break
        if (encontrado):
            break
        print("4º For")
        for i in range(limite - 1, temp, -1):
            for j in range(temp, temp + 1):
                contador += 1
                if (contador >= ultimoFeijao):
                    indexI = i
                    indexJ = j
                    encontrado = True
                    break
                ##contador += 1
            if (encontrado):
                break
        limiteLateralEsquerda += 1
        temp += 1
    fim = time()
    print("%d %d" % (indexI + 1, indexJ + 1))
    print("Tempo de Execucao:", (fim - inicio))



if __name__ == "__main__":
    main()