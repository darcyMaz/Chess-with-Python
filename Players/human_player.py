import player as Player
import board as Board  # can this file find this since it's not in the same folder?

class Human_Player(Player.Player):
    def __init__(self, playerNum, color):
        super().__init__(playerNum, color)
    
    def move(self, board_input: Board.Board):
        
        board = board_input.copy_board()

        piece_dict = {}
        stalemate_bool = False
        for row in board:
            for col in row:
                current_piece = board[row][col]
                if current_piece.get_color() == self.color:
                    current_moves = current_piece.get_moves()
                    piece_dict.append( (row,col), current_moves )
                    if len(current_moves[0]) + len(current_moves[1]) != 0 and not stalemate_bool:
                        stalemate_bool = True

        print(f"It is Player {self.playerNum}'s turn. As a human player they must choose a move.")

        if stalemate_bool:
            print(f"There are no moves left for {self.playerNum} to play. A stalemate has been reached.")

        print(f"Player {self.playerNum} is playing with the {self.color} pieces.")
        print(f"Please choose a coordinate with a {self.color} piece on it. Its possible moves will be listed out.")
        # reminder that white pieces are capitalized
        print('Please enter the coordinate of the piece you want to move (Format: A1).')

        while True:
            coord = input("Type coordinates (Format: A1): ")
            if len(coord) != 2:
                print("The format of the input is incorrect: The length must be 2.")
                continue

            letter = coord[0]
            number = coord[1]
            
            number_int = -1

            try:
                number_int = int(number)
            except ValueError:
                print('The format of the input is incorrect: The second character is not a number.')
                continue

            piece = board_input.get_piece_at_coord(number_int, letter)

            if piece == None:
                print('The coordinate you have chosen has no piece on it. Please choose another coordinate.')
                continue
            if piece.get_color() != self.color:
                print('This piece is the wrong color. Please choose another coordinate.')
                continue

            print(f"This piece is a {piece.str()}.")
            moves_and_attacks = piece_dict.get( piece.get_position() )
            moves = moves_and_attacks[0]
            attacks = moves_and_attacks[1]

            if len(moves) + len(attacks) == 0:
                print('This piece has no available moves. Please choose another coordinate.')
                continue

            move_index = 0
            for move in moves:
                (letter_, number_) = Board.Board.translate_coords_num_to_chess(move[0], move[1])
                print(f'{move_index}: Move to {letter_}{number_}.')
                move_index += 1
            for attack in attacks:
                (letter_, number_) = Board.Board.translate_coords_num_to_chess(attack[0], attack[1])
                piece_to_capture = board[ attack[0] ][ attack[1] ]
                print(f'{move_index}: Capture {piece_to_capture.__str__()} on {letter_}{number_}.')
                move_index += 1

            while True:
                move_input = input("Please choose a move by typing its number and pressing enter (type 'q' to select a different piece): ")
                try:
                    if move_input == 'q':
                        break
                    move_input_int = int(move_input)
                    if 0 > move_input_int > (len(moves) + len(attacks) - 1):
                        print("The format of the input is incorrect: The number is out of bounds, try again.")
                        continue
                    if move_input_int > len(moves) - 1:
                        # this means that we're going to choose a capture.
                        attack_index = move_input_int - len(moves)
                        board.move_piece(  piece, attacks[attack_index][0], attacks[attack_index][1] )
                        return
                    # this means that we're not choosing a capture, instead a normal move.
                    board.move_piece(  piece, moves[move_input_int][0], attacks[move_input_int][1] )
                    return
                except ValueError:
                    print('The format of the input is incorrect: It should be a number.')
                







