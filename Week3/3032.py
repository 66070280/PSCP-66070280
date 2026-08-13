"""P8"""
def main():
    """P8"""
    n = int(input())
    max_score = 0
    count = 0

    for _ in range(n):
        score = int(input())
        if score > max_score:
            max_score = score
            count = 1
        elif score == max_score:
            count = count + 1
    print(max_score)
    print(count)
main()
