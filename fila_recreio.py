


def main():
    n = int(input())
    
    for i in range(n):
        contador = 0
        qtd = int(input())
        nt = [int(i) for i in input().split()]
        
        notas = [nt[i] for i in range(qtd)]
        
        l = sorted(notas, reverse = True)
        
        for i in range(len(l)):
            if l[i] == notas[i]:
                contador += 1
        
        print(contador)
           



if __name__ == "__main__":
    main()