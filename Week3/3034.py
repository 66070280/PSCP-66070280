"""P8"""
def main():
    """P8"""
    n , k = map(int, input().split())
    count = [0] * (k + 1)

    for _ in range(n):
        row = int(input())
        count[row] += 1
    time = min(count[1:])
    answer = n - time * k
    print(answer)
main()
