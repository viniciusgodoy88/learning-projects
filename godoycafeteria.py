# This variable requests the number of items the customer will request
itenscustumerrequest = int(input("Insert the itens the custumer will request: "))
total = 0

# This variable requests how many items need to be registered
quantity = int(input("How many itens you want to register?: "))

# Loop to register items and prices
for i in range(quantity):
    print(f"\nItem {i+1}")
    
    name = input("Insert the item name: ")
    price = float(input("Insert the item value:R$ "))
    
    total += price 

print("\n=== Purchase Summary ===")
print(f"Total purchase amount: R$ {total:.2f}")

# Check if customer is registered
registercustumer = input("Customer is registered? (T/F): ").strip().upper()
registred = True if registercustumer == "T" else False

# Apply discount only if registered
if registred:
    discount = total * 0.10
    total_receipt = total - discount
else:
    total_receipt = total

print(f"Total to pay: R$ {total_receipt:.2f}")