# tic tac toe game / noughts and crosses
#Exercise 1
import numpy as np

def create_board():
    tictacboard = np.zeros((3,3))
    return tictacboard

board = create_board()
board


#exercise 2
board = create_board()
def place(board, player, position):
    if player == 1:
        board[position] = player
    elif player == 2:
        board[position] = player

place(board,1,(0,0))
board

#exercise 3 (Still have to fix to work seperately)

Altpossible = board
def Original_possibilities(board):
    # numpy.where
    # possible = ()
    Altpossible = np.where(board == 0,1,0)
    return Altpossible

Original_possibilities(board)

# Alternative method as per exercise requirements
# def possibilities(board):
#     # numpy.where
#     # possible = ()
#     board_free = np.where(board == 0,1,0)
#     board_free
#     row = 0
#     possible = []
#     for line in board_free:
#         #print(line)
#         column = 0
#         for down in line:
#             #print(column)
#             #print('B' + str(board_free[row, down]))
#             if board_free[row,down] == 1:
#                 possible.append([row,column])
#             column =+ 1
#         row =+ 1
#     #print(row)
#     #possible = list(zip(board_free[0],board_free[1],board_free[2]))
#     return possible
#
# print(len(possibilities(board)))
# possibilities(board)

def possibilities(board):
    possible = []
#    print(possible)
    for i in range(3):
        for j in range(3):
            value = board[i][j]
#            print(value)
            if value == 0.0:
                possible.append((i,j))
#                print(possible)
    # numpy.where
    # possible = ()
    return possible

#print(len(possibilities(board)))
possibilities(board)

#exercise 4 (Complete)
import random

def random_place(board, player):
    new_pos_coordinates = random.choice(possibilities(board))
    board[new_pos_coordinates[0], new_pos_coordinates[1]] = player

random_place(board, 2)
board

#exercise 5 (Complete)
board = create_board()
for i in range(3):
    for player in [1, 2]:
        # add here!
        j = (i) % 2
#        print(str(i) + ' - ' + str(j))
        random_choice(board,player)

print(board)

#exercise 6 (Complete)
# write your code here!
board = np.array([[2, 2, 1],[0, 1, 0],[1, 1, 2]])

board = np.array([[2, 2, 1],[0, 1, 0],[2, 1, 2]])

def row_win(board, player):
    check = []
    for i in board:
        status = all(player == i)
        check.append(status)
    result = True in check
    return result
#    if status == True:
#            return status
print(board)
row_win(board,2)

#exercise 7 (Complete)
# write your code here!
board = np.array([[2, 1, 1],[0, 1, 0],[0, 1, 2]])

def col_win(board, player):
    Tboard = board.transpose()
    check = []
    for i in Tboard:
        status = all(player == i)
        check.append(status)
    result = True in check
    return result
print(board)
#print(board)
col_win(board,1)

#exercise 8 (Complete)
board = np.array([[2, 2, 1],[0, 2, 0],[1, 1, 2]])
def diag_win(board, player):
    LRDiag = []
    RLDiag = []
    for i in range(3):
        LRDiag.append(board[i][i] == player)
        RLDiag.append(board[i][-i + 2] == player)
    status = all(LRDiag) or all(RLDiag)
    return status
print(board)
diag_win(board, 2)


#exercise 9 (Complete)
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply.  if so, store `player` as `winner`.
#        print(player)
        if row_win(board,player) == True or col_win(board,player) == True or diag_win(board,player) == True:
            winner = player
#            print('The winner is ' + str(winner))
            return winner
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

# add your code here.

evaluate(board)


#exercise 10 (Complete)
def play_game():
    board = create_board()
    for i in range(9):
        player = i % 2 + 1
#        print('Player ' + str(player))
        random_place(board,player)
#        print(board)
        winner = evaluate(board)
        if winner != 0:
#            print('Result ' + str(winner))
            return winner

play_game()

#exercise 11 (Complete)
import time
import matplotlib.pyplot as plt

start_time = time.clock()
Game_result = []
time.time()
for rep in range(1000):
    Game_result.append(play_game())

end_time = time.clock()
print(end_time - start_time)
Game_result
time.time()
plt.hist(Game_result)
plt.show()

#exercise 12 (Complete)
def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            # use `random_place` to play a game, and store as `board`.
            # use `evaluate(board)`, and store as `winner`.
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

play_strategic_game()

#exercise 13 (WIP)
import time
import matplotlib.pyplot as plt

start_time = time.clock()
Game_result = []
time.time()
for rep in range(1000):
    Game_result.append(play_strategic_game())

end_time = time.clock()
print(end_time - start_time)
Game_result
time.time()
plt.hist(Game_result)
plt.show()