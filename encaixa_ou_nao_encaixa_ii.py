
def main():
    n = int(input())
    
    for i in range(n):
        a = input()
        b = input()
        
        sz = len(a) - len(b)
        
        c = a[sz: len(a):]
        
        if b.lower() == c.lower():
            print("encaixa")
        else:
            print("nao encaixa")
        
        



if __name__ == "__main__":
    main()