import Tile
import random
import os

class Board:
    def __init__(self, x_length, y_length, mines):
        self.x_length = x_length
        self.y_length = y_length
        self.mines = mines
        self.tiles = {}
        self.game_over = False
        self.remaining_tiles = (x_length * y_length) - mines
        self.message = ''

    def generate_board(self):
        for x in range(self.x_length):
            for y in range(self.y_length):
                tile = Tile.Tile(x, y)
                self.tiles[x,y] = tile
        self.plant_mines()

    def plant_mines(self):
        for mine in range(self.mines):
            mine_planted = False
            while mine_planted == False:
                random_tile = self.tiles[(random.randint(0, self.x_length - 1)), (random.randint(0, self.y_length - 1))]
                if random_tile.has_mine == False:
                    random_tile.has_mine = True
                    mine_planted = True

    def generate_tile_values(self):
        for tile in self.tiles.values():
            for x in range (-1,2):
                for y in range(-1,2):
                    if x == 0 and y == 0:
                        pass
                    elif (x + tile.x ,y + tile.y) in self.tiles and self.tiles[(x + tile.x,y + tile.y)].has_mine == True:
                        tile.adjacet_mines += 1

    def list_board(self):
        for tile in self.tiles.values():
            tile.print_tile()

    def print_board(self):
        column = []
        column.append('0')
        for x in range(self.x_length):
            column.append(str(x+1))
        print('')
        print(column)
        for y in range(self.y_length):
            row = []
            row.append(str(y+1))
            for x in range(self.x_length):
                row.append(self.tiles[(x,y)].print_tile())
            print(row)
        print(self.message)

    def pop_tile(self, x, y):
        tile = self.tiles[(x,y)]
        if tile.popped == True:
            return
        tile.popped = True
        self.remaining_tiles -= 1
        if tile.has_mine == True:
            self.message = "\n\nYou lose!!!"
            self.game_over = True
        if self.remaining_tiles == 0:
            self.message = "\n\nYou Win!!!"
            self.game_over = True
        elif tile.flagged == True:
            tile.flagged == False
        elif tile.adjacet_mines == 0:
            for x in range (-1,2):
                for y in range(-1,2):
                    if x == 0 and y == 0:
                        pass
                    elif (x + tile.x, y + tile.y) in self.tiles:
                        self.pop_tile(x + tile.x, y + tile.y)

    def flag_tile(self, x, y):
        tile = self.tiles[(x, y)]
        tile.flagged = True

game_in_progress = True
while game_in_progress == True:
    difficulty = input("CLI Sweeper\nBy Riley Mulvihill\nSelect Difficulty [1] Easy, [2] Medium, [3] Hard, [4] Custom\n")
    if int(difficulty) == 1:
        x = y = mines = 3
    elif int(difficulty) == 2:
        x = y = mines = 9
    elif int(difficulty) == 3:
        x = y = mines = 16
    elif int(difficulty) == 4:
        x = int(input("How many Columns?\n"))
        y = int(input("How many Rows?\n"))
        mines = int(input("How many Mines?\n"))
        if mines > x * y:
            self.messages = list("Too many mines\n")
    board = Board(x,y,mines)
    board.generate_board()
    board.list_board()
    board.generate_tile_values()
    os.system('cls')
    board.print_board()
    while board.game_over == False:
        x_coordinate = input("\nPick an x cord\n")
        y_coordinate = input("Pick an y cord\n")
        is_flagged = input("Enter 'f' to flag, any other key to pop\n")
        if is_flagged == 'f' or is_flagged == 'F':
            board.flag_tile(int(x_coordinate) - 1, int(y_coordinate) - 1)
        else:
            board.pop_tile(int(x_coordinate) - 1, int(y_coordinate) - 1)
        os.system('cls')
        board.print_board()
    play_again = input("\nAnother? y/n\n")
    if play_again == 'n':
        print("Thanks for playing")
        game_in_progress = False
        goodbye = input("Press any key to close")
