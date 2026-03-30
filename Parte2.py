import csv

maxval1 = 0
maxval2 = 0

minval1 = 999
minval2 = 999

valorA = []
valorS = []

contagem1 = 0
contagem2 = 0

with open('Pokemon.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        a = linha['Attack']
        b = linha['Speed']

        valorA.append(int(linha['Attack']))
        valorS.append(int(linha['Speed']))
        

        if int(a) > int(maxval1):
            maxval1 = a
        if int(b) > int(maxval2):
            maxval2 = b
        if int(a) < int(minval1):
            minval1 = a 
        if int(b) < int(minval2):
            minval2 = b

        if int(a) > 0:
            contagem1 += 1
        if int(b) > 0:
            contagem2 += 1
            

    
    mediaA = sum(valorA) / len(valorA)
    mediaS = sum(valorS) / len(valorS)

    print(f'Máximo de Attack: {maxval1}')
    print(f'Máximo de Speed: {maxval2}')

    print(f'Mínimo de Attack: {minval1}')
    print(f'Mínimo de Speed: {minval2}')

    print(f'Média Attack: {mediaA:.2f}')
    print(f'Média Speed: {mediaS:.2f}')

    print(f'Registros de Attack: {contagem1}')
    print(f'Registros de Speed: {contagem2}')