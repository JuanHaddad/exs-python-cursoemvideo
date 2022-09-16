#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.


numero = int(input('Digite um numero de 0 a 9999: '))
lista = []
lista.append(numero % 10)
lista.append((numero % 100) / 10)
lista.append((numero % 1000) / 100)
lista.append(numero / 1000)
for i, elemento in enumerate(lista):
    if elemento >= 1:
        if i == 0:
            print(f'Unidade: ', end='')
        elif i == 1:
            print(f'Dezena: ', end='')
        elif i == 2:
            print(f'Centena: ', end='')
        else:
            print(f'Milhar: ', end='')
    print(f'{int(elemento)}')