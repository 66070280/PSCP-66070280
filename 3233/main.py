"""P8"""
def main():
    """P8"""
    win = input().split()
    buy = input().split()
    win_letter = win[0]
    win_num = win[1]
    buy_letter = buy[0]
    buy_num = buy[1]

    if win_letter == buy_letter and win_num == buy_num:
        print(1000000)
    elif win_num == buy_num:
        print(100000)
    elif win_letter == buy_letter and win_num[-3:] == buy_num[-3:]:
        print(2000)
    elif win_letter == buy_letter and win_num[-2:] == buy_num[-2:]:
        print(1000)
    elif win_letter != buy_letter and win_num[-3:] == buy_num[-3:]:
        print(200)
    elif win_letter != buy_letter and win_num[-2:] == buy_num[-2:]:
        print(100)
    elif win_letter == buy_letter:
        print(20)
    else:
        print(0)
main()
