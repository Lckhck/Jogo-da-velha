#Jogo da velha
ganhador = False

tabuleiro = [
<<<<<<< HEAD
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
=======
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['O', 'X', 'O']
>>>>>>> parent of 4678ca2 (Implementação da verificação de espaços em branco, que não foram feitas jogadas no tabuleiro.)
]

comecar = int(input("Qual player começará a jogar? 1 ou 2?"))
player1 = 1 if comecar == 1 else 0
player2 = 1 if comecar == 2 else 0
escolhidos = []
mapeamento_linha = 0
mapeamento_coluna = 0
numero_colunas = len(tabuleiro)
x = 0
y = 0
linhas = 0
colunas = 0

while ganhador == False:

<<<<<<< HEAD
    if player1 == 1:
        posicao_escolhida = int(input("(Player 1) Escolha uma posição para jogar de 1 a 9: "))
        if posicao_escolhida < 1 or posicao_escolhida > 9:
            print(f"Posição {posicao_escolhida+1} inválida!")
            continue
        posicao_escolhida -= 1
        if posicao_escolhida in escolhidos:
            print("Posição já escolhida, escolha outra posição!")
            continue


        mapeamento_linha = posicao_escolhida // numero_colunas
        mapeamento_coluna = posicao_escolhida % numero_colunas
        tabuleiro[mapeamento_linha][mapeamento_coluna] = 'X'
        player1 = 0
        player2 = 1
        escolhidos.append(posicao_escolhida)

    elif player2 == 1:
        posicao_escolhida = int(input("(Player 2) Escolha uma posição para jogar de 1 a 9: "))
        if posicao_escolhida < 1 or posicao_escolhida > 9:
            print(f"Posição {posicao_escolhida+1} inválida!")
            continue
        posicao_escolhida -= 1
        if posicao_escolhida in escolhidos:
            print("Posição já escolhida, escolha outra posição!")
            continue

        mapeamento_linha = posicao_escolhida // numero_colunas
        mapeamento_coluna = posicao_escolhida % numero_colunas
        tabuleiro[mapeamento_linha][mapeamento_coluna] = 'O'
        player1 = 1
        player2 = 0
        escolhidos.append(posicao_escolhida)
        
    while True:      
        print('Coluna inicial:', colunas)
        #Verifica se a posição atual representa o X, se sim incrementa +1 na variável X
        if colunas == 3:
            colunas = 0
        if tabuleiro[linhas][colunas] == 'X':

                #Esses prints são para testes
                print(f'linha: {linhas}, coluna: {colunas}')
                print(f'{tabuleiro[linhas][colunas]}')
                print(x)

                #Verifica se x é igual a 3, se sim o X ganha
                if x == 3:
                    print(f'Ganhou X na coluna {colunas + 1}')
                    print(f'Player 1 ganhou')
                    ganhador = True
                    break
                
                #Incrementa +1 na linha para percorrer as linhas, mas mantendo a coluna

                linhas += 1
                print('-'*10)
        elif tabuleiro[linhas][colunas] == '':
            linhas += 1
        else:
                x += 1


        #Se a linha é 3 reinicia as variáveis linhas, x e y. Incrementa +1 pra coluna
        if linhas == 3:
            linhas = 0
            colunas += 1
            x = 0
            y = 0
            #Realiza a verificação da coluna, se chegou na coluna 2 zera as colunas e acaba o laço de repetição
            if colunas == 3:
                colunas = 0
                break

        #Verifica se a posição atual representa o O, se sim incrementa +1 na variável Y
        if tabuleiro[linhas][colunas] == 'O' or tabuleiro[linhas][colunas] == '':
            if tabuleiro[linhas][colunas] == '':
                linhas += 1
            else:
                y += 1

                #Esses prints são para testes
                print(f'linha: {linhas}, coluna: {colunas}')
                print(f'{tabuleiro[linhas][colunas]}')
                print(y)

                #Verifica se y é igual a 3, se sim o O ganha
                if y == 3:
                    print(f'Ganhou O na coluna {colunas + 1}')
                    print(f'Player 2 ganhou')
                    ganhador = True
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
            if colunas == 3:
                colunas = 0
                break
            
    #Parte do algoritmo para verificar a diagonal principal no jogo
    while True:
        if (linhas > 2 or colunas > 2) or tabuleiro[linhas][colunas] == '':
            linhas = 0
=======
while True:

    #Verifica se a posição atual representa o X, se sim incrementa +1 na variável X
    print(colunas)
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
        #Realiza a verificação da coluna, se chegou na coluna 2 zera as colunas e acaba o laço de repetição
        if colunas == 3:
>>>>>>> parent of 4678ca2 (Implementação da verificação de espaços em branco, que não foram feitas jogadas no tabuleiro.)
            colunas = 0
            x = 0
            y = 0
            break

<<<<<<< HEAD
        if tabuleiro[linhas][colunas] == 'X':
            x += 1
            linhas += 1
            colunas += 1
            if x == 3:
                print('Ganhou X na diagonal principal')
                print('Player 1 ganhou')
                ganhador = True
                break

        if (linhas > 2 or colunas > 2) or tabuleiro[linhas][colunas] == '':
            linhas = 0
            colunas = 0
            x = 0
            y = 0
            break

=======
    print(colunas)
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
        if colunas == 3:
            colunas = 0
            break
         
