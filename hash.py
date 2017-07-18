

def main():
    afbt = [chr(i).upper() for i in range(97, 123)]
    
    n = int(input())
    
    for i in range(n):
        ls = int(input())
        soma = 0
        wds = []
        
        for j in range(ls):
            wds.append(input())
        
        for w in range(len(wds)):
            for l in range(len(wds[w])):
                soma += afbt.index(wds[w][l].upper()) + w + l
        
        print(soma)



if __name__ == "__main__":
    main()