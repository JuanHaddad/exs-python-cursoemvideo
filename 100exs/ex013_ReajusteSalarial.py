# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Qual o salário atual do Pedrinho? R$'))
ns = s + (s * 0.15)
print(f'Pedrinho !AMASSOU! na empresa e recebeu um aumento de 15%!\nSalário antigo --> R${s:.2f}\nSalário atual --> R${ns:.2f}')