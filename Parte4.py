from Parte1 import contador, coluna

with open("Relatório.txt", 'w', encoding='utf-8') as arquivo:
    dataset = 'Pokemon.csv'
    arquivo.write(f'Nome do Dataset usado: {dataset}\n')
    arquivo.write(f'Descrição Breve: O dataset usado é sobre os Pokemons da 3° geração dos jogos de Pokemon.\n')

    arquivo.write(f'Quantidade de registros: {contador}\n')
    arquivo.write(f'Quantidade de colunas: {coluna}\n')