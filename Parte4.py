from Parte1 import contador, coluna
from Parte2 import maxval1, maxval2, minval1, minval2, mediaA, mediaS, contagem1, contagem2
from Parte3 import filtro1, filtro2, filtro3
import os

conta = 0

os.system('cls' if os.name == 'nt' else 'clear')

with open("Relatório.txt", 'w', encoding='utf-8') as arquivo:
    dataset = 'Pokemon.csv'

    arquivo.write(f'Nome do Dataset usado: {dataset}\n')
    arquivo.write(f'''Descrição Breve: O dataset usado é sobre os Pokemons da 3° geração dos jogos de Pokemon.
Ele contém informações sobre os atributos dos Pokemons, como Total de Stats, HP, Attack, Defense, Speed, entre outros.
Também contém informações sobre os tipos dos Pokemons, como Type 1 e Type 2, e também seu número na Pokedex oficial.
Essas informações podem ser usadas para realizar análises e encontrar Pokemons com características específicas, como os filtros aplicados na Parte 3.\n''')

    arquivo.write(f'\n')

    arquivo.write(f'Quantidade de registros: {contador}\n')

    for i in coluna:
        conta += 1

    arquivo.write(f'Quantidade de colunas: {conta}\n')
    arquivo.write(f'Nome das colunas: {coluna}\n')
    
    arquivo.write(f'\n')

    arquivo.write(f'Estatísticas da Parte 2:\n')
    arquivo.write(f'Máximo de Attack: {maxval1}\n')
    arquivo.write(f'Máximo de Speed: {maxval2}\n')
    arquivo.write(f'Mínimo de Attack: {minval1}\n')
    arquivo.write(f'Mínimo de Speed: {minval2}\n')
    arquivo.write(f'Média de Attack: {mediaA:.2f}\n')
    arquivo.write(f'Média de Speed: {mediaS:.2f}\n')
    arquivo.write(f'Quantidade de registros de Attack: {contagem1}\n')
    arquivo.write(f'Quantidade de registros de Speed: {contagem2}\n')

    arquivo.write(f'\n')
    arquivo.write(f'Estatísticas da Parte 3:\n')
    arquivo.write(f'Filtro 1: Pokemon Ghost com Total de Stats maior que 300:\n')
    arquivo.write(f'{filtro1}\n')
    arquivo.write(f'Filtro 2: Pokemon com segundo tipo Ground com Defense maior que 60:\n')
    arquivo.write(f'{filtro2}\n')
    arquivo.write(f'Filtro 3: Pokemon com Total de Stats maior que 500 e com HP maior que 100:\n')
    arquivo.write(f'{filtro3}\n')
    arquivo.write(f'Filtro Interativo: O usuário pode aplicar filtros personalizados ao dataset.\n')

    arquivo.write(f'\n')

    arquivo.write(f'''Conclusão: O dataset é bem completo, com muitas informações sobre os Pokemons da 3° geração. 
Através dos filtros aplicados, foi possível encontrar Pokemons com características específicas, como os 
únicos Pokemons com tipo Ghost e com Total de Stats maior que 300, sendo Banette e Dusclops.
Também foi possível encontrar a média de Attack e Speed dos Pokemons, sendo {mediaA:.2f} e {mediaS:.2f}, respectivamente.
E também foi possível saber quantos Pokemons da 3° geração existem na Pokedex, sendo {contador} registros. 
O dataset é uma ótima fonte de informações para quem gosta de Pokemon e quer realizar análises sobre os Pokemons da 3° geração.''')
    
