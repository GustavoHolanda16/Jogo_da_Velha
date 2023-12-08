tabu = [' ' for _ in range(9)]

def tabuleiro():
    row = ""
    for i in range(len(tabu)):
        if i % 3 == 0 and i != 0:
            print(row)
            row = ""
        row += tabu[i]
    print(row)

def make_move(jogador):
    move = int(input("Vez do jogador " + jogador + ", escolha uma posição (0-8): "))
    tabu[move] = jogador

def check_win(jogador):
    vitoria = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for cond in vitoria:
        if tabu[cond[0]] == tabu[cond[1]] == tabu[cond[2]] == jogador:
            return True
    return False

def game():
    tabuleiro()
    while True:
        for jogador in ["X", "O"]:
            make_move(jogador)
            tabuleiro()
            if check_win(jogador):
                print("Jogador", jogador, "venceu!")
                return

game()
