import math

reais = float(input("Informe quantos reais você tem para trocar: "))
dolares = reais / 5.73

print(f"Você pode trocar por ${math.floor(dolares):.2f} dolares")

"""
import math
reias = float(input("Digite quantos reais você tem: "))
dolar = reias // 5.51

print(f"O valor em dolar vai ser: {math.floor(dolar)}")
"""