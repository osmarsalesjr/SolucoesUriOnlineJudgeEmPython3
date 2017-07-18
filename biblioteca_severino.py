

def main():
    n = int(input())
    ws = []
    
    words = [i.upper() for i in input().split()]
    
    for w in words:
        size = len(w)
        if size == 3 and ("OB" in w or "UR" in w):
            ws.append(w[0 : 2] + "I")
        else:
            ws.append(w)
    
    for w in ws:
        print(w,)
    
    
if __name__ == "__main__":
    main()