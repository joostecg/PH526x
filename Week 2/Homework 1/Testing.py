def random_place(board, player):
    available = possibilities(board)
    available

#    selection = [random.choice([0,1,2]), random.choice([0,1,2])]
    selection = [random.choice(available)]
    selection
    random.choice(selection)
    available_value = available[selection[0],selection[1]]
    available_value

    for i in range(len(myArray)):
        for j in range(len(myArray[i])):
            print
            myArray[i][j]

    random.choice(list(enumerate(possibilities(board))))[0]
    # selection = random.choice(available)
    # player = 2
    # selection[random.randint(0, len(selection)- 1)] = player
    # selection




    random.choice(selection)

    place(board,2,randomplace)
    # return selection


random_place(board, 2)
board

 [1]: possibilities(board)
Out[1]: [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

In [2]: pos = possibilities(board)

In [3]: pos[1][2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    pos[1][2]
IndexError: tuple index out of range

In [4]: pos[1],[2]
Out[4]: ((0, 2), [2])

In [5]: pos[1]
Out[5]: (0, 2)

In [6]: select = pos[1]

In [7]: select
Out[7]: (0, 2)

In [8]: select[1]
Out[8]: 2

In [9]: select[0]
Out[9]: 0

In [10]: board
Out[10]:
array([[1, 0, 0],
       [0, 0, 0],
       [0, 0, 0]])

In [11]: board([select[0],select[1]])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    board([select[0],select[1]])
TypeError: 'numpy.ndarray' object is not callable

In [12]: board[select[0],select[1]]
Out[12]: 0

In [13]:

A = [[ 1, 2, 3],[ 4, 5, 6]]
A
zip(*A)



def col_win(board, player):
    column = []
    for i in range(3):
        print(i)
        for j in board:
            print(j)
            check_column.append([board[j], board[i]])

    print(column)
    status = True
    return status


col_win(board, 1)


def possibilities(board):
    # numpy.where
    # possible = ()
    board_free = np.where(board == 0,1,0)
    board_free
    b = list(np.where(board_free == 1))
    b

    value = 1
    if value in board_free:
        board_index = list(board_free).index(value)
    board_index

    val = 1
    y = [(index, row.index(val)) for index, row in enumerate(board_free) if val in row]
    y
    for (x,y) in range(board_free.shape):
        print(board_free[[x],[y]])
    board_free[[0],[2]]
    row = 0
    possible = []
    for (x,y,z) in board_free:
        print(x,y,z)
        column = 0
        for down in line:
            #print(column)
            #print('B' + str(board_free[row, down]))
            if board_free[row,down] == 1:
                possible.append([row,column])
            column =+ 1
        row =+ 1
    #print(row)
    #possible = list(zip(board_free[0],board_free[1],board_free[2]))
    return possible

print(len(possibilities(board)))
possibilities(board)

def col_win(board, player):
    check = []
    print(board)
    Tboard = board.transpose()
    for i in Tboard:
        check.append(all(player == i))
        print (check)
#    status = True
    status = check == True
    print (status)
    return status