# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite um valor em Metros(m): '))
cm = m*100
mm = cm*10
print(f'O valor de {m}m é:\nEm centímetros: {cm:.1f}cm\nEm milímetros: {mm}mm')
