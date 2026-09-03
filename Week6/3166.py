"""P8"""
def main():
    """P8"""
    n = int(input())
    avg = 0
    porf = True
    for _ in range(n):
        num = int(input())
        if num < 50:
            porf = False
        avg += num
    avg = avg / n
    print(f"{avg:.1f}")
    if porf is True and avg >= 60:
        print("PASS")
    else:
        print("FAIL")
main()
