def main():
    n = int(input())
    
    for i in range(n):
        qtd_alunos = int(input())
        alunos = [int(i) for i in input().split()]
    
        for j in range(qtd_alunos):
            alunos[j] = alunos[j]
    
        alunos_desc = sorted(alunos, reverse=True)
        
        posicao = 0
        for k in range(qtd_alunos):
            if alunos[k] == alunos_desc[k]:
                posicao += 1
        
        print(posicao)

if __name__ == '__main__':
    main()