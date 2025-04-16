a = int(input('Insira a quantidade de frascos: '))
b = int(input('Insira o passo no qual deve ser removido as garrafas: '))

frascos = list(range(a))
atual = -1
while len(frascos) > 1:
    for c in range(b):
        if atual < len(frascos) -1:
            atual += 1
        else:
            atual = 0
    frascos.pop(atual)
    atual -= 1

print(int(frascos[0]) + 1)