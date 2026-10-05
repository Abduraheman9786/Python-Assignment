cost_price=float(input("Enter cost price : "))
Selling_price=float(input("Enter Selling Price : "))

if Selling_price>cost_price:
    print("profit =",Selling_price-cost_price)
else:
    print("Loss =",cost_price-Selling_price)