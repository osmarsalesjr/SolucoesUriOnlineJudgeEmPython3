

def main():
    n = int(input())
    
    for i in range(n):
        txt = input()
        wds = [i for i in txt.split()]
        sc = "oulupukk"
        new = []
        
        for w in wds:
            if sc in w and "." in w:
                new.append("Joulupukki.")
            
            elif sc in w:
                new.append("Joulupukki")
            
            else:
                new.append(w)
        
        new_txt = " ".join(new)
        
        print(new_txt)
        
    
if __name__ == "__main__":
    main()