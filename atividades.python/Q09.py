op = '1'
import time

while op  != '0':
    time.sleep(1)
    print('''      --* calc.py *--
          digite
          1 - soma
          2 - subtração
          3 - divisão
          4 - multiplicação
          5 - exponênciação ao quadrado
          0 - sair
          ''')
    op = input(' ')
    if op == '1':
        print('você escolheu soma')
        n1 = int(input('digite n1: ')) 
        n2 = int(input('digite n2: ')) 
        print(f'{n1} + {n2} = {n1 + n2}')
        print(' ') 
    elif op == '2':
        print('você escolheu subtração')
        n1 = int(input('digite n1: ')) 
        n2 = int(input('digite n2: ')) 
        print(f'{n1} - {n2} = {n1 - n2}')
        print(' ')
    elif op == '3':
        print('você escolheu divisão')
        n1 = int(input('digite n1: ')) 
        n2 = int(input('digite n2: ')) 
        print(f'{n1} / {n2} = {n1 / n2}')
        print(' ')
    elif op == '4':
        print('você escolheu multiplicação')
        n1 = int(input('digite n1: ')) 
        n2 = int(input('digite n2: ')) 
        print(f'{n1} * {n2} = {n1 * n2}')
        print(' ')
    elif op == '5':
        print('você escolheu exponênciação ao quadrado')
        n1 = int(input('digite n1: '))  
        print(f'{n1}^ = {n1 ** 2}')
        print(' ')
    elif op == '0':
        print('bye, bye...')
        break
    else:
        print('inválido,tente novamente...')
        print(' ')