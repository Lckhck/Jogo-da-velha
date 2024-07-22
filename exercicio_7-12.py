#Jogo da velha
ganhador = False

tabuleiro = [
    ['O', 'X', 'O'],
    ['O', 'O', 'X'],
    ['O', 'X', 'O']
]

x = 0
y = 0
vertical_O = 0
vertical_X = 0
linhas = 0
colunas = 0
#while ganhador == False:

#Algoritmo para percorrer e analisar as colunas do tabuleiro. Identifica se ganhou pela coluna

while True:
    #Verifica se chegou no final da checagem de colunas e paga o laço de repetição
    if colunas == 3:
        linhas = 0
        colunas = 0
        break

    #Verifica se a posição atual representa o X, se sim incrementa +1 na variável X
    if tabuleiro[linhas][colunas] == 'X':
        x += 1

        #Esses prints são para testes
        print(f'linha: {linhas}, coluna: {colunas}')
        print(f'{tabuleiro[linhas][colunas]}')
        print(x)
        
        #Verifica se x é igual a 3, se sim o X ganha
        if x == 3:
            print(f'Ganhou X na coluna {colunas + 1}')
            break
        
        #Incrementa +1 na linha para percorrer as linhas, mas mantendo a coluna
        linhas += 1
        print('-'*10)

    #Se a linha é 3 reinicia as variáveis linhas, x e y. Incrementa +1 pra coluna
    if linhas == 3:
            linhas = 0
            colunas += 1
            x = 0
            y = 0

    #Verifica se a posição atual representa o O, se sim incrementa +1 na variável Y
    if tabuleiro[linhas][colunas] == 'O':
        y += 1

        #Esses prints são para testes
        print(f'linha: {linhas}, coluna: {colunas}')
        print(f'{tabuleiro[linhas][colunas]}')
        print(y)

        #Verifica se y é igual a 3, se sim o O ganha
        if y == 3:
            print(f'Ganhou O na coluna {colunas + 1}')
            break

        #Incrementa +1 na linha para percorrer as linhas, mas mantendo a coluna
        linhas += 1
        print('-'*10)

    #Se a linha é 3 reinicia as variáveis linhas, x e y. Incrementa +1 pra coluna
    if linhas == 3:
            linhas = 0
            colunas += 1
            x = 0
            y = 0
         

print('-'*20)
#Reiniciando variáveis
x = 0
y = 0
linhas = 0
colunas = 0

while True:

    #Algoritmo para percorrer a matriz do tabuleiro do jogo da velha.
    if linhas == 2 and colunas == 3: #Verifica se a matriz chegou no final para parar o programa.
        break
    if colunas == 3: #Verifica se a coluna é igual a 3 para zerar a coluna e incrementar a linha e começar a verificar a próxima linha.
        colunas = 0
        linhas += 1
        x = 0
        y = 0
    

    if colunas < 3 and linhas < 3:
        print('colunas: ', colunas, 'Linhas:', linhas, tabuleiro[linhas][colunas])
        
        #Algoritmo para verificar se o X ou o O ganhou, verifica pela quantidade de pontos
        if tabuleiro[linhas][colunas] == 'X':
                x += 1
                print(f'X: {x}')
                if x == 3: # se x for igual a 3 significa que bateu os 3 pontos da linha e ganhou
                    print('Ganhou X')
                    break
        if tabuleiro[linhas][colunas] == 'O':
            y += 1
            print(f'O: {y}')
            if y == 3: # se y for igual a 3 significa que bateu os 3 pontos da linha e ganhou
                 print('Ganhou Y')
                 break
            
    colunas += 1