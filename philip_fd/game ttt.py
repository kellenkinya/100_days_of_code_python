class gama:
    def __init__(self) -> None:
        self.board= [' ' for _ in range(9)]
        self.current_winner= None # keep record of who is the winner an who is it

    def print_board(self):
        for row in [self.board[i*3(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row)+'|')
