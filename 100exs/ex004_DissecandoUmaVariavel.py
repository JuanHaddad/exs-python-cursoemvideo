# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

msg = str(input('Digite qualquer coisa: '))
print(f'Qual o tipo? {type(msg)}')
print(f'Quantos caracteres totais: {len(msg)}')
print(f'É uma frase numérica? {msg.isnumeric()}')
print(f'É alfanumérica? {msg.isalnum()}')
print(f'É alfabética? {msg.isalpha()}')
print(f'Só tem espaços? {msg.isspace()}')
print(f'Está capitalizado? {msg.isidentifier()}')
print(f'Está em maiúsculo? {msg.isupper()}')
print(f'EStá em minúsculo? {msg.islower()}')
