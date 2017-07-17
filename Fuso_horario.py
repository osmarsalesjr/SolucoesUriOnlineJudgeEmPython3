def main():
    hora_partida, duracao, fuso_horario = [int(i) for i in input().split()]
    horas = range(0, 24)
    
    tempo_excedente = duracao + fuso_horario
    
    if (tempo_excedente + hora_partida) > 24:
        indice = (hora_partida - 24) + tempo_excedente
        
    elif (tempo_excedente + hora_partida) == 24:
        indice = 0
        
    else:
        indice = tempo_excedente + hora_partida
    
    
    hora_chegada = horas[indice]
    
    print(hora_chegada)


if __name__ == "__main__":
    main()
