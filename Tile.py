class Tile:
    """ Tile on the board"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.popped = False
        self.flagged = False
        self.has_mine = False
        self.adjacet_mines = 0

    def list_tile(self):
        print("X:" + str(self.x) + " Y:" + str(self.y) + " Mine:" + str(self.has_mine))

    def print_tile(self):
        if self.popped == True:
            if self.has_mine == True:
                return "X"
            elif self.flagged == True:
                return "!"
            else:
                return str(self.adjacet_mines)

        else:
            return '_'


