"""P8"""
color1 = input()
color2 = input()
if color1 == "Red" and color2 == "Yellow":
    print("Orange")
elif color1 == "Yellow" and color2 == "Red":
    print("Orange")
elif color1 == "Red" and color2 == "Blue":
    print("Violet")
elif color1 == "Blue" and color2 == "Red":
    print("Violet")
elif color1 == "Yellow" and color2 == "Blue":
    print("Green")
elif color1 == "Blue" and color2 == "Yellow":
    print("Green")
else:
    print("Error")
