
def main():
    testes = int(input())
    for j in range(testes):
        texto = input()
        qtd = int(input())
        palavra = ""
        contador = 0

        for i in range(qtd):
            for n in range(contador, len(texto)):
                for z in range(97, 123):
                    if texto[n].upper() == chr(z).upper():
                        palavra += chr(z - 2)
                        contador += 1
                        break

        if qtd == 0:
            print(texto)
        else:
            print(palavra)


if __name__ == "__main__":
    main()