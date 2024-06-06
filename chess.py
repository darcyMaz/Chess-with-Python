import pieces as Piece
import board as Board

def main():
    # Should make the board 'private' i.e. in the board file only.
    # Static fields in python?



    board = Board.Board()
    board.print_board()
    temp_board = board.temp_get_board()

    for row in temp_board:
       for _ in row:
        if isinstance(_, Piece.Pawn): 
            print(_.get_symbol())
            for __ in _.get_moves(temp_board):
                print(__)        
    


if __name__ == "__main__":
    main()


#I want three things: (1) The game itself flowing (2) An endgame (3) Decision making for pieces (start with random)
# Check if king and queen are in the right place later.
