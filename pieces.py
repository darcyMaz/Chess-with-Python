class Piece:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.directions = []
    
    def get_symbol(self):
        raise NotImplementedError()
    
    # This funtion will return all places the piece can travel on an empty board.
    # CAREFUL: This function cannot access the actual board so it will likely 
    #          return moves that aren't viable due to pieces blocking it.
    def get_moves(self):
        raise NotImplementedError()

    def update_position(self, row, col):
        self.row = row
        self.col = col

    def get_moves_in_direction(self):
        moves = []
        # Iterate over each possible direction.
        for (row,col) in self.directions:
            current_row = self.row + row
            current_col = self.col + col
            # Check if that direction is out of bounds.
            # Check if all options in that direction are out of bounds.
            while (8 > current_row >= 0) & (8 > current_col >= 0):
                moves.append( (current_row, current_col) )
                current_row = current_row + row
                current_col = current_col + col
        return moves

class King(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def get_moves(self):
        moves = []
        # Go through each possible direction.
        for (row,col) in self.directions:
            # Check if moving to that direction is out of bounds.
            if (8 > self.row + row >= 0) & (8 > self.col + col >= 0):
                moves.append( (self.row + row,self.col + col) )
        return moves
        
    def get_symbol(self):
        return __class__.__name__[0] if self.color == 'white' else __class__.__name__[0].lower()

class Queen(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    def get_moves(self):
        return self.get_moves_in_direction()
    
    def get_symbol(self):
        return __class__.__name__[0] if self.color == 'white' else __class__.__name__[0].lower()

class Rook(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    def get_moves(self):
        return self.get_moves_in_direction()
    def get_symbol(self):
        return __class__.__name__[0] if self.color == 'white' else __class__.__name__[0].lower()

class Bishop(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    def get_moves(self):
        return self.get_moves_in_direction()
    def get_symbol(self):
        return __class__.__name__[0] if self.color == 'white' else __class__.__name__[0].lower()

class Knight(Piece):
    def __init__(self, color, row, col):
            super().__init__(color, row, col)
            self.directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    def get_moves(self):
        moves = []
        # Go through each possible direction.
        for (row,col) in self.directions:
            # Check if moving to that direction is out of bounds.
            if (8 > self.row + row >= 0) & (8 > self.col + col >= 0):
                moves.append( (row,col) )
        return moves
    def get_symbol(self):
        return 'N' if self.color == 'white' else 'n'

class Pawn(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        direction = -1 if self.color == 'white' else 1
        # Directly forward
        self.directions.append((direction,  0))
        # Diagonally forward
        self.directions.append((direction, -1))
        self.directions.append((direction,  1))


    def get_moves(self):
        moves = []
        for (row,col) in self.directions:
            # Check if moving to that direction is out of bounds.
            if (8 > self.row + row >= 0) & (8 > self.col + col >= 0):
                moves.append( (self.row + row,self.col + col) )
        return moves
    
    def get_symbol(self):
        return __class__.__name__[0] if self.color == 'white' else __class__.__name__[0].lower()