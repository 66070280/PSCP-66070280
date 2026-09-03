"""P8"""
def main():
    """P8"""
    N, K, T = map(int, input().split())
    current = 1

    for step in range(1, N + 1):
        if current == T:
            print(step)
            break
        current = (current - 1 + K) % N + 1
        if current == 1:
            print(step)
            break
main()
