"""P8"""
def main():
    """P8"""
    n = int(input())
    sid1 = input()[:n]
    sid2 = input()[:n]
    count = 0
    for i in range(n):
        if int(sid1[i]) + int(sid2[i]) != 9:
            count += 1
    if not count:
        print("YES")
    else:
        print("NO", count)
main()
