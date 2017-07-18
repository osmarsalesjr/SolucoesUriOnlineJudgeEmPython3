
def main():
    while True:
        a = [i for i in input().split()]
        if a[0] == "0" == a[1]:
            break
        else:
            texto = ""
            for i in a[1]:
                if a[0] != i:
                    texto += i
            if texto == "":
                print(0)
            else:
                print(int(texto))



if __name__ == "__main__":
    main()