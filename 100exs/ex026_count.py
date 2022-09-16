#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: \n'))
print(f'letra A aparece {frase.count("a")}x')
print(f'letra A aparece pela primeira vez na posição {frase.find("a")} e pela ultima vez na posição {frase.rfind("a")}')