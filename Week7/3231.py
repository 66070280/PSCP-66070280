"""P8"""
def main():
    """P8"""
    g = int(input())
    r = int(input())

    if g not in (1, 2, 3, 4, 5, 6) or r not in (1, 2, 3, 4, 5, 6):
        print("Invalid")
    elif g == r:
        print("Correct!")
    else:
        print("Wrong!")
main()
