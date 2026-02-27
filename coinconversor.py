print("Coin Conversor")

def conversorRStoUS(reais_value, exchange_rate):
    conversor_value = reais_value / exchange_rate
    return conversor_value

# Entrada de dados
reais = float(input("Insert the value in Reais: "))
rate = float(input("Insert the exchange rate (USD): "))

# Chamando a função
d = conversorRStoUS(reais, rate)

print("Value in U$: ", d)
