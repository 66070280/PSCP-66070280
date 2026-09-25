"""P8"""
import math
def main():
    """P8"""
    r = float(input())
    a = float(input())
    b = float(input())

    l1 = 2 * math.pi * r
    l2 = a * 2 + b * 2
    lob = abs(l1 - l2)
    if l1 > l2:
        print("Circle is longer")
    elif l2 > l1:
        print("Rectangle is longer")
    else:
        print("Equal")
    print(f"{lob:.5f}")
main()
