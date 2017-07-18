
def main():
    
    n = int(input())
    jgs = ["pedra", "papel", "tesoura", "lagarto", "spock"]
    pls = ["rajesh", "sheldon"]
    
    for i in range(n):
        ps = [i for i in input().split()]
        
        if ps[0] == jgs[0] and (ps[1] == jgs[2] or ps[1] == jgs[3]):
            print(pls[0])
        elif ps[1] == jgs[0] and (ps[0] == jgs[2] or ps[0] == jgs[3]):
            print(pls[1])
        
        elif ps[0] == jgs[1] and (ps[1] == jgs[0] or ps[1] == jgs[4]):
            print(pls[0])
        elif ps[1] == jgs[1] and (ps[0] == jgs[0] or ps[0] == jgs[4]):
            print(pls[1])
            
        elif ps[0] == jgs[2] and (ps[1] == jgs[1] or ps[1] == jgs[3]):
            print(pls[0])
        elif ps[1] == jgs[2] and (ps[0] == jgs[1] or ps[0] == jgs[3]):
            print(pls[1])
        
        elif ps[0] == jgs[3] and (ps[1] == jgs[1] or ps[1] == jgs[4]):
            print(pls[0])
        elif ps[1] == jgs[3] and (ps[0] == jgs[1] or ps[0] == jgs[4]):
            print(pls[1])
        
        elif ps[0] == jgs[4] and (ps[1] == jgs[0] or ps[1] == jgs[2]):
            print(pls[0])
        elif ps[1] == jgs[4] and (ps[0] == jgs[0] or ps[0] == jgs[2]):
            print(pls[1])
        
        else:
            print("empate")

        
    
if __name__ == "__main__":
    main()