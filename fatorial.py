
def main():
    n = int(input())
    contador = 0
    anterior = 0
    
    
    while True:
        resto = n - anterior
        n = resto
        
        if resto <= 0:
            break
        
        for i in range(n):
            fat = fatorial(i + 1)
            if fat == n:
                contador += 1
                anterior = fat
                break
            if fat > n:
                anterior = fatorial(i)
                contador += 1
                break
    
    print(contador)
        





def fatorial(numero):
    if numero <= 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)


if __name__ == "__main__":
    main()