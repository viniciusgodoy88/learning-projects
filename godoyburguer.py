print ("Welcome to Godoy's burger! Please inform the quantity for the below products to receive a receipt!")

burguer = 12.00
frenchfries = 7.00
soda = 5.00

burguer = float (input("Please insert the quantity of hamburguer: "))
frenchfries = float (input ("Please insert the quantity of French Fries: "))
soda = float (input ("Please insert the quantity of Soda: "))

quantity_burguer = burguer * 12
quantity_frenchfries = frenchfries * 7 
quantity_soda = soda * 5

receipt = quantity_burguer + quantity_frenchfries + quantity_soda

print("Your receipt value is: ",receipt)