# in this class, we'll initialize a board and its pieces
# then we'll get as input what the players will be
# then, ok so i want the game to be played here versus the game starts in the chess file.
# lets figure out the difference. in chess.py, we have Play.play() called and that's it
# then play does everything.
# sure lol.

# ok so play does what?
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
#   