import player as Player
import board as Board  # can this file find this since it's not in the same folder?

class Human_Player(Player.Player):
    def __init__(self, playerNum, color):
        super().__init__(playerNum, color)
    
    # I think the actual board should be passed into the players instead of the copy board.
    # This will allow either player to edit the board from within the class.
    def move(self, board_input: Board.Board):
        # Should the while loop be here or outside the move func... idk.
        
        board = board_input.copy_board()

        print(f"It is Player {self.playerNum}'s turn. As a human player they must choose a move.")
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

            piece = Board.Board.get_piece_at_coord(board, number_int, letter)

            print(f"This piece is a {piece.str()}.")
            moves_and_attacks = piece.get_moves(board)
            moves = moves_and_attacks[0]
            attacks = moves_and_attacks[1]

            move_index = 0
            # The 'move' is a set of coords (row, col) which I need to translate and then print on a line.
            # In the future I will standardize the coord system and print out the chess grammar as well.
            for move in moves:
                (letter_, number_) = Board.Board.translate_coords_num_to_chess(move[0], move[1])
                print(f'{move_index}: Move to {letter_}{number_}.')
                move_index += 1
            for attack in attacks:
                (letter_, number_) = Board.Board.translate_coords_num_to_chess(attack[0], attack[1])
                piece_to_capture = board[ attack[0] ][ attack[1] ]
                print(f'{move_index}: Capture {piece_to_capture.__str__()} on {letter_}{number_}.')
                move_index = move_index + 1
                # ok after this i want to accept an input, check if it's a number
                # then choose one of the options
                # if input > moves - 1 then input = moves.length

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
                        # this means that we're going to choose an attack.
                        attack_index = move_input_int - len(moves)
                        # SEND MESSAGE TO BOARD TO CHANGE IT!!!
                        break
                    # SEND MESSAGE TO BOARD TO CHANGE IT!!!
                    # move_index = move_input_int. 
                except ValueError:
                    print('The format of the input is incorrect: It should be a number.')
                







