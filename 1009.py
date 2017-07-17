# -*- coding: utf-8 -*-

def main():
    name = str(input())
    salario_fixo = float(input())
    total_vendas = float(input())

    salary = salario_fixo + (total_vendas * 0.15)

    print("TOTAL = R$ %.2f" % salary)


if __name__ == '__main__':
    main()