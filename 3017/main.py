"""P8"""
def main():
    """P8"""
    food_price = int(input())
    service_charge = food_price * 0.10

    if service_charge < 50:
        service_charge = 50.0
    elif service_charge > 1000:
        service_charge = 1000.0
    subtotal = food_price + service_charge
    total_price = subtotal * 1.07
    print(f"{total_price:.2f}")
main()
