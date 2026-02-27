delivery = int(input("Please insert the kilometers to check the value: "))
rain_input = input("Is it raining? (T/F): ").strip().upper()

tax = 2.00
value = 0

# Convertendo para boolean corretamente
rain = True if rain_input == "T" else False

# Definindo valor base por quilometragem
if delivery <= 5:
    value = 5.00
elif delivery <= 10:
    value = 8.00
else:
    value = 10.00

# Acrescenta taxa se estiver chovendo
if rain:
    value += tax

print(f"The final value is: R$ {value:.2f}")