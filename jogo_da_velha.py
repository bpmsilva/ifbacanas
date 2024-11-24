class Jogo:
    def __init__(self):
        self.lista = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def imprime_tabuleiro(self):
        print(self.lista[0] + '|' + self.lista[1] + '|' + self.lista[2])
        print('-|-|-')
        print(self.lista[3] + '|' + self.lista[4] + '|' + self.lista[5])
        print('-|-|-')
        print(self.lista[6] + '|' + self.lista[7] + '|' + self.lista[8])

    def marcar_posicao(self, i, jogador):
        self.lista[i] = jogador

jogo = Jogo()

for rodada in range(9):
    jogo.imprime_tabuleiro()

    i = input('\nEscreva um valor:')
    i = int(i) - 1

    if rodada % 2 == 0:
        jogo.marcar_posicao(i, 'O')
    else:
        jogo.marcar_posicao(i, 'X')


