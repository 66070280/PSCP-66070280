"""P8"""
def main():
    """P8"""
    N = int(input())

    for i in range(1, N + 1):
        if not i % 5:
            print("X", end="")
        else:
            print("*", end="")
main()
