##Thanks to Leo for suport

def main():
    resultsLists = list()
    while True:

        nWords = int(input())

        if (nWords <= 0):

            break
        else:

            words = list()
            for i in range(nWords):
                word = input()
                words.append(word)

            lastWord = sorted(words, key=len).pop()
            size_max = len(lastWord)

            temp = list()
            size = len(words)
            for i in range(size):

                spaces = (size_max - len(words[i])) * " "
                if (i == size - 1):
                    newString = "%s%s\n" % (spaces, words[i])
                else:
                    newString = "%s%s" % (spaces, words[i])
                temp.append(newString)
            resultsLists.append(temp)

    lastPosition = temp[-1]
    lenght = len(temp) - 1
    newStringTemp = ""

    for i in range(len(lastPosition) - 1):
        newStringTemp += lastPosition[i]
    temp[lenght] = newStringTemp

    listar(resultsLists)


def listar(listas):
    for i in range(len(listas)):
        for j in range(len(listas[i])):
            print(listas[i][j])


if __name__ == "__main__":
    main()