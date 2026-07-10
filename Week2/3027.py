"""P8"""

text_input = input()
text_split = text_input.split(" ")
price = int(input())

num_1 = int(text_split[0])
num_2 = int(text_split[1])
num_3 = int(text_split[2])

amount = (num_1 + num_2) * (num_3 * 2)

print(amount)
print(amount * price)
