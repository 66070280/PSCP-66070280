"""P8"""
def main():
    """P8"""
    text = input()[:3]
    count = 0
    for char in text:
        if char in "aeiou":
            count += 1
    print(count)
main()
