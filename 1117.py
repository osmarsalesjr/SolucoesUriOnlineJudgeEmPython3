
def main():
    tempo_viagem = int(input())
    velocidade_media = int(input())

    distancia = tempo_viagem * velocidade_media

    litros = float(distancia) / 12.0

    print("%.3f" % litros)




if __name__ == '__main__':
    main()