# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número para tabuada: '))
for i in range(1, 11):
    print(f'{n:<3}x{i:>3} = {n*i}')
