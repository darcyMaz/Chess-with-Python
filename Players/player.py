class Player:
    def __init__(self, playerNum, color):
        self.playerNum = playerNum
        self.color = color

    def move(self, board_input):
        raise NotImplementedError