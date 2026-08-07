"""P8"""
def main():
    """P8"""
    n = int(input())
    a = 1
    for _ in range(n):
        if n > 0:
            a = a * n
        n -= 1
    print(a)
main()
