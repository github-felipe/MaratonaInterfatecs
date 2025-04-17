n = int(input('Insira quantas sequências de captura: '))

for i in range(n):
    entradas = input('Insira a sequência de entrada: ')
    l1 = True
    l2 = True
    l3 = True
    saidas = ''
    for ent in entradas:
        if ent == 'A':

            if l1:
                saidas += 'D'
                l1 = False
            
            else:
                l1 = True
                if l2:
                    saidas += 'D'
                    l2 = False
                
                else:
                    saidas += 'E'
                    l2 = True
        elif ent == 'B':
            if l2:
                saidas += 'D'
                l2 = False
                
            else:
                saidas += 'E'
                l2 = True

        elif ent == 'C':
            if l3:
                l3 = False
                if l2:
                    saidas += 'D'
                    l2 = False
                
                else:
                    saidas += 'E'
                    l2 = True
            else:
                saidas += 'E'
                l3 = True
    print(saidas)
