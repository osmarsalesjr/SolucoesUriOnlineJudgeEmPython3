
def main():
    while True:
        try:
            text = input()
            indice = 0
            sentenca = ""
            
            for i in range(len(text)):
                 if text[i] != " ":
                     indice = i
                     la = text[i].upper()
                     break
                 else:
                     sentenca += text[i]
                      
            
            sentenca += la
            
            for i in range(indice + 1, len(text)):
                if text[i] == " ":
                    sentenca += " "
                else:
                    if la.isupper():
                        sentenca += text[i].lower()
                        la = text[i].lower()
                    else:
                        sentenca += text[i].upper()
                        la = text[i].upper()
            
            print(sentenca)
                    
                    
                    
            
        except:
            break





if __name__ == "__main__":
    main()