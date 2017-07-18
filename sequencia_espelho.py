

def main():
    n = int(input())
    
    for i in range(n):
        xtms = [int(z) for z in input().split()]
        txt = ""
        
        for j in range(xtms[0], xtms[1] + 1):
            txt += str(j)
        
        for j in reversed(txt):
            txt += j
        
        print(txt)
        
    
if __name__ == "__main__":
    main()