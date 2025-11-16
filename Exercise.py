# Billing App
item = input("What Item would you like to buy?: ")
price = int(input("Enter a price: "))
quantity = int(input("How many would you like to buy?: "))
total = price * quantity
print(f"You have bought {quantity} of {item}/s.")
print(f"The total price is:${total}")
