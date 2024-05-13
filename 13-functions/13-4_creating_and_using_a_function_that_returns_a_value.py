def calculateTax(price, tax_rate):
    total = price + (price * tax_rate)
    return total  # Sends result back to the main program

my_price = float(input("Enter a price: "))

totalPrice = calculateTax(my_price, 0.06)  # Calls function and stores the result in `totalPrice`
print("price = ", my_price, " Total price = ", totalPrice)