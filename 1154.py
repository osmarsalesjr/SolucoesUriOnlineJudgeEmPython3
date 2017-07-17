
def main():
    soma, qtd = 0, 0
    while True:
        n = int(input())
        if n < 0:
            break
        soma += n
        qtd += 1

    media = float(soma / qtd)
    print("%.2f" % media)



if __name__ == '__main__':
    main()
