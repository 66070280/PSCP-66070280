"""P8"""
def main():
    """P8"""
    weather = input()
    hml = input()
    if weather == "Gloomy" and hml == "High" or hml == "Medium":
        print("100%")
    elif weather == "Cloudy" and not hml:
        print("50%")
    elif weather == "Clear" and hml == "Low":
        print("0%")
    else:
        print("Not sure.")
main()
