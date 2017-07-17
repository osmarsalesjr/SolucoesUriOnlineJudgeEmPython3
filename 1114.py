def main():
    contador = 0
    while True:
        if contador >= 3:
            print("Acesso Negado")
            break

        senha = int(input())
        if senha != 2002:
            print("Senha Invalida")
        else:
            print("Acesso Permitido")
            break
        contador += 1


if __name__ == '__main__':
    main()