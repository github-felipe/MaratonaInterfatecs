x = int(input('Insira o valor x: '))
y = int(input('Insira o valor y: '))

if 1 <= x <= 100 and 1 <= y <= 100:
    print(f'{x}\n{y}')
    print(f'{y}\n{x}')
    print(f'{y}\n{x*-1}')
    print(f'{x}\n{y*-1}')
    print(f'{x*-1}\n{y*-1}')
    print(f'{y*-1}\n{x*-1}')
    print(f'{y*-1}\n{x}')
    print(f'{x*-1}\n{y}')
else:
    print('ERRO')