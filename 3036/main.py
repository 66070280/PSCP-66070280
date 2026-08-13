"""P8"""
def main():
    """P8"""
    n = int(input())
    r = int(n ** 0.5)

    if r * r < n:
        r += 1
    x = n - (r - 1) ** 2
    if n == 1:
        print(0)
    elif x % 2 == 1:
        print(2 * r - 2)
    else:
        print(2 * r - 3)
main()
