import pieces as Piece
import board as Board

def main():
    # Should make the board 'private' i.e. in the board file only.
    # Static fields in python?



    board = Board.Board()
    copy_board = board.copy_board()
    temp_board = board.temp_get_board()

    #for row in temp_board:
    #   for _ in row:
    #    if isinstance(_, Piece.Bishop): 
    #        print(_.get_symbol())
    #        for __ in _.get_moves():
    #            print(__)        
    
    # next i want to integrate the board and its pieces into the move choices
    # a few ways to do this
    # don't change the pieces file anymore. return the possible moves and show it to the board.
    # i don't really like that because it's kind of doubling up the look at the board
    # pass the board into the pieces file... i dont like that either i dont want to
    #   actually no the board should be a public thing tbh. not changing it but seeing it
    #   i should make a function that returns a copy of the board.

    # ok so i will pass the board copy into the pieces get_moves function
    # 


if __name__ == "__main__":
    main()


#I want three things: (1) The game itself flowing (2) An endgame (3) Decision making for pieces (start with random)
# Check if king and queen are in the right place later.
