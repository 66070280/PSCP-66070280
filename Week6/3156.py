"""P8"""
def main():
    """P8"""
    text = input()
    k = int(input())
    result = ""

    for char in text:
        num = ord(char) - ord("a")
        new_num = (num + k) % 26
        result += chr(new_num + ord("a"))
    print(result)
main()
