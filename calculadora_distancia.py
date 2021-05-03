# Variables
price_comb = float(input("Valor do Combustível: "))
distance = float(input("Distância Percorrida: "))
km_liter = float(input("Quantos KM/L: "))

# Litragem Gasta No Percurso
liter = distance/km_liter

# Preço do Que Foi Gasto
result = liter * price_comb

print("Você gastou ", liter, "L na sua viagem \n")
print("Você precisa repor R$", result, " do seu tanque de combustível!")
