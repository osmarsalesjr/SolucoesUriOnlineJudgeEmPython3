

def main():
    while True:
        try:
            text = input()    
        except:
            break
        
        words = text.split()
        qtd = len(words)
        contador = 0
            
        for w in words:
            if w.isalpha():
                contador += len(w)            
            
        media = int(contador / qtd)
            
        if media >= 6:
            classificacao = 1000
        elif 4 <= media <= 5:
            classificacao = 500
        else:
            classificacao = 250
                    
        print(classificacao)




if __name__ == "__main__":
    main()