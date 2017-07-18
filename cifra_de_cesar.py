

def main():
    teste = int(input())
    for i in range(teste):
        texto = input()
        qtd = int(input())
        
        alfabeto = [chr(i).upper() for i in range(97, 123)]
        word = ""
        
        for letra in texto:
            for j in range(len(alfabeto)):
                if letra.upper() == alfabeto[j]:
                     word += alfabeto[j - qtd]
                     break
            
        print(word)



if __name__ == "__main__":
    main()