import pieces as Piece

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces('white', 7, 6)
        self.setup_pieces('black', 0, 1)
    
    def get_coord(self, number, letter):
        letter = letter.upper()
        letter_int = ord(letter) - 65
        if 0 > letter_int > 7:
            print('The letter input is out of bounds.')
            return IndexError()
        number = number - 1
        if 0 > number > 7:
            print('The number input is out of bounds.')
            return IndexError()
        
        return self.board[7 - number][letter_int]
        
        # 7=0; 6=1; 5=2; 4=3; 3=4; 2=5; 1=6; 0=7;
        # A = 65 = 0; B = 66 = 1; C = 67 = 2; ...

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

    class Temp:
        def __init__(self):
            self.temp = 1

    def temp_get_board(self):
        return self.board


