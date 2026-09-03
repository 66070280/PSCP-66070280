"""P8"""
def main():
    """P8"""
    n = int(input())
    isum = 0
    iodd = 0
    ieven = 0
    for _ in range(n):
        num = int(input())
        if not num % 2:
            ieven += 1
        else:
            iodd += 1
        isum += num
    print(f"SUM {isum}")
    print(f"EVEN {ieven}")
    print(f"ODD {iodd}")
main()
