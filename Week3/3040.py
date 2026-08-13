"""8"""
def main():
    """P8"""
    n = int(input())
    ten = n // 10
    n = n % 10
    five = n // 5
    n = n % 5
    two = n // 2
    n = n % 2
    one = n // 1
    n = n % 1
    print("10 =",ten)
    print("5 =",five)
    print("2 =",two)
    print("1 =",one)
main()
