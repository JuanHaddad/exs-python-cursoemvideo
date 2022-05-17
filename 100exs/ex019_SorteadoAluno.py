# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import randint

nomes = []
for i in range(1,5):
    nome = str(input(f'Digite o {i}° nome: '))
    nomes.append(nome)
sorteado = nomes[randint(0,3)]
print(f'O aluno sorteado a apagar a lousa foi o {sorteado}')