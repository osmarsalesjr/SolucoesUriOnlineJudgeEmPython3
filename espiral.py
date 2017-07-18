
def main():
    
    medida, numero = [int(i) for i in input().split()]
    
    matriz = []
    valores = 1
    indices = ""
    
    for i in range(medida):
        lista = range(valores, valores + medida)
        matriz.append(lista)
        
        valores += medida
    
    for i in range(medida):
       if numero in matriz[i]:
            j = matriz[i].index(numero)
            print("%d %d" % (j, i))
            break
    



if __name__ == "__main__":
    main()