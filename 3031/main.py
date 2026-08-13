"""P8"""
def main():
    """P8"""
    s, n = map(int, input().split())

    for _ in range(n):
        x, y = map(int, input().split())
        area = 3.1416 * (x * x + y * y)
        time = int(area / s)
        if area / s > time:
            time += 1
        print(time)
main()
