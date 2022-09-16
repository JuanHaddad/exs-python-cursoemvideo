# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import randint
from time import sleep

alunos = []
for aluno in range(1,5):
    alunos.append(input(f'Qual o nome do {aluno}° aluno? '))
sorteados = []
while len(sorteados) < len(alunos):
    numero = randint(0,3)
    if alunos[numero] not in sorteados:
        sorteados.append(alunos[numero])
print('Os sorteados foram...')
for indice in range(0,4):
    print(f'{indice+1}° - {sorteados[indice]}')