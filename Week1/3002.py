"""P8"""
def main():
    """P8"""
    first_name = input()
    last_name = input()
    age = input()

    if len(first_name) >= 5 and len(last_name) >= 5:
        password = first_name[0:2] + last_name[-1] + age[-1]
    else:
        password = first_name[0:1] + age + last_name[-1]
    print(password)
main()
