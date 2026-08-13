"""P8"""
def main():
    """P8"""
    text_input = input()
    text_split = text_input.split(" ")

    r = float(text_split[0])
    h = float(text_split[1])
    g = float(text_split[2])
    pi = 3.14

    width = h + (2 * r)
    length = (2 * pi * r) + g
    print(f"{width:.2f} {length:.2f}")
main()
