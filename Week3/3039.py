"""P8"""
def main():
    """P8"""
    n = int(input())
    minimum = int(input())

    for _ in range(n - 1):
        num = int(input())
        if num < minimum:
            minimum = num
    print(minimum)
main()
