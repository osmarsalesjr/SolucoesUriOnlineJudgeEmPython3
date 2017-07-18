


def main():
    while True:
        ns = [int(i) for i in input().split()]
        
        if ns[0] <= 0 or ns[1] <= 0:
            break
        
        soma = str(ns[0] + ns[1])
        
        if "0" in soma:
            soma = soma.split("0")
        
        soma = "".join(soma)
        
        print(soma)
        
    
if __name__ == "__main__":
    main()