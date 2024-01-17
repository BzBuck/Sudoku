import math


mpty = [
    # x 0 1 2  3 4 5  6 7 8   y
        0,0,0, 0,0,0, 0,0,0, #0
        0,0,0, 0,0,0, 0,0,0, #1
        0,0,0, 0,0,0, 0,0,0, #2

        0,0,0, 0,0,0, 0,0,0, #3
        0,0,0, 0,0,0, 0,0,0, #4
        0,0,0, 0,0,0, 0,0,0, #5
        
        0,0,0, 0,0,0, 0,0,0, #6
        0,0,0, 0,0,0, 0,0,0, #7
        0,0,0, 0,0,0, 0,0,0, #8
        ]

# full flat 81 item board array in reading order
board = [
    # x 0 1 2  3 4 5  6 7 8   y
        1,2,3, 4,5,6, 7,8,9, #0
        4,5,6, 7,8,9, 1,2,3, #1
        7,8,9, 1,2,3, 4,5,6, #2

        2,3,1, 5,6,4, 8,9,7, #3
        5,6,4, 8,9,7, 2,3,1, #4
        8,9,7, 2,3,1, 5,6,4, #5
        
        3,1,2, 6,4,5, 9,7,8, #6
        6,4,5, 9,7,8, 3,1,2, #7
        9,7,8, 3,1,2, 6,4,5, #8
        ] 


board = [
    # x 0 1 2  3 4 5  6 7 8   y
        0,0,0, 0,0,0, 0,0,0, #0
        0,0,0, 4,0,0, 9,0,0, #1
        0,0,2, 0,0,3, 8,0,4, #2

        6,0,0, 5,0,0, 0,0,2, #3
        0,9,0, 0,0,0, 7,0,0, #4
        2,0,0, 0,9,7, 0,0,6, #5
        
        4,0,5, 2,0,0, 3,0,0, #6
        0,0,0, 0,8,0, 1,0,0, #7
        9,8,0, 3,0,5, 0,0,0, #8
        ]

gp = 0
ip = 0

board_column = [] # 9x9 digit columns
board_row = [] # 9x9 digit rows
board_cell = [] # 9x9 digit cells

''''
candidate_row = [] # 9x9xN candidate rows
candidate_column = [] # 9x9xN candidate columns
candidate_cell = [] # 9x9xN candidate cells

Posible take these 3 and then mix for full
'''


board_candidates = [] # 81xN candidate spaces

# posible if value known, either mark number or 0
# posible elimination method: in candidates if value eliminated store negative
# posible use candidates as practical board

# input: standard board 81
# output: cleanly printed board 
def display(board):
    for i in range(27):
        if i % 3 == 0:
            if i % 9 == 0:
               print("\n------|------|------|",end = '') 
            print('')#"\n---------|--------")#'\n')
        for j in range(3):
            print(board[3*i+j],end=' ')
        print('',end='|')
    print('\n')

# input: standard board 81
# output: 9x9 matrix rows
def rower(board):
    row = []
    for i in range(9):
        row += [board[9*i:9*i+9]]
    return row

# input: standard board 81
# output: 9x9 matrix columns
def columner(board):
    col = [[0 for i in range(9)] for j in range(9)]
    for j in range(9):
        for i in range(9):
            col[j][i] = board[i*9+(j%9)]
    return col

# input: standard board 81
# output: 9x9 matrix cells
def celler(board):
    cell = [[]for j in range(9)]
    for j in range(9):
        for i in range(3):
            cell[j]+= board[i*9+3*j+ 18*math.floor(j/3):i*9+3+3*j+ 18*math.floor(j/3)] #012, 91011...
    return cell

# input pos: position of item 0-80
# output: [x,y,z] of a points position in col row cell
def coordinate(pos):
    x = pos % 9  # column
    y = math.floor(pos/9)# row
    z = math.floor(x/3) + math.floor(y/3)*3 # cell

    return [x,y,z]

# input 
def reposition(x=(-1,-1),y=(-1,-1),z=(-1,-1)):
    if x != (-1,-1):
        pos = (x[1] % 9) + x[0] * 9
    elif y != (-1,-1):
        pos = (y[0] % 9) + y[1] * 9

    elif z != (-1,-1):
        pos = (x[0] % 9)  * x[1]


    return pos


def flatten(arr):
    arrout = []
    for i in arr:
        if isinstance(i,list):
             arrout += flatten(i)
        else:
            arrout.append(i)
    return arrout


def uncan(candidates):
    for i in range(81):
        if isinstance(candidates[i],list):
            candidates[i] = 0

    return candidates



def ex(candidates):
    row = rower(candidates)
    col = columner(candidates)
    cell = celler(candidates)
    for i in range(81):
        if isinstance(candidates[i],list):
            for j in candidates[i]:
                if flatten(row[coordinate(i)[1]]).count(j) == 1 or flatten(col[coordinate(i)[0]]).count(j) == 1 or flatten(cell[coordinate(i)[2]]).count(j) == 1:
                    candidates[i] = j
    return candidates

def candidate(board):
    row = rower(board)
    col = columner(board)
    cell = celler(board)

    for i in range(81):
        coords = coordinate(i)
        if board[i] == 0:
            board[i] = []
            for j in range(1,10):
                if j not in row[coords[1]] and j not in col[coords[0]] and j not in cell[coords[2]]:  
                    board[i].append(j)

    return board




def flatten2(candidates):
    for i in range(81):
        try:
            if len(candidates[i]) == 1:
                candidates[i] = candidates[i][0]
        except:
            continue
    return candidates
    


# true if there are no errors
def err(board):
    row = rower(board)
    col = columner(board)
    cell = celler(board)
    for i in row:
        for j in i:
            if isinstance(j,list) == False:
                if  1 <= j <= 9 and i.count(j) > 1:
                    return False
    for i in col:
        for j in i:
            if isinstance(j,list) == False:
                if  1 <= j <= 9 and i.count(j) > 1:
                    return False
    for i in cell:
        for j in i:
            if isinstance(j,list) == False:
                if  1 <= j <= 9 and i.count(j) > 1:
                    return False
    return True


# update the board
def upbo(board):
    board = flatten2(ex(candidate(board)))
    if err(board) == False:
        return False
    return board


def runthru(board):
    old = board.copy()
    try:
        while board != uncan(upbo(board.copy())):
            uncan(upbo(board))
    except:
        return old
  
    return board




def forck(board):
    upbo(board)
    temp = board.copy()

    for ipa in range(len(board)):
        if isinstance(board[ipa], list):
            for gpa in range(len(board[ipa])):
                temp = board.copy()
                temp[ipa] = board[ipa][gpa]
                runthru(temp)
                if (0 in temp) == False and temp == flatten(temp):
                    return temp
      

    return board
    

board = forck(board.copy())


print('start')

# display([i for i in range(81)]) # index preview



print(err(board))
display(board)  
print('sucess')
