"""P8"""
def main():
    """P8"""
    n = int(input())
    total_sum = 0
    equation = ""

    for i in range(n):
        a = int(input())
        b = int(input())
        max_val = a if a > b else b
        total_sum += max_val
        if n == 1:
            equation = str(max_val)
        else:
            if not i:
                equation = str(max_val)
            else:
                equation += " + " + str(max_val)
    if n == 1:
        print(equation)
    else:
        print(equation + " = " + str(total_sum))
main()
