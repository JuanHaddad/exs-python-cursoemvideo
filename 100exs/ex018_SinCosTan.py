# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan
ang = float(input('Digite um ângulo: '))
print(f'Sen{ang}°: {sin(ang):.2f}\nCos{ang}°: {cos(ang):.2f}\nTan{ang}°: {tan(ang):.2f}')
