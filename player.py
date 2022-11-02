import math
import random
import game
class Player:
    def __init__(self,letter):
        #letter is X or O
        self.letter=letter

    #we want all player to get there next move
    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        square=random.choice(game.available_moves())

class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self,game):
        valid_square=False
        val=None
        while not valid_square:
            square=input(self.letter + '\'s turn. Input move (0,9')

            try:
                val=int(square)
                if val not in game.available_moves():
                    raise ValueError
            except ValueError:
                print('Invalid square, try again.')
        return val        