#Parte do algoritmo para verificar a diagonal principal no jogo
while True:
    if linhas > 2 or colunas > 2:
        linhas = 0
        colunas = 0
        x = 0
        y = 0
        break

    if tabuleiro[linhas][colunas] == 'X':
        x += 1
        linhas += 1
        colunas += 1
        if x == 3:
            print('Ganhou X na diagonal principal')
            break
    if tabuleiro[linhas][colunas] == 'O':
        y += 1
        linhas += 1
        colunas += 1
        if y == 3:
            print('Ganhou Y na diagonal principal')
            break


#Parte do algoritmo para verificar a diagonal secundária no jogo
colunas = 2 #Define a coluna para começar a contar do 2 porque funciona no inverso para essa diagonal
while True:
    if linhas > 2 or colunas < 0: #Parque que faz a checagem para encerrar o laço caso não tenha nenhum ganhador nessa diagonal
        x = 0
        y = 0
        break
    if tabuleiro[linhas][colunas] == 'X':
        x += 1
        #Aqui faz uma lógica de incremento nas linhas e decremento nas colunas, para conseguir mapear na diagonal secundária
        linhas += 1
        colunas -= 1
        if x == 3:
            print('Ganhou X na diagonal secundária')
            break

    if tabuleiro[linhas][colunas] == 'O':
        y += 1
        #Aqui faz uma lógica de incremento nas linhas e decremento nas colunas, para conseguir mapear na diagonal secundária
        linhas += 1
        colunas -= 1
        if y == 3:
            print('Ganhou Y na diagonal secundária')
            break


print('-'*20)
#Reiniciando variáveis
x = 0
y = 0
linhas = 0
colunas = 0

while True:

    #Algoritmo para percorrer a matriz do tabuleiro do jogo da velha na horizontal, apenas checando as linhas.
    if linhas == 2 and colunas == 3: #Verifica se a matriz chegou no final para parar o programa.
        break
    if colunas == 3: #Verifica se a coluna é igual a 3 para zerar a coluna e incrementar a linha e começar a verificar a próxima linha.
        colunas = 0
        linhas += 1
        x = 0
        y = 0
    

    if colunas < 3 and linhas < 3:
        print('colunas: ', colunas, 'Linhas:', linhas, tabuleiro[linhas][colunas])
        
        #Algoritmo para verificar se o X ou o O ganhou na horizontal, verifica pela quantidade de pontos
        if tabuleiro[linhas][colunas] == 'X':
                x += 1
                print(f'X: {x}')
                if x == 3: # se x for igual a 3 significa que bateu os 3 pontos da linha e ganhou
                    print('Ganhou X')
                    break
>>>>>>> parent of 4678ca2 (Implementação da verificação de espaços em branco, que não foram feitas jogadas no tabuleiro.)
        if tabuleiro[linhas][colunas] == 'O':
            y += 1
            linhas += 1
            colunas += 1
            if y == 3:
                print('Ganhou O na diagonal principal')
                print('Player 2 ganhou')
                ganhador = True
                break


    #Parte do algoritmo para verificar a diagonal secundária no jogo
    colunas = 2 #Define a coluna para começar a contar do 2 porque funciona no inverso para essa diagonal
    while True:
        if (linhas > 2 or colunas < 0) or tabuleiro[linhas][colunas] == '': #Parque que faz a checagem para encerrar o laço caso não tenha nenhum ganhador nessa diagonal
            x = 0
            y = 0
            break
        
        if tabuleiro[linhas][colunas] == 'X':
            x += 1
            #Aqui faz uma lógica de incremento nas linhas e decremento nas colunas, para conseguir mapear na diagonal secundária
            linhas += 1
            colunas -= 1
            if x == 3:
                print('Ganhou X na diagonal secundária')
                print('Player 1 ganhou')
                ganhador = True
                break

        if (linhas > 2 or colunas < 0) or tabuleiro[linhas][colunas] == '': #Parque que faz a checagem para encerrar o laço caso não tenha nenhum ganhador nessa diagonal
            x = 0
            y = 0
            break
        
        if tabuleiro[linhas][colunas] == 'O':
            y += 1
            #Aqui faz uma lógica de incremento nas linhas e decremento nas colunas, para conseguir mapear na diagonal secundária
            linhas += 1
            colunas -= 1
            if y == 3:
                print('Ganhou O na diagonal secundária')
                print('Player 2 ganhou')
                ganhador = True
                break


    print('-'*20)
    #Reiniciando variáveis
    linhas = 0
    colunas = 0

    while True:

        #Algoritmo para percorrer a matriz do tabuleiro do jogo da velha na horizontal, apenas checando as linhas.
        if linhas == 2 and colunas == 3: #Verifica se a matriz chegou no final para parar o programa.
            break
        if colunas == 3: #Verifica se a coluna é igual a 3 para zerar a coluna e incrementar a linha e começar a verificar a próxima linha.
            colunas = 0
            linhas += 1
            x = 0
            y = 0


        if colunas < 3 and linhas < 3:
            print('colunas: ', colunas, 'Linhas:', linhas, tabuleiro[linhas][colunas])

            #Algoritmo para verificar se o X ou o O ganhou na horizontal, verifica pela quantidade de pontos
            if tabuleiro[linhas][colunas] == 'X':
                    x += 1
                    print(f'X: {x}')
                    if x == 3: # se x for igual a 3 significa que bateu os 3 pontos da linha e ganhou
                        print(f'Ganhou X na linha {linhas}')
                        print('Player 1 ganhou')
                        ganhador = True
                        break
            if tabuleiro[linhas][colunas] == 'O':
                y += 1
                print(f'O: {y}')
                if y == 3: # se y for igual a 3 significa que bateu os 3 pontos da linha e ganhou
                     print(f'Ganhou O na linha {linhas}')
                     print('Player 2 ganhou')
                     ganhador = True
                     break
                 
        colunas += 1