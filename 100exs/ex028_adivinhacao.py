# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0
# e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint

computador = randint(0, 5)
print(f'Tente adivinhar o que o computador pensou...')
jogador = int(input(f'Escolha um numero de 0 a 5: '))
if jogador == computador:
    print(f'Uau, você ACERTOU, os dois escolheram {computador}')
else:
    print(f'Nao foi dessa vez, o pc escoolheu {computador} e voce {jogador}')