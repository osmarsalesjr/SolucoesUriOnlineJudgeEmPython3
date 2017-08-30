import math

def main():

    listaDeDicionarios = list()
    while(True):

        tempo = int(input())

        if(tempo <= 0):
            break
        media = tempo/90.0
        alemanha = math.ceil(media * 7.0)
        brasil = int(media * 1.0)
        listaDeDicionarios.append({"a": alemanha, "b": brasil})

    for dicionario in listaDeDicionarios:
        print("Brasil %d x Alemanha %d" % (dicionario["b"], dicionario["a"]))


if __name__ == '__main__':
    main()