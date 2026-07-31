"""P8"""
def main():
    """P8"""
    x = int(input())
    y = int(input())
    a = int(input())
    z = int(input())

    group = z // x
    remain = z % x
    total = (group * y + remain) * a
    print(total)
main()
