# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('-'*32)
print('ALUGANDO CARRO'.center(32))
print('-'*32)
d = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos Km foram rodados? '))
p = (d*60)+(km*0.15)
print(f'O total à pagar é R${p:,.2f}')