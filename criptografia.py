

def main():
    n = int(input())
    
    for i in range(n):
        text = input()
        t1 = ""
        t2 = ""
        
        for i in text:
            if i.isalpha():
                t1 += chr(ord(i) + 3)
            else:
                t1 += i
       
        for i in reversed(t1):
            t2 += i
        
        size = len(t2)
        half_size = int(size / 2)
        
        t3 = t2[0 : half_size]
        
        for i in range(half_size, size):
            t3 += chr(ord(t2[i]) - 1)
        
        print(t3)
        
             




if __name__ == "__main__":
    main()