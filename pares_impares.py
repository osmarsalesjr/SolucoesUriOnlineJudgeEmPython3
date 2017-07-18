

def main():
    n = int(input())
    par, impar = [], []
    
    for i in range(n):
        n = int(input())
        
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
        
    par.sort()
    impar.sort(reverse = True)
    
    listar(par)
    listar(impar)


def listar(lista):
     for i in lista:
         print(i)



if __name__ == "__main__":
    main()