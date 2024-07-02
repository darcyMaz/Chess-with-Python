import play

def main():
    # Should make the board 'private' i.e. in the board file only.
    # Static fields in python?


    # I'm thinking Board should be a black box and it can return Board_instance which has a copy of the board arrays
    # and the ability to print it among a few other functionalities.
    play.play()



    #board.print_board()
    # copy_board = board.copy_board()
    # temp_board = board.temp_get_board()

    #for row in temp_board:
    #   for _ in row:
    #    if isinstance(_, Piece.Bishop): 
    #        print(_.get_symbol())
    #        for __ in _.get_moves():
    #            print(__)        


if __name__ == "__main__":
    main()


#I want three things: (1) The game itself flowing (2) An endgame (3) Decision making for pieces (start with random)
