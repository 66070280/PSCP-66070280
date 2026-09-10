"""P8"""
def main():
    """P8"""
    base = int(input())
    bonus = int(input())
    days = int(input())

    score = base + bonus

    if days > 3:
        score = score * 1.5

    if score >= 1500:
        rank = 5
    elif score >= 1000:
        rank = 4
    elif score >= 500:
        rank = 3
    elif score >= 200:
        rank = 2
    else:
        rank = 1

    status = 0

    if rank == 5 and days >= 7:
        status = 99
    elif rank == 4 and bonus > 300:
        status = 88

    print(int(score))
    print(rank)
    print(status)
main()
