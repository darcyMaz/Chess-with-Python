import pieces as Piece
import board as Board
from Players import human_player as Human
from Players import random_player as Rando

# chess.py will have one call: Play.play().
# Every else happens here or within other objects created here.


def play():

    board = Board.Board()

    # There should be a dialogue here instead of automatic assignment.
    player1 = Human.Human_Player(1, 'white')
    player2 = Rando.Random_Player(2, 'black')

    # So i need to make a while loop where each loop is a back and forth between players.
    # The end of each loop must look at some returned number. 0 for normal 1 for stalemate 2 for checkmate
    # obvs i need to make a checkmate check, that needs 
        #  (1) king has a function which looks at whether any other pieces attack it and 
        #  (2) if king can't move checkmate; ...

    # If the king is in check and the checked player has no legal move to get out of check, the king is checkmated and the player loses

    while True:
        input_ = input("Turn starts:")
        break

    return 0


# initialize the board
# assign players
#   is player 1 human or AI?
#       which AI is player 1?
#   is player 2 human or AI?
#       which AI is player 2?
#   is player 1 white or black or random?
# on each turn
#   print the board
#       call playerX.move()
#           human_player class implements move() with a question to the terminal on how to play
#           AI_player class implements move() with an AI algorithm answer. I'll make random and maybe one or two others
#           move is sent to the board which checks if it's a valid move and rejects it if it isn't
#   is_check_mate() (function in the board class)
#       checks if there's a check or checkmate
#       i can look up how to implement this maybe idk. doable but tough and time consuming idk
#       return 0 for check mate, 1 for stalemate, 2 for check, 3 for nothing
#       if check_mate or stalemate end the game with 0 or 1 respectively
#       if check, somehow save all the vectors of attack and make sure next move removes all vectors of attack?
#           gonna have to think about this one
#       else do nothing else
#

# Tasks:
#   - Pass the board copy into the Piece.get_moves(board_copy) and narrow down the possible moves for each piece.
#   - Figure out a project wide coordinate system. Ideally it would be Letter, Number which translates to row (number), col (letter) in Board.
#   - Play.play()
#       - Assign players dialogue
#       - Each turn while loop
#   - Player super class
#   - Human_player(Player)
#   - AI_player(Player)  <- can we make this an abstract class? Doesn't have to be cus you choose AI type with dialogue
#   - Random_Player(AI_Player)
#   - is_check_mate()