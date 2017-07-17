
def main():
    code_one, qtd_one, valor_one = [float(i) for i in input().split()]
    code_two, qtd_two, valor_two = [float(i) for i in input().split()]

    valor_total = (valor_one * qtd_one) + (valor_two * qtd_two)

    print("VALOR A PAGAR: R$ %.2f" % valor_total)




if __name__ == '__main__':
    main()