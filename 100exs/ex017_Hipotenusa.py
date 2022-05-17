# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

c1 = float(input('1° cateto: '))
c2 = float(input('2° cateto: '))
hip = (c1**2+c2**2) ** (1/2)
print(f'No triângulo com os catetos {c1} e {c2} têm a hipotenusa igual a {hip:.2f}')
