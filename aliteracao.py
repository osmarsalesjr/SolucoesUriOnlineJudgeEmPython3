
def main():
    
    n = int(input())
    alfabeto = [chr(i) for i in range(97, 123)]
    
    for i in range(n):
        text = input()
        contador = 0
        
        for letra in alfabeto:
            if letra not in text:
                contador += 1
        
        if contador == 0:
            print("frase completa")
        elif contador <= 13:
            print("frase quase completa")
        else:
            print("frase mal elaborada")
            

if __name__ == "__main__":
    main()