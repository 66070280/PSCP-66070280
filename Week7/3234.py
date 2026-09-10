"""P8"""
def main():
    """P8"""
    start, n = input().split()
    n = int(n)
    colors = ["Red", "Green", "Blue"]

    if start == "R":
        index = 0
    elif start == "G":
        index = 1
    else:
        index = 2

    for _ in range(n):
        print(colors[index], end=" ")
        index += 1
        if index == 3:
            index = 0
main()
