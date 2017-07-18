


def main():
    n = int(input())
    
    for i in range(n):
        txt = input()
        contador = 0
        caracteres = []
        
        for j in txt:
            if j == ">" or j == "<":
                caracteres.append(j)
        
        for i in range(len(caracteres)):
            if caracteres[i] == "<":
                for j in range(i + 1, len(caracteres)):
                    if caracteres[j] == ">":
                        contador += 1
                        caracteres[j] = "."
                        break
        
        print("%d" % contador)
            
        



if __name__ == "__main__":
    main()