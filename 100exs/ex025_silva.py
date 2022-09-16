#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nomecompleto = str(input('Digite seu nome completo: ')).lower()
if 'silva' in nomecompleto:
    print('Você tem Silva no seu nome, boa!')
else:
    print(f'Você não tem silva no seu nome... aff...')