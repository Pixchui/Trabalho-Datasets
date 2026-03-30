import csv

contador = 0
dados = []
reg = []

with open('Pokemon.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for registro in leitor:
        contador += 1
        if contador < 6:
            reg.append(registro)

    for pin in arquivo:
        dados.append([pin])

    
    
    dataset = 'Pokemon.csv'
    coluna = leitor.fieldnames

    print(f'Dataset: {dataset}')
    print(f'Quantidade de Registros: {contador}')
    print(f'Nome das Colunas: {coluna}')
    print(f'5 Primeiros Registros: {reg}')