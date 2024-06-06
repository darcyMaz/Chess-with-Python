class Piece:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
    
    def get_symbol(self):
        raise NotImplementedError()
    
    def get_directions(self):
        raise NotImplementedError()

    def update_position(self, row, col):
        self.row = row
        self.col = col

class King(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def get_directions(self):
        return self.directions
        # i know the dimensions and the position, i can narrow it down from there
        # make a function that can take all possible options and narrow them down based on those two factors

    def get_symbol(self):
        return __class__.__name__[0] if self.color == 'white' else __class__.__name__[0].lower()

class Queen(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    def get_moves(self):
        moves = []
        for (row,col) in self.directions:
            current_row = self.row + row
            current_col = self.col + col
            while (8 > current_row >= 0) & (8 > current_col >= 0):
                print()

        return self.directions
    
    def get_symbol(self):
        return __class__.__name__[0] if self.color == 'white' else __class__.__name__[0].lower()

class Rook(Piece):
    def get_moves(self, board, row, col):
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        return self._get_moves_in_directions(board, row, col, directions, 8)
    def get_symbol(self):
        return __class__.__name__[0] if self.color == 'white' else __class__.__name__[0].lower()

class Bishop(Piece):
    def get_moves(self, board, row, col):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        return self._get_moves_in_directions(board, row, col, directions, 8)
    def get_symbol(self):
        return __class__.__name__[0] if self.color == 'white' else __class__.__name__[0].lower()

class Knight(Piece):
    def get_directions(self):
        #moves = []
        directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        #for d in directions:
            #new_row, new_col = row + d[0], col + d[1]
            #if 0 <= new_row < 8 and 0 <= new_col < 8 and (board[new_row][new_col] is None or board[new_row][new_col].color != self.color):
                #moves.append((new_row, new_col))
        #return moves
        return directions
    def get_symbol(self):
        return 'N' if self.color == 'white' else 'n'

class Pawn(Piece):
    def get_moves(self, board):
        moves = []
        direction = -1 if self.color == 'white' else 1
        start_row = 6 if self.color == 'white' else 1
        if board[self.row + direction][self.col] is None:
            moves.append((self.row + direction, self.col))
            if self.row == start_row and board[self.row + 2 * direction][self.col] is None:
                moves.append((self.row + 2 * direction, self.col))
        for dcol in [-1, 1]:
            new_row, new_col = self.row + direction, self.col + dcol
            if 0 <= new_col < 8 and board[new_row][new_col] is not None and board[new_row][new_col].color != self.color:
                moves.append((new_row, new_col))
        return moves
    def get_symbol(self):
        return __class__.__name__[0] if self.color == 'white' else __class__.__name__[0].lower()