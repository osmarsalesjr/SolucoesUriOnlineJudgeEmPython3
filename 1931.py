#-*-coding:utf8;-*-

def main():
    cidades_estradas = [int(i) for i in raw_input().split()]
    percursos_pedagios = []
    soma = 0
    
    for i in range(cidades_estradas[1]):
        for j in range(3):
            percursos_pedagios.append([int(i) for i in raw_input().split()])
    
    for i in range(len(percursos_pedagios)):
        if percursos_pedagios[i][0] >= 1

    print(percursos_pedagios)



                
if __name__ == "__main__":
    main()