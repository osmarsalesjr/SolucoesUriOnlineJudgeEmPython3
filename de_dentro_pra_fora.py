

def main():
    n = int(input())
    
    for i in range(n):
        text = input()
        sz = len(text)
        hsz = int(sz / 2)
        
        final_text = text[hsz - 1:: -1]
        final_text += text[sz - 1: hsz - 1: -1]
        
        print(final_text)




if __name__ == "__main__":
    main()