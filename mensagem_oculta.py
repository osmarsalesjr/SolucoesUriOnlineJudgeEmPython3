
def main():
    n = int(input())
    
    for i in range(n):
        a = input()
        a = a.replace(".", " ")
        
        wds = a.split()
        text = ""
        
        for i in wds:
            text += i[0]
        
        print(text)
        
        



if __name__ == "__main__":
    main()