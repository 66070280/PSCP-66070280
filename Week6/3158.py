"""P8"""
def main():
    """P8"""
    n = int(input())
    a = 0
    for _ in range(n):
        a += n ** 2
        n -= 1
    print(a)
main()
