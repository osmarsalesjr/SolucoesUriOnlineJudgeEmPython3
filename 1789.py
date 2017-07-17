
def main():
    while True:
        try:
            n = int(input())
        except:
            break

        velocidades = [int(i) for i in input().split()]
        maior = max(velocidades)

        if maior >= 0 and maior < 10:
            print(1)
        elif maior >= 10 and maior < 20:
            print(2)
        else:
            print(3)



if __name__ == '__main__':
    main()