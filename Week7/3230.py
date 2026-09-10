"""P8"""
def main():
    """P8"""
    N = input()
    a = int(N[0])
    b = int(N[1])
    c = int(N[2])
    d = int(N[3])
    e = int(N[4])

    digits = [a, b, c, d, e]
    floors = [9, 10, 11, 12, 14]
    floor = 13

    for i in range(5):
        if digits[i] > 5:
            floor = floors[i]
            break

    palindrome = N == N[::-1]
    if palindrome:
        room_code = 1 if a + e > 5 else 2 if b * d > 5 else 0
    else:
        room_code = 1 if e and a // e > 5 else 2 if b - e > 5 else 0

    total = a + b + c + d + e
    product = a * b * c * d * e
    last_code = 1 if total > 25 else 2 if product > 55 else 0
    print(str(floor) + str(room_code) + str(last_code))
main()
