import player

class AI_Player(player.Player):
    def __init__(self, playerNum, color):
        super().__init__(playerNum, color)

    def move(self, board_input):
        raise NotImplementedError