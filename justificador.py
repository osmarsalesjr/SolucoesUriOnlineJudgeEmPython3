
def main():

    results = list()
    while True:

        nWords = int(input())
        
        if (nWords <= 0):

            results.pop()
            break
        else:

            words = list()

            for i in range(nWords):

                word = input()
                words.append(word.upper())
            
            size_max = len(sorted(words, key = len).pop())

            for word in words:

                sizeWord = size_max - len(word)
                spaces = ""

                for i in range(sizeWord):
                    spaces += " "

                results.append(spaces + word)

            results.append("")


    listar(results)


def listar(lista):

    for i in lista:

        print(i)


if __name__ == "__main__":
    main()