'''
Fernanda is planning a trip and wants to calculate 
how much she will pay in tolls. 
The toll amount depends on the distance traveled:

Up to 100 km: R$ 10.00
Between 100 km and 200 km: R$ 20.00
Above 200 km: R$ 30.00

Create a program that receives the distance traveled and displays 
the corresponding toll amount.
'''
tool = int(input("Enter the kilometers to find out how much you will need to pay in tolls: "))

if tool <= 100:
    print("You need to pay R$10,00")
elif 100 < tool <= 200:
    print("You need to pay R$20,00")
else:
    print ("You need to pay R$30,00")