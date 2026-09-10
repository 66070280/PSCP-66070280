"""P8"""
def main():
    """P8"""
    n = int(input())

    for i in range(n):
        for j in range(i + 1):
            if not j:
                print(0, end="")
            elif i == n - 1:
                print(0, end="")
            elif i == j:
                print(0, end="")
            else:
                print(1, end="")
        print()
main()
