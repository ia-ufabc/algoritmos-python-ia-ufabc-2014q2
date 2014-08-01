# Nome: Alamo Pereira Saravali
# RA: 11097810
# Email: alamo.saravali@gmail.com / alamo.saravali@aluno.ufabc.edu.br

from random import shuffle, randrange
 
def labrinto(largura, altura):
    celulas = [[0] * largura + [1] for _ in range(altura)] + [[1] * (largura + 1)]
    vertical = [["|  "] * largura + ['|'] for _ in range(altura)] + [[]]
    horizontal = [["+--"] * largura + ['+'] for _ in range(altura + 1)]

    def print_lab():
        lab = ''
        for (a, b) in zip(horizontal, vertical):
            if lab:
                lab += '\n'
            lab += ''.join(a + ['\n'] + b)
        print lab
    
    print "=> Labirinto construido:"
    print_lab()

    def busca_profundidade(x, y, xfinal, yfinal):

        def marcar_caminho(x, y):
            primeiro_caractere = vertical[y][x][:1]
            marca = "o"
            ultimo_caractere = vertical[y][x][2:]
            vertical[y][x] = ''.join(primeiro_caractere + marca + ultimo_caractere)

        def marcar_visitada(x, y):
            primeiro_caractere = vertical[y][x][:1]
            marca = "x"
            ultimo_caractere = vertical[y][x][2:]
            vertical[y][x] = ''.join(primeiro_caractere + marca + ultimo_caractere)

        def get_vizinho(x, y):
            possibilidades = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(possibilidades)
            vizinho = []
            for (v1, v2) in possibilidades:
                if celulas[v2][v1]: continue
                if v1 == x: horizontal[max(y, v2)][x] = "+  "
                if v2 == y: vertical[y][max(x, v1)] = "   "
                vizinho = [v1, v2]
                break
            return vizinho


        # Marca a primeira celula como visitada e adiciona na pilha
        pilha = []
        pilha.append([x, y])
        print '\n'
        print '=> Pilha:'
        print pilha
        print '\n'
        print_lab()

        x = 0
        y = 0
        v1 = 0
        v2 = 0
        while len(pilha) > 0:
            celula = pilha.pop()
            x = celula[0]
            y = celula[1]
            celulas[y][x] = 1

            marcar_visitada(x, y)

            # Verifica se ja eh o ponto final e finaliza
            if x == xfinal and y == yfinal:
                # Marca celula como caminho
                marcar_caminho(x, y)
                pilha = []
            # Caso contrario, continue a busca
            else:
                vizinho = get_vizinho(x, y)

                if(vizinho):
                    v1 = vizinho[0]
                    v2 = vizinho[1]
                    
                    # Marca celula como caminho
                    marcar_caminho(x, y)

                    #Adiciona celular e vizinho na pilha
                    pilha.append([x, y])
                    pilha.append([v1, v2])

            print_lab()

    # Gera pontos aleatorios
    while True:
        inicio1 = randrange(largura)
        inicio2 = randrange(altura)
        final1 = randrange(largura)
        final2 = randrange(altura)

        # Se forem posicoes diferentes, quebra o ciclo
        if inicio1 != final1 and inicio2 != final2:
            break

    # Imprime os pontos
    print ''.join('Ponto inicial: [' + str(inicio1) + ', ' + str(inicio2) + ']')
    print ''.join('Ponto final: [' + str(final1) + ', ' + str(final2) + ']')

    # Reseolve o labirinto com busca em profundidade
    busca_profundidade(inicio1, inicio2, final1, final2) # Marca A como inicial
 
labrinto(3, 3)