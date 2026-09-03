"""P8"""
def main():
    """P8"""
    n = int(input())
    base = int(input())
    imax = base
    imin = base
    total = base
    avg = 0
    for _ in range(n - 1):
        num = int(input())
        if imax < num:
            imax = num
        if imin > num:
            imin = num
        total += num
    avg = total / n
    print(total)
    print(imax)
    print(imin)
    print(f"{avg:.1f}")
main()
