"""P8"""

tem = float(input())
temchar1 = (input())
temchar2 = (input())

if temchar1 == "C" and temchar2 == "K":
    print(tem + 273.15)
elif temchar1 =="C" and temchar2 == "F":
    print(((tem * 9) / 5 ) + 32)
elif temchar1 =="C" and temchar2 == "R":
    print(((tem + 273.15) * 9 ) / 5)
elif temchar1 =="K" and temchar2 == "C":
    print(tem - 273.15)
elif temchar1 =="K" and temchar2 == "F":
    print((((tem - 273.15) * 9) / 5) + 32)
elif temchar1 =="K" and temchar2 == "R":
    print((((tem - 273.15) + 273.15) * 9) / 5)
elif temchar1 =="F" and temchar2 == "C":
    print(tem - 273.15)