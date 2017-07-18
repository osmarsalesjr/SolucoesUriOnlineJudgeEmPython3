#-*-coding:utf8;-*-
#qpy:2
#qpy:console

def main():
    leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    num = int(input())
    
    for i in range(num):
        soma = 0
        numeros = raw_input()
        for j in numeros:
            soma = soma + leds[int(j)]
        print("%d leds" % soma)
    

if __name__ == "__main__":
    main()