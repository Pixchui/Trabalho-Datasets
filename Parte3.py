import csv

contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0

with open('Pokemon.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)

    print('Filtro 1: Pokemon Ghost com Total de Stats maior que 300:')
    for linha in leitor:
        a = linha['Type 1']
        b = linha['Total']
        c = linha['Name']

        if a == 'Ghost' and int(b) > 300:
            contador1 += 1
            print(f'{contador1}: {c}')

with open('Pokemon.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    
    print('Filtro 2: Pokemon com segundo tipo Ground com Defense maior que 60:')
    for linha in leitor:
        a = linha['Type 2']
        b = linha['Defense']
        c = linha['Name']

        if a == 'Ground' and int(b) > 60:
            contador2 += 1
            print(f'{contador2}: {c}')

with open('Pokemon.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    
    print('Filtro 3: Pokemon com Total de Stats maior que 500 e com HP maior que 100:')
    for linha in leitor:
        a = linha['Total']
        b = linha['HP']
        c = linha['Name']

        if int(a) > 500  and int(b) > 100:
            contador3 += 1
            print(f'{contador3}: {c}')

with open('Pokemon.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    
    filtro1 = input("Digite o primeiro tipo do Pokemon: ")
    filtro2 = input("Qual o segundo filtro vocẽ quer?: ")
    filtro3 = int(input("Digite o valor do segundo filtro: "))
    filtro4 = input("Maior ou menor?: ")

    for linha in leitor:
        a = linha['Type 1']
        b = linha[filtro2]
        c = linha['Name']

        if filtro4 == 'maior':
            if a == filtro1 and int(b) > filtro3:
                contador4 += 1
                print(f'{contador4}: {c}')
        
        if filtro4 == 'menor':
            if a == filtro1 and int(b) < filtro3:
                contador4 += 1
                print(f'{contador4}: {c}')