price = int(input("Enter original price: "))
discount_percent = int(input("Enter discount percentage: "))

discount = discount_percent / 100
calculate_discount = price - (price * discount)

if discount_percent >= 20:
    print(calculate_discount)
else:
    print(price)