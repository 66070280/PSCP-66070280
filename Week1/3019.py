"""P8"""
def main():
    """P8"""
    pass_char = input()
    pass_int = int(input())

    if pass_char == "H" and pass_int == 4567:
        print("safe unlocked")
    elif pass_char == "H":
        print("safe locked - change digit")
    elif pass_int == 4567:
        print("safe locked - change char")
    else:
        print("safe locked")
main()
