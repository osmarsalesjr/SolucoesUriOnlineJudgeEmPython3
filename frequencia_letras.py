def main():
    n = int(input())
    
    for i in range(n):
        texto = input()
        letras = seleciona_letras(texto.lower())
        resultados = ""
        qtds = [texto.lower().count(i) for i in letras]
        maior, index = 0, 0
        
        for i in range(len(letras)):
            if qtds[i] > maior:
                maior = qtds[i]
                index = i
                resultados = letras[i]
        
        
        for i in range(len(qtds)):
            if qtds[i] == maior and i != index:
                resultados += letras[i]
        
        resultados = "".join(sorted(resultados))
        print("%s" % resultados)



def seleciona_letras(text):
    alphabet = [chr(i) for i in range(97, 123)]
    alfabeto = "".join(alphabet)
    letters = ""
    for letra in text:
        if letra not in letters and letra in alfabeto:
            letters += letra
    return letters   


if __name__ == "__main__":
    main()