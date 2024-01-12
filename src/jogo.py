import random
import os

tabu = [' ' for _ in range(9)]
ranking = []

class MeuObjeto:
    def __init__(self, nome, vitorias, derrotas, empates):
        self.nome = nome
        self.vitorias = vitorias
        self.derrotas = derrotas
        self.empates = empates
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

def test_fazer_jogada(jogador):
    while True:
        move = int(input(f"Vez do jogador {jogador}, escolha uma posição (0-8): "))
        if 0 <= move <= 8 and tabu[move] == ' ':
            tabu[move] = jogador
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
    while True:
        limpar_tela()
        tabuleiro()
        test_fazer_jogada('X')
        if verificar_vitoria('X'):
            tabuleiro()
            print("Jogador X venceu!")
            return
        if not vazio():
            return
        limpar_tela()
        tabuleiro()
        test_fazer_jogada('O')
        if verificar_vitoria('O'):
            tabuleiro()
            print("Jogador O venceu!")
            return
        if not vazio():
            return

def gameCom():
    while True:
        limpar_tela()
        tabuleiro()
        test_fazer_jogada('X')
        if verificar_vitoria('X'):
            tabuleiro()
            print("Jogador X venceu!")
            return
        if not vazio():
            return
        limpar_tela()
        tabuleiro()
        jogada_computador()
        if verificar_vitoria('O'):
            limpar_tela()
            tabuleiro()
            print("Jogador O (computador) venceu!")
            return
        if not vazio():
            return

def menu_principal():
    print('Escolha uma das opções...')
    print('1 -- Para Jogar contra outro jogador')
    print('2 -- Para Jogar contra o PC')
    print('3 -- Para ver Ranking')
    print('4 -- Para sair')
    x = input(': ')

    if x == '1':
        game()
    elif x == '2':
        gameCom()

menu_principal()








