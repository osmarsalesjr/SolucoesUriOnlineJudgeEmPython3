def main():
    qtd_testes = int(input())
    for i in range(qtd_testes):
        words = [i for i in input().split()]
        qtd_words = len(words)
        for i in range(qtd_words - 1, 0,-1):
            for j in range(i):
                if len(words[j]) < len(words[j+1]):
                    words[j+1], words[j] = words[j], words[j+1]
        
        text = " ".join(words)
        print(text)

if __name__ == '__main__':
    main()