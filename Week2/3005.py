"""P8"""

text_input = input()
text_split = text_input.split(" ")

num_1 = int(text_split[0])
num_2 = int(text_split[1])
num_3 = int(text_split[2])

carrot = num_1 * 10
cabbage = num_2 * 25
tomato = num_3 * 3

print(carrot + cabbage + tomato)
