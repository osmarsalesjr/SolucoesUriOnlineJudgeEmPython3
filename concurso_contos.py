def main():
    while True:
        try:
            n = [int(i) for i in input().split()]
            texto = input()
            linhas, limite = 0, n[2]
            tamanho = len(texto)
        
            for i in range(tamanho):
                if i >= limite:
                    linhas += 1
                    limite += n[2]
        
            paginas = int(linhas / n[1])
        
            if tamanho % n[2] > 0:
                paginas += 1
        
            print("%d" % paginas)
        except:
            break


if __name__ == "__main__":
    main()