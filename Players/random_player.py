import ai_player as AI
import random

class Random_Player(AI.AI_Player):
    def __init__(self, playerNum, color):
        super().__init__(playerNum, color)

    def move(self, board_input):

        board = board_input.copy_board()

        # Make a list of all of this player's pieces.
        piece_list = []
        for row in board:
            for col in row:
                if board[row][col].get_color() == self.color:
                    piece_list.append(board[row][col])

        # Grab a piece at random and then choose one of its moves at random.
        # If no moves (or pieces) exist then a stalemate is returned.
        try:

            while True:

                # Grab a piece at random and remove it from the list
                # Check if it has any moves or attacks
                # Put them all in a list and grab one at random
                # If there are no moves or attacks loop to the next random piece.
                rand_index = random.randint(0, len(piece_list))
                piece = piece_list.pop(rand_index)

                moves_and_attacks = piece.get_moves(board)
                moves = moves_and_attacks[0]
                attacks = moves_and_attacks[1]
                
                rand_index = random.randint(0, len(moves) + len(attacks) - 1)

                if rand_index >= len(moves):
                    chosen_move = attacks[rand_index - len(moves)]
                chosen_move = moves[rand_index]

                board.move_piece(piece, chosen_move[0], chosen_move[1])

        except IndexError:
            print(f"There are no moves left for {self.playerNum} to play. A stalemate has been reached.")