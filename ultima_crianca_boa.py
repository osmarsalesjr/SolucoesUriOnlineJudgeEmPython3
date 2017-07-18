

def main():

    names = []
    
    while True:
        try:
            names.append(input())
        except:
            break
    
    ns = [i.upper() for i in names]
    ns.sort()
    t = len(ns)
    
    for i in names:
        if i.upper() == ns[t - 1]:
            print(i)
            break
    
    
if __name__ == "__main__":
    main()