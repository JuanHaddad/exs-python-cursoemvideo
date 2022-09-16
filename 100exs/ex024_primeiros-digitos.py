#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome de uma cidade: ')).capitalize()
comeco = cidade.split()
if comeco[0] == 'Santo':
    print('Sua cidade começa com Santo.')
else:
    print('Sua cidade nao começa com Santo.')