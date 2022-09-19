# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('digite um numero inteiro: '))
if num % 2 == 0:
    print(f'{num} é IMPAR.')
else:
    print(f'{num} é PAR.')