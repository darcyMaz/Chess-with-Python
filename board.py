import pieces as Piece
import copy

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces('white', 7, 6)
        self.setup_pieces('black', 0, 1)

        # i think later I'll have two variables, one for each player.
        # a player class and a human_player and AI_player class where AI_player can be implemented by subclasses.
    
    def translate_coords_num_to_chess(row: int, col: int):
        number = 8 - row
        if 7 < number < 0:
            print("Coordinate translation failed. Row input out of bounds.")
            return ValueError
        if 7 < col < 0:
            print("Coordinate translation failed. Column input out of bound")
        # A = 65 = 0; B = 66 = 1; C = 67 = 2; ...
        letter = chr(col + 65)
        return (number, letter)

    def translate_coords_chess_to_num(number: int, letter: str):
        if len(letter) != 1:
            print('The letter input of this function must be of length 1.')
            return ValueError()
        letter = letter.upper()
        letter_int = ord(letter) - 65
        if 0 > letter_int > 7:
            print('The letter input is out of bounds.')
            return ValueError()
        number = number - 1
        if 0 > number > 7:
            print('The number input is out of bounds.')
            return ValueError()
        return (7-number, letter_int)
        
        # 7=0; 6=1; 5=2; 4=3; 3=4; 2=5; 1=6; 0=7;
        # A = 65 = 0; B = 66 = 1; C = 67 = 2; ...
    
    def get_piece_at_coord(self, row: int, col: int):
        return self.board[row][col]

    def get_piece_at_coord(self, number: int, letter: str):
        (row, col) = Board.translate_coords_chess_to_num(number, letter)
        return Board.get_piece_at_coord(row, col)

    def print_board(self):
        print('. A B C D E F G H')
        i = 8
        for row in self.board:
            print(i,'', end='')
            i = i-1
            print(' '.join([piece.get_symbol() if piece else '.' for piece in row]))

    def setup_pieces(self, color, back_row, pawn_row):
        pieces = [Piece.Rook, Piece.Knight, Piece.Bishop, Piece.Queen, Piece.King, Piece.Bishop, Piece.Knight, Piece.Rook]
        for col, PieceClass in enumerate(pieces):
            self.board[back_row][col] = PieceClass(color, back_row, col)
        for col in range(8):
            self.board[pawn_row][col] = Piece.Pawn(color, pawn_row, col)

    # def temp_get_board(self):
    #    return self.board
    
    def copy_board(self):
        return copy.deepcopy(self.board)
    
    def move_piece(self, piece, letter: str, number: int):
        (row, col) = Board.translate_coords_chess_to_num(letter, number)
        self.move_piece(piece, row, col)

    # Validity of move is checked before this function.
    def move_piece(self, piece, row: int, col: int):
        (curr_row, curr_col) = piece.get_position()
        
        # Special case: when the King castles.
        if isinstance(piece, Piece.King) & curr_col == 4:
            row_color = 7 if piece.get_color() == 'white' else 0
            # If the column we are moving to is either 6 or 4 (G or C) then we are castling.
            # If we are castling we also need to move the rook.

            # Short-side
            if col==6:
                rook = self.get_piece_at_coord(row_color, 7)
                self.board[row_color][0] = None
                piece.update_position(row_color, 5)
                self.board[row_color][5] = rook
            # Long-side
            if col==2:
                rook = self.get_piece_at_coord(row_color, 0)
                self.board[row_color][0] = None
                piece.update_position(row_color, 3)
                self.board[row_color][3] = rook
            
        self.board[curr_row][curr_col] = None
        piece.update_position(row,col)
        self.board[row][col] = piece
