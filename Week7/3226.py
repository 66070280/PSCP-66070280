"""P8"""
def main():
    """P8"""
    n = float(input())
    k = int(input())
    r = 0.0381

    fv = n * ((1 + r) ** k)
    print(f"{fv:.2f}")
main()
