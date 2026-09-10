"""P8"""
def main():
    """P8"""
    x, y = map(int, input().split())
    total = 0
    jump = x
    count = 0

    for _ in range(x // 2 + 1):
        if total >= y:
            break

        total += jump
        count += 1
        jump -= 2

    if total >= y:
        print(count)
    else:
        print(-1)
main()
