#pseudocode 
"""
two players: computer and human player



computer will have x and human will o 

we need a board 3*3 board drawn separated by lines

there is checking whose move we at , 
check if a square is a avaialble 
how to win 
how to continue
"""
class player:
    def __init__(self, letter) -> None:
        self.letter=letter
    def get_moves(self, game):
        pass
#used inheritance in these classes player
class randomcomputer(player):
    def __init__(self, letter) -> None:
        super().__init__(letter)
    def get_moves(self, game):
        pass
class human(player):
    def __init__(self, letter) -> None:
        super().__init__(letter)
    def get_moves(self, game):
        pass