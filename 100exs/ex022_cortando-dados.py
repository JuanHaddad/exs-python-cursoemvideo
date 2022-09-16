""" Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome. """

nomecompleto = str(input('Digite seu nome completo: '))
print(f'Maiusculas: {nomecompleto.upper()}')
print(f'Minusculas: {nomecompleto.lower()}')
semespaços = nomecompleto.replace(' ', '')
print(f'Seu nome completo tem {len(semespaços)} letras')
nome = nomecompleto.split()
print(f'Seu primeiro nome é {nome[0]}')