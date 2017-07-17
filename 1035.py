
def main():
    a, b, c, d = [int(i) for i in input().split()]

    soma_ab = a + b
    soma_cd = c + d

    if b > c and d > a and soma_cd > soma_ab and c > 0 < d and a % 2 == 0:
        print("Valores aceitos")
    else:
        print("Valores nao aceitos")



if __name__ == '__main__':
    main()