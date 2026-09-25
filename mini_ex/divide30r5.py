"""P8"""
def main():
    """P8"""
    n = int(input())
    plus = 0
    for i in range(1, n + 1):
        if not i % 3:
            plus += i
        elif not i % 5:
            plus += i
    print(plus)
main()
