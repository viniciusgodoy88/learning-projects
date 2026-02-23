'''
Bruno manages a small business and wants to know which product 
had the best sales performance last month.

He recorded the quantity sold of two products: apples and bananas.

Now, he needs to write a program that identifies and 
displays which one had higher sales.

Create a program that receives the number of sales of the two products 
and displays a message indicating which one sold more.

If the quantities are equal, display a message saying that there was a tie.

'''
apples = int(input("Enter the number of apples sold: "))
bananas = int(input("Enter the number of bananas sold:"))

if apples > bananas:
    print("Apples had higher sales")
elif bananas > apples:
    print("Bananas had higher sales")
else:
    print("Sales were the same.")

    