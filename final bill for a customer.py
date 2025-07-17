total_price = float(input("Enter total price (in PKR): "))

if total_price > 500:
    discount = total_price * 0.10 
    final_price = total_price - discount
    print("A 10% discount applied.")
else:
    final_price = total_price
    print("No discount applied.")
print("Final bill amount: PKR", final_price)