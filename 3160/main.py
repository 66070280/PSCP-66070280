"""P8"""
def main():
    """P8"""
    start, end = map(int, input().split())
    count = 0

    for n in range(start, end + 1):
        if n < 2:
            continue
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        if prime:
            print(n, end=" ")
            count += 1
    if count > 0:
        print()
    print(f"Total primes: {count}")
main()
