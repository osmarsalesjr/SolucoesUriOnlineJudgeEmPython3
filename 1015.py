# -*- coding: utf-8 -*-

import math

def main():
    x1, y1 = [float(i) for i in input().split()]
    x2, y2 = [float(i) for i in input().split()]
    
    distancia = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    
    print("%.4f" % distancia)

if __name__ == "__main__":
    main()