
def main():
    while True:
        n = int(input())
        
        if n <= 0:
            break
        else:
            words = []
            
            for i in range(n):
                wrd = input()
                words.append(wrd.upper())
            
            size_max = 0
            for w in words:
                if len(w) > size_max:
                    size_max = len(w)
                
            rlts = []
            for i in range(len(words)):
                d = size_max - len(words[i])
                if d <= 0:
                    palavra = words[i]
                else:
                    spcs = " " * d
                    palavra = spcs + words[i]
                    
                rlts.append(palavra)
            
            listar(rlts)
            


def listar(lista):
    for i in lista:
        print(i)
    
    print("")



if __name__ == "__main__":
    main()