def main():
    n = int(input())
    
    for i in range(n):
        pa, pb, ga, gb = [float(i) for i in input().split()]
        contador = 0
        
        while True:
            if contador >= 101 or pa > pb:
                break
            
            pa += int(pa * (ga / 100))
            pb += int(pb * (gb / 100))
            contador += 1
            
        print(pa, pb)
        if contador < 100:
            print("%d anos." % contador)
        elif contador == 100:
            print("%d anos." % contador)
        else:
            print("Mais de um seculo.")




if __name__ == "__main__":
    main()