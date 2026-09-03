"""P8"""
def main():
    """P8"""
    com = input()
    x, y = 0, 0

    for cmd in com:
        if cmd == 'N':
            y += 1
        elif cmd == 'S':
            y -= 1
        elif cmd == 'E':
            x += 1
        elif cmd == 'W':
            x -= 1
    distance = abs(x) + abs(y)
    print(f"{x} {y} {distance}")
main()
