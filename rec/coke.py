"""P8"""
def main():
    """P8"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    if not d:
        print(0)
        return
    if not b:
        print(d * a)
        return

    discount = (d - 1) // b
    fullprice = d - discount
    total = (fullprice * a) + (discount * c)
    print(total)
main()
