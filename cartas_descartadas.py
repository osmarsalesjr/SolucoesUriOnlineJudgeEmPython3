
def main():
    while True:
        try:
            n = int(input())
            discarded = []
        
            if n <= 0:
                break
        
            cards = [i for i in range(1, n + 1)]
        
            for i in range(n - 1):
                discarded.append(str(cards.pop(0)))
                cards.append(str(cards.pop(0)))
        
            dsds = ", ".join(discarded)
            crds = ", ".join(cards)              
        
            print("Discarded cards: %s" % dsds)
            print("Remaining cards: %s" % crds)
        except:
            break

if __name__ == "__main__":
    main()