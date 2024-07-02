class Piece:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.directions = []
    
    def get_symbol(self):
        raise NotImplementedError()
    
    # This funtion will return all places the piece can travel on the board.
    # It will return a tuple holding two arrays: (moves, attack_moves)
    # I'm thinking I want Move to be a class with the coordinates to move to and the grammatical wording for the move.
    def get_moves(self, board):
        raise NotImplementedError()

    def update_position(self, row, col):
        self.row = row
        self.col = col

    def get_position(self):
        return (self.row, self.col)
    
    def get_color(self):
        return self.color

    # I think this should be a function outside of the Piece class because not all pieces should implement it.
    def get_moves_in_direction(self, board):
        moves = []
        attacks = []
        # Iterate over each possible direction.
        for (row,col) in self.directions:
            next_row = self.row + row
            next_col = self.col + col

            # Check if the spot in this direction is out of bounds.
            # Loop through all options in that direction until you get out of bounds.
            while (8 > next_row >= 0) & (8 > next_col >= 0):

                # Check if the spot in that direction has a piece on it.
                pieceAtNextSpot = board[next_row][next_row]
                if pieceAtNextSpot != None:
                    # Check if the spot in this directon has an opposing piece.
                    if pieceAtNextSpot.get_color() != self.color:
                        attacks.append( (next_row, next_col) )
                    # As we have encountered a piece in this direction, we are blocked and must check the next direction.
                    continue

                # Since the next spot in this direction is within bounds and has no piece occupying it, we could move here.
                moves.append( (next_row, next_col) )
                # Increment to the next spot in this direction.
                next_row = next_row + row
                next_col = next_col + col   
        return (moves, attacks)
    
    def __str__(self):
        return __class__.__name__

class King(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def get_moves(self, board):
        moves = []
        attacks = []
        # Go through each possible direction.
        for (row,col) in self.directions:
            # Check if moving to that direction is out of bounds.
            if (8 > self.row + row >= 0) & (8 > self.col + col >= 0):
                # Check if the spot in that direction has a piece on it.
                pieceAtNextSpot = board[self.row + row][self.col + col]
                if pieceAtNextSpot != None:
                    # Add it to possible attacks if it's another color.
                    if pieceAtNextSpot.get_color() != self.color:
                        attacks.append( (self.row + row,self.col + col ) )
                        continue
                # Add the next possible move to moves as there is no other piece occupying that space.
                moves.append( (self.row + row,self.col + col) )
        return (moves, attacks)
        
    def get_moves_in_direction(self, board):
        return []

    def get_symbol(self):
        return __class__.__name__[0] if self.color == 'white' else __class__.__name__[0].lower()
        

class Queen(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    def get_moves(self, board):
        return self.get_moves_in_direction(board)
    
    def get_symbol(self):
        return __class__.__name__[0] if self.color == 'white' else __class__.__name__[0].lower()

class Rook(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    def get_moves(self, board):
        return self.get_moves_in_direction(board)
    def get_symbol(self):
        return __class__.__name__[0] if self.color == 'white' else __class__.__name__[0].lower()

class Bishop(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    def get_moves(self, board):
        return self.get_moves_in_direction(board)
    def get_symbol(self):
        return __class__.__name__[0] if self.color == 'white' else __class__.__name__[0].lower()

class Knight(Piece):
    def __init__(self, color, row, col):
            super().__init__(color, row, col)
            self.directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    def get_moves(self, board):
        moves = []
        attacks = []
        # Go through each possible direction.
        for (row,col) in self.directions:
            # Check if moving to that direction is out of bounds.
            if (8 > self.row + row >= 0) & (8 > self.col + col >= 0):

                # Check if there is a piece already in that spot.
                pieceAtNextSpot = board[self.row + row][self.col + col]
                if pieceAtNextSpot != None:
                    # Add it to possible attacks if it's another color.
                    if pieceAtNextSpot.get_color() != self.color:
                        attacks.append( (self.row + row, self.col + col) )
                        continue

                moves.append( (self.row + row, self.col + col) )
        return (moves, attacks)
    def get_moves_in_direction(self, board):
        return []
    def get_symbol(self):
        return 'N' if self.color == 'white' else 'n'

class Pawn(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        direction = -1 if self.color == 'white' else 1
        # Directly forward
        self.directions.append((direction,  0))
        # Diagonally forward
        self.directions.append((direction,  1))
        self.directions.append((direction, -1))


    def get_moves(self, board):
        moves = []
        attacks = []

        # If the pawn is white and it's on row 6 then it is on its starting position and can move two spots.
        if self.color == 'white' & self.row == 6:
            moves.append( (self.row - 2, self.col) )
        # Similar for black.
        if self.color == 'black' & self.row == 1:
            moves.append( (self.row + 2, self.col))

        # Check if moving one step forward is out of bounds.
        # For now I'll keep it but due to promotion it can't go out of bounds.
        if 8 > (self.row + self.directions[0][0]) >= 0:
            # Check if the spot in that direction is unoccupied.
            if board[self.row + self.directions[0][0] ][self.col] == None:
                moves.append( (self.row + self.directions[0][0], self.col) )
            # Check if stepping diagonally is out of bounds for either direction.
            if 8 > self.col + 1:
                # Check if the spot diagonally forward is occupied by an enemy piece.
                if board[ self.row + self.directions[1][0] ][ self.col + self.directions[1][1] ] != None:
                    attacks.append( (self.row + self.directions[1][0], self.col + self.directions[1][1]) )
            if self.col - 1 < 0:
                if board[ self.row + self.directions[2][0] ][ self.col + self.directions[2][1] ] != None:
                     attacks.append( (self.row + self.directions[2][0], self.col + self.directions[2][1]) )

        # i'll figure out en passent later

        return (moves, attacks)
    
    def promotion(self):
        raise NotImplementedError

    def get_moves_in_direction(self, board):
        return []

    def get_symbol(self):
        return __class__.__name__[0] if self.color == 'white' else __class__.__name__[0].lower()