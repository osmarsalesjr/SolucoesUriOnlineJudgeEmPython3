

def main():
    afbt = [chr(i) for i in range(97, 123)]
    while True:
        try:
            txt = input()
            new_txt = ""
            
            for i in range(len(txt) - 1, -1, -1):
                if txt[i].isalpha() and txt[i].isupper():
                    a = afbt.index(txt[i].lower())
                    new_txt += afbt[a - 13].upper()
                elif txt[i].isalpha() and txt[i].islower():
                    a = afbt.index(txt[i].lower())
                    new_txt += afbt[a - 13].lower()
                else:
                    new_txt += txt[i]
           
            new = ""
            for i in reversed(new_txt):
                new += i
            
            print(new)
        
        
        except:
            break



if __name__ == "__main__":
    main()