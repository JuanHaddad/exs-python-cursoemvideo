# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input('Digite a largura da parede (m): '))
h = float(input('Agora a altura(m): '))
a = l*h
print(f'Sabendo que a área da parede é {a:.1f}m², você precisará de {a/2:.2f}l de tinta!')