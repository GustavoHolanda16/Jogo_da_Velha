import random
import os

tipo = ''
cont = True
tabu = [' ' for _ in range(9)]
ranking = []

def tabela_ranking():
    limpar_tela()
    ranking_ordenado = sorted(ranking, key=lambda x: x.vitorias, reverse=True)
    print("\n{:<15} {:<10} {:<10} {:<10}".format("Nome", "Vitórias", "Derrotas", "Empates"))
    print("-" * 45)
    for jogador in ranking_ordenado:
        print("{:<15} {:<10} {:<10} {:<10}".format(
            jogador.nome, jogador.vitorias, jogador.derrotas, jogador.empates
        ))

class Jogador:
    def __init__(self, nome):
        self.tipo = tipo
        self.nome = nome
        self.vitorias = 0
        self.derrotas = 0
        self.empates = 0

    def vitoria(self):
        self.vitorias += 1

    def derrota(self):
        self.derrotas += 1

    def empate(self):
        self.empates += 1

def verificar_jogador(nome):
    for jogador in ranking:
        if jogador.nome == nome:
            return jogador

    novo_jogador = Jogador(nome)
    if tipo == "X":
        novo_jogador.tipo = "X"
    elif tipo == "O":
        novo_jogador.tipo = "O"

    ranking.append(novo_jogador)
    return novo_jogador

def tabuleiro():
    print(f" {tabu[0]} | {tabu[1]} | {tabu[2]} ")
    print("---+---+---")
    print(f" {tabu[3]} | {tabu[4]} | {tabu[5]} ")
    print("---+---+---")
    print(f" {tabu[6]} | {tabu[7]} | {tabu[8]} ")

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def vazio():
    if ' ' in tabu:
        return True
    print('O jogo empatou!')
    return False

def test_fazer_jogadaX(jogador):
    while True:
        move = int(input(f"Vez do jogador {jogador.nome}, escolha uma posição (0-8): "))
        if 0 <= move <= 8 and tabu[move] == ' ':
            tabu[move] = 'X'
            break
        else:
            print("Posição inválida ou já preenchida. Tente novamente.")

def test_fazer_jogadaO(jogador):
    while True:
        move = int(input(f"Vez do jogador {jogador.nome}, escolha uma posição (0-8): "))
        if 0 <= move <= 8 and tabu[move] == ' ':
            tabu[move] = 'O'
            break
        else:
            print("Posição inválida ou já preenchida. Tente novamente.")

def jogada_computador():
    print("Vez do jogador O (computador):")

    for i in range(9):
        if tabu[i] == ' ':
            tabu[i] = 'O'
            if verificar_vitoria('O'):
                return
            tabu[i] = ' '

    for i in range(9):
        if tabu[i] == ' ':
            tabu[i] = 'X'
            if verificar_vitoria('X'):
                tabu[i] = 'O'
                return
            tabu[i] = ' '

    move = random.choice([i for i, val in enumerate(tabu) if val == ' '])
    tabu[move] = 'O'

def verificar_vitoria(jogador):
    vitoria = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for cond in vitoria:
        if tabu[cond[0]] == tabu[cond[1]] == tabu[cond[2]] == jogador:
            return True
    return False

def check_empate():
    return ' ' not in tabu

def game():
    global tabu
    tabu = [' ' for _ in range(9)]
    nome1 = input('Digite o nome do jogador X:')
    jogador1 = verificar_jogador(nome1)
    nome2 = input('Digite o nome do jogador O:')
    jogador2 = verificar_jogador(nome2)

    while True:
        limpar_tela()
        tabuleiro()
        test_fazer_jogadaX(jogador1)
        if verificar_vitoria('X'):
            tabuleiro()
            jogador1.vitoria()
            jogador2.derrota()
            print(f"Jogador {jogador1.nome} venceu!")
            break
        if not vazio():
            jogador1.empate()
            jogador2.empate()
            break
        limpar_tela()
        tabuleiro()
        test_fazer_jogadaO(jogador2)
        if verificar_vitoria('O'):
            tabuleiro()
            jogador2.vitoria()
            jogador1.derrota()
            print(f"Jogador {jogador2.nome} venceu!")
            break
        if not vazio():
            jogador1.empate()
            jogador2.empate()
            break

def gameCom():
    global tabu
    tabu = [' ' for _ in range(9)]
    nome1 = input('Digite o nome do jogador X:')
    jogador1 = verificar_jogador(nome1)
    nome2 = 'PC'
    jogador2 = verificar_jogador(nome2)
    while True:
        limpar_tela()
        tabuleiro()
        test_fazer_jogadaX(jogador1)
        if verificar_vitoria('X'):
            tabuleiro()
            jogador1.vitoria()
            jogador2.derrota()
            print(f"Jogador {jogador1.nome} venceu!")
            break
        if not vazio():
            jogador1.empate()
            jogador2.empate()
            break
        limpar_tela()
        tabuleiro()
        jogada_computador()
        if verificar_vitoria('O'):
            tabuleiro()
            jogador2.vitoria()
            jogador1.derrota()
            print(f"Jogador {jogador2.nome} venceu!")
            break
        if not vazio():
            jogador1.empate()
            jogador2.empate()
            break

def menu_principal():
    print('Escolha uma das opções...')
    print('1 -- Para Jogar contra outro jogador')
    print('2 -- Para Jogar contra o PC')
    print('3 -- Para ver Ranking')
    print('4 -- Para sair')
    x = input('Digite sua opção: ')

    if x == '1':
        limpar_tela()
        game()
    elif x == '2':
        limpar_tela()
        gameCom()
    elif x == '3':
        limpar_tela()
        tabela_ranking()
    elif x == '4':
        exit()

while cont:
    menu_principal()
