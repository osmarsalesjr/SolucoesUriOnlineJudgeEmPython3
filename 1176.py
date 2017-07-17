# -*- coding: utf-8 -*-

def main():
    T = int(input())

    fibonacci = []
    fibonacci.append(0)
    fibonacci.append(1)

    for i in range(1, 60):
        fibonacci.append((fibonacci[i]) + (fibonacci[i - 1]))

    for i in range(T):
        N = int(input())
        print("Fib[%d] = %d" % (N, fibonacci[N]))


if __name__ == "__main__":
    main()