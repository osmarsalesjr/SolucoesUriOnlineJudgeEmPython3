
def main():
    
    dias, taxa = [int(i) for i in input().split()]
    cotacoes = [int(i) for i in input().split()]
    valor = 0
    
    for c in range(len(cotacoes)):
        m = c + 1
        valor += cotacoes[c] * ((taxa/100) * (m/dias)) + 1
    
        print(valor)



if __name__ == "__main__":
    main()