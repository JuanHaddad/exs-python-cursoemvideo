#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nomecompleto = str(input('Digite seu nome completo: '))
nome = nomecompleto.split()
print(f'Seu primeiro nome é {nome[0]} e o ultimo é {nome[len(nome)-1]}')