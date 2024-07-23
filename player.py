import copy
#import time
 
class MyPlayer:
    '''Player playing based on the move value'''
 
    def __init__(self, my_color, opponent_color):
        self.my_color = my_color #1 or 0
        self.opponent_color = opponent_color #1 or 0
        self.name = 'veselsa1'
        self.value_board = [[8, 2, 6, 4, 4, 6, 2, 8], #fields are evaluated according to importance and relevance in the game
                            [2, 0, 4, 4, 4, 4, 0, 2],
                            [6, 4, 6, 6, 6, 6, 4, 6],
                            [4, 4, 6, 6, 6, 6, 4, 4],
                            [4, 4, 6, 6, 6, 6, 4, 4],
                            [6, 4, 6, 6, 6, 6, 4, 6],
                            [2, 0, 4, 4, 4, 4, 0, 2],
                            [8, 2, 6, 4, 4, 6, 2, 8]]
 
    def transpose(self, temp_board): #transposition of board for scaning the column
        return [*zip(*temp_board)]
 
    def find_valid_move_in_row(self, ro, co, board, n):
        point = board [ro][co] #element which is my opponents stone 
        #print(board)
        #print(point,':', ro, co)
        self.temp = n
        #print(n)
        move_is_valid = 0 #when i find possible move to empty position
        my_valid_move = () #writing down the valid move 
        my_valid_move_reversed = () #writing down valid move for column when it's necessary
        row = board[ro] #for counting a size of board
        #print(row)
        profit_of_stones = 0 #number of stones i win in this move 
 
        for l in range(co,len(row)): #for cyklus for going throw a row
            if row[l] == self.my_color: 
                move_is_valid = 1
                break
            elif row[l] == -1: 
                my_valid_move = (ro, l, profit_of_stones + self.value_board[ro][l])
                my_valid_move_reversed = (l, ro, profit_of_stones + self.value_board[l][ro])
                break
            profit_of_stones += 1
         
        for k in range(co, -1, -1): #for cyklus for going throw a row but to the back
            if row[k] == self.my_color:
                move_is_valid = 1
                break
            elif row[k] == -1:
                my_valid_move = (ro, k, profit_of_stones + self.value_board[ro][k])
                my_valid_move_reversed = (k, ro, profit_of_stones + + self.value_board[k][ro])
                break
            profit_of_stones += 1
        #print(my_valid_move, my_valid_move_reversed)
        #print(self.temp)
        #print(move_is_valid)
        if (self.temp == 1 and move_is_valid == 1 and my_valid_move_reversed != ()): #condition when we went through column, found valid move and wrote it down as a tuple
            if (board[ro][l] == -1 or board [ro][k] == -1): 
                move_is_valid = 0
                return my_valid_move_reversed
 
        if (self.temp == 0 and move_is_valid == 1 and my_valid_move != ()): #condition when we went through row, found valid move and wrote it down as a tuple
            if (board[ro][l] == -1 or board [ro][k] == -1):
                move_is_valid = 0
                return my_valid_move
         
     
    def find_valid_move_in_diag_to_right(self, ro, co, board):
        point_1 = board [ro][co]
        #print(point_1, ':', ro, co)
        move_is_valid_1 = 0
        my_valid_move_1 = ()
        row = board[ro]
        n = co
        q = co
        profit_of_stones = 0
 
        for m in range (ro, -1, -1):
            if board[m][n] == self.my_color:
                move_is_valid_1 = 1
                break
            elif board[m][n] == -1:
                my_valid_move_1 = (m, n, profit_of_stones + self.value_board[m][n])
                break
            profit_of_stones += 1
            n += 1
            if (n == 8):
                break
         
        for p in range (ro, len(row)):
            if board[p][q] == self.my_color:
                move_is_valid_1 = 1
                break
            elif board[p][q] == -1:
                my_valid_move_1 = (p,q, profit_of_stones + self.value_board[p][q])
                break
            profit_of_stones += 1
            q -= 1
            if (q == -1):
                break
         
        if (move_is_valid_1 == 1 and my_valid_move_1 != ()):
            if (board[m][n] == -1 or board [p][q] == -1):
                move_is_valid_1 = 0
                return my_valid_move_1
 
 
    def find_valid_move_in_diag_to_left(self, ro, co, board):
        point_2 = board [ro][co]
        move_is_valid_2 = 0
        my_valid_move_2 = ()
        row = board[ro]
        s = co
        v = co
        profit_of_stones = 0
 
        for r in range (ro, -1, -1):
            if board[r][s] == self.my_color:
                move_is_valid_2 = 1
                break
            elif board[r][s] == -1:
                my_valid_move_2 = (r, s, profit_of_stones + self.value_board [r][s])
                break
            profit_of_stones += 1
            s -= 1
            if (s == -1):
                break
         
        for u in range (ro, len(row)):
            if board[u][v] == self.my_color:
                move_is_valid_2 = 1
                break
            elif board[u][v] == -1:
                my_valid_move_2 = (u, v, profit_of_stones + self.value_board [u][v])
                break
            profit_of_stones += 1
            v += 1
            if (v == 8):
                break
         
        if (move_is_valid_2 == 1 and my_valid_move_2 != ()):
            if (board[u][v] == -1 or board[r][s] == -1):
                move_is_valid_2 = 0
                return my_valid_move_2
     
    def sortFunc(self, e): #sort function for last step to choose the best move
        return e[2]
 
    def move (self, board):
        #start_time = time.time()
         
        self.temp = -1 #variable needed in find_valid_move_in_row to know whether we are working with original board or transposed
        set_of_valid_moves = set([]) #set for all possible moves for this situation
         
        for i in range (0, len(board)): #going through whole board and searching for opponents draughtsmens
            for j in range (0, len(board)):
                n = 0 #variable needed in find_valid_move_in_row to know whether we are working with original board or transposed
                if (board[i][j] == self.opponent_color):
                    #print('board:', i, j)
                    #finding all possible moves
                    set_of_valid_moves.add(self.find_valid_move_in_row(i, j, board, n))
                    #print(set_of_valid_moves)
                    n = 1
                    temp_board = copy.deepcopy(board) #creating temporary array for transposition board
                    temp_board = self.transpose(temp_board) 
                    set_of_valid_moves.add(self.find_valid_move_in_row(j, i, temp_board, n))
                    #print(set_of_valid_moves)
                    set_of_valid_moves.add(self.find_valid_move_in_diag_to_right(i, j, board))
                    #print(set_of_valid_moves)
                    set_of_valid_moves.add(self.find_valid_move_in_diag_to_left(i, j, board))
                    #print(set_of_valid_moves)
 
        valid_set = {x for x in set_of_valid_moves if x != None} #making new set without None which appears when in some function is the return my_valid_move empty
        #print(valid_set)
        my_ret = list(valid_set) #converting set to list with tuples
        #print(my_ret)
 
        #elapsed_time = time.time() - start_time
        #print('Elapsed time:', elapsed_time)
         
        if (valid_set == set()):
            return None
        else:
            my_ret.sort(reverse = True, key=self.sortFunc) #sorting tuples from highest valuated moves to lowest
            my_final_move = (my_ret[0][0], my_ret[0][1]) #creating move player plays
            return my_final_move
 
 
if __name__ == '__main__':
 
    board = [[-1, -1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1, -1],
             [-1, -1, 0, -1, 0, 1, -1, -1],
             [-1, -1, 0, 0, 1, -1, -1, -1],
             [-1, -1, 0, 1, 0, -1, -1, -1],
             [-1, -1, 0, 1, 0, -1, -1, -1],
             [-1, -1, 0, -1, -1, 0, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1, -1]]
    p1 = MyPlayer(1, 0)
    print(p1.move(board))
