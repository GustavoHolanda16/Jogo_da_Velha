import unittest

class TestJogoDaVelha(unittest.TestCase):
    def test_tabuleiro(self):
        # Teste para a função tabuleiro
        # Certifique-se de que a função não gera erros
        tabu = ['X', 'O', ' ', 'O', 'X', ' ', ' ', ' ', 'O']
        with self.assertRaises(Exception):
            tabuleiro()

    def test_make_move(self):
        # Teste para a função make_move
        # Certifique-se de que a função não gera erros
        jogador = 'X'
        with self.assertRaises(Exception):
            make_move(jogador)

    def test_make_move_computador(self):
        # Teste para a função make_move_computador
        # Certifique-se de que a função não gera erros
        with self.assertRaises(Exception):
            make_move_computador()

    def test_check_win(self):
        # Teste para a função check_win
        # Certifique-se de que a função retorna True para uma situação de vitória e False para uma situação não vitoriosa
        tabu_vitoria = ['X', 'X', 'X', 'O', 'O', ' ', ' ', ' ', ' ']
        tabu_nao_vitoria = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'X']
        self.assertTrue(check_win('X', tabu_vitoria))
        self.assertFalse(check_win('O', tabu_nao_vitoria))

    def test_game(self):
        # Teste para a função game
        # Certifique-se de que a função não gera erros
        with self.assertRaises(Exception):
            game()

if __name__ == '__main__':
    unittest.main()
