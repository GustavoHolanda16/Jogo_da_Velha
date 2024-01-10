import random

tabu = [' ' for _ in range(9)]
print('boa noite')
def tabuleiro():
    print(f" {tabu[0]} | {tabu[1]} | {tabu[2]} ")
    print("---+---+---")
    print(f" {tabu[3]} | {tabu[4]} | {tabu[5]} ")
    print("---+---+---")
    print(f" {tabu[6]} | {tabu[7]} | {tabu[8]} ")
def vazio():
    for i in range(9):
        if tabu[i]==' ':
            True
        else:
            print('tente de novo!')
def make_move(jogador):
    if jogador == 'X':
        move = int(input("Vez do jogador X, escolha uma posição (0-8): "))
    else:
        move = int(input("Vez do jogador O, escolha uma posição (0-8): "))
    tabu[move] = jogador

def make_move_computador():
    print("Vez do jogador O (computador):")

    
    for i in range(9):
        if tabu[i] == ' ':
            tabu[i] = 'O'
            if check_win('O'):
                return
            tabu[i] = ' '

    for i in range(9):
        if tabu[i] == ' ':
            tabu[i] = 'X'
            if check_win('X'):
                tabu[i] = 'O'
                return
            tabu[i] = ' '

    move = random.choice([i for i, val in enumerate(tabu) if val == ' '])
    tabu[move] = 'O'

def check_win(jogador):
    vitoria = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for cond in vitoria:
        if tabu[cond[0]] == tabu[cond[1]] == tabu[cond[2]] == jogador:
            return True
    return False
def check_empate():
    return ' ' not in tabu
def game():

    tabuleiro()

    while True:
        for jogador in ["X", "O"]:
            make_move(jogador)
            tabuleiro()
            vazio()
            if check_win(jogador):
                print("Jogador", jogador, "venceu!")
                return 

def gameCom():
    tabuleiro()

    while True:
        make_move('X')
        tabuleiro()
        if check_win('X'):
            print("Jogador X venceu!")
            return
        if check_empate():
            print("O jogo empatou!")
            return

        make_move_computador()
        tabuleiro()
        if check_win('O'):
            print("Jogador O (computador) venceu!")
            return 
        if check_empate():
            print("O jogo empatou!")
            return

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
