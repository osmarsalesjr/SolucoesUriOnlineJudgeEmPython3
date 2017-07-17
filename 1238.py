def main():
    quantidade = int(input())

    for j in range(quantidade):
        textos = [i for i in input().split()]

        if len(textos[0]) <= len(textos[1]):
            qtd_combinacoes = len(textos[0])
            texto_maior = textos[1]
        else:
            qtd_combinacoes = len(textos[1])
            texto_maior = textos[0]

        texto_resultante = ""
        for i in range(qtd_combinacoes):
            texto_resultante += textos[0][i] + textos[1][i]

        texto_resultante += texto_maior[qtd_combinacoes: len(texto_maior)]

        print(texto_resultante)


if __name__ == "__main__":
    main()