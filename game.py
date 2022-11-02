import player
import game


class TicTacToe:

    def __init__(self):
        self.board=[' ' for _ in range(9)] #single list to represent 3x3 board
        self.current_winner=None #keep track of winner
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| | ".join(row))

    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc tells what number corresponds to what box
        number_board=[str(i) for i in range(j*3, (j+1)*3) for j in range(3)]
        for row in number_board:
            print('| |'.join(row))
    
    def available_moves(self):
        
        moves=[]
        for (i,spot) in enumerate(self.board):
            #[x, x, 0]----->[(0 ,x), (1, x), (2, 0)]
            if spot==' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square,letter):
        if self.board[square]==' ':
            self.board[square]=letter
            if self.winner(square,letter):
                self.current_winner=letter
            return True
        return False
    def winner(self, square,letter):
        #lets check the row
        row_index=square//3
        row=self.board[row_index*3:(row_index+1)*3]
        if all([spot == letter for spot in row]):
            return True
        #check column
        col_index=square%3
        column=[self.board[col_index+i*3] for i in range(3)]
        if all([spot==letter for spot in column]):
            return True
        
        #check diagonal
        #only if the square is even [ 0,2,4,6,8]
        #these are the only move to win diagonal
        if square%2==0:
            diagonal_1=[self.board[i] for i in [0,4,8]]
            if all([spot==letter for spot in diagonal_1]):
                return True
            diagonal_2=[self.board[i] for i in [2,4,6]]
            if all([spot==letter for spot in diagonal_2]):
                return True
        #if all the test fails
        return False
            
def play(game,x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    
    letter='X' #starting letter

    while game.empty_squares():
        #get the move from the appropriate player
        if letter == 'O':
            square=o_player.player.RandomComputerPlayer.get_move(game)
        else:
            square=x_player.player.HumanPlayer.get_move(game)
        
        #lets define a function to take a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f'makes a move to square {square}')
                game.print_board()
                print(' ') #just empty line
            if game.current_winner:
                if print_game:
                    print(letter + 'wins!')
            #after we made our move, we need to alternate letter
            letter='O' if letter=='X' else 'X'
        if print_game:
            print('Its a tie')

if __name__=='__main__':
    x_player=player.HumanPlayer('X')
    o_player=player.RandomComputerPlayer('o')
t=TicTacToe()
play(t, x_player, o_player,print_game=True)