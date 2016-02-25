#100 boxes

ACTIONS = [[2,-2],[2,2],[-2,2],[-2,-2],[0,3],[3,0],[-3,0],[0,-3]]
# 0:RightUp 1:RightDown 2:LeftDown 3:LeftUp 4:Down 5:Right 6:Left 7:Up
board = [[0 for i in range(10)] for n in range(10)] #prints a 10X10 array
board[0][0] = 1 #y axis first, then x [y,x]
past_moves = [[]]


#global location
location = [0, 0]
#performs a move, takes an index of ACTION as input
def location_change(action_n): 
    location[0] += ACTIONS[action_n][0]
    location[1] += ACTIONS[action_n][1]
    return location
#places the inputted value/number on the current location
def place(value):
    board[location[1]][location[0]] = value
    return board
#reverts the current location back to zero    
def delete():
    board[location[1]][location[0]] = 0
#loops through all actions, records possibilities as index of ACTIONS
def check_options():
    possibilities = []
    #loops through index of ACTIONS, possible ones stay on board#loops through index of ACTIONS, possible ones stay on board
    for p in range(8):
        if (ACTIONS[p][0] + location[0] <= 9 and\
        ACTIONS[p][0] + location[0] >= 0 and\
        ACTIONS[p][1] + location[1] <= 9 and\
        ACTIONS[p][1] + location[1] >= 0 and\
        board[ACTIONS[p][1] + location[1]][ACTIONS[p][0] + location[0]] == 0)\
        :possibilities.append(p)
    return possibilities
#prints the array board
def print_board(): #prints board in array format
    for i in board:
        print i
        
location_change(5)
place(2)
location_change(2)
place(3)
print_board()
print check_options()



        

