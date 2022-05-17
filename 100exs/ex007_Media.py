def linha():
    print('-'*32)

linha()
print('ALUNO JOHNSON'.center(32))
linha()
n1 = float(input('1° Nota de Johnson: '))
n2 = float(input('2° Nota de Johnson: '))
m = (n1+n2)/2
linha()
print(f'A média de Johnson foi {m:.1f}')
