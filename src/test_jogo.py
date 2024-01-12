import unittest

def verificar_vitoria(jogador, tabu):
    vitoria = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for cond in vitoria:
        if tabu[cond[0]] == tabu[cond[1]] == tabu[cond[2]] == jogador:
            return True
    return False

def check_empate(tabu):
    return ' ' not in tabu

class TestJogoDaVelha(unittest.TestCase):

    def test_verificar_vitoria_X(self):
        tabu_teste = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(verificar_vitoria('X', tabu_teste))

        tabu_teste = ['O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertFalse(verificar_vitoria('X', tabu_teste))

    def test_verificar_vitoria_O(self):
        tabu_teste = ['O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(verificar_vitoria('O', tabu_teste))

        tabu_teste = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertFalse(verificar_vitoria('O', tabu_teste))

    def test_verificar_empate(self):
        tabu_teste_empate = ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X', 'O']
        self.assertTrue(check_empate(tabu_teste_empate))

        tabu_teste_nao_empate = ['X', 'O', 'X', 'O', 'X', ' ', 'O', 'X', 'O']
        self.assertFalse(check_empate(tabu_teste_nao_empate))

        tabu_teste_empate_vazio = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertFalse(check_empate(tabu_teste_empate_vazio))

if __name__ == '__main__':
    unittest.main()
