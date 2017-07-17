
def main():
    tomadas = [int(i) for i in input().split()]
    total_aparelhos = 1

    for tomada in tomadas:
        total_aparelhos += tomada - 1

    print(total_aparelhos)




if __name__ == '__main__':
    main()