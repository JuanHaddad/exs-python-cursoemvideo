# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Qual o preço do produto? R$'))
np = p - (p * 0.05)
print(f'O novo preço com 5% de desconto aplicado é R${np:,.2f} !!')