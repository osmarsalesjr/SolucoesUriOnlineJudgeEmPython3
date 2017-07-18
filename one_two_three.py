


def main():
    n = int(input())
    
    for i in range(n):
        wd = input()
        
        if len(wd) == 3 and ("on" in wd or "ne" in wd or (wd[0] == "o" and wd[2] == "e")):
            print("one")
        elif len(wd) == 3:
            print("two")
        else:
            print("three")

if __name__ == "__main__":
    main()