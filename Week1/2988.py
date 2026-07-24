"""P8"""
def main():
    """P8"""
    id_card = input()

    if id_card.isnumeric() and len(id_card) == 13:
        print("yes")
    else:
        print("no")
main()
