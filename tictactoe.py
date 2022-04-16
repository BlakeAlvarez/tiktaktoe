    # [0,0,0,0],
    # [0,0,0,0],
    # [0,0,0,0],
    # [0,0,0,0],



from importlib.resources import read_binary
from pydoc import doc
from random import randint


Board = [
    [' ',' ',' ',' '],
    [' ',' ',' ',' '],
    [' ',' ',' ',' '],
    [' ',' ',' ',' '],
]




win = 100
lose = -100
merit = 30
draw = 0


def printBoard():
    for j, block in enumerate(Board):
        for i, square in enumerate(block):
            print(square, end="")
            if i < len(block)-1:
                print('|',end="")
        print()
        if j < 3:
            print("_ _ _ _")
            print()

def checkWin():
    global aiScore
    global humanScore
    for i in range(0,4):
        if (Board[i][0] == Board[i][1]) and (Board[i][1] == Board[i][2]) and (Board[i][2] == Board[i][3]) and (Board[i][0] != ' '):
            if Board[i][0] == 'X':
                print("Computer wins")
                
                aiScore+=win
                return True
            if Board[i][0] == 'O':
                print("Human wins")
                humanScore+=win
                return True

        if Board[0][i] ==  Board[1][i] and Board[1][i] == Board[2][i] and Board[2][i] == Board[3][i] and Board[0][i] != ' ':
            if Board[0][i] == 'X':
                print("Computer wins")
                aiScore+=win
                return True
            if Board[0][i] == 'O':
                print("Human wins")
                humanScore+=win
                return True

    if Board[0][0] == Board[1][1] and Board[1][1] == Board[2][2] and Board[2][2] == Board[3][3] and Board[0][0] != ' ':
            if Board[0][0] == 'X':
                print("Computer wins")
                aiScore+=win
                return True
            if Board[0][0] == 'O':
                print("Human wins")  
                humanScore+=win 
                return True     

    if Board[0][3] == Board[1][2] and Board[1][2] == Board[2][1] and Board[2][1] == Board[3][0] and Board[0][3] != ' ':
            if Board[0][3] == 'X':
                print("Computer wins")
                aiScore+=win
                return True
            if Board[0][3] == 'O':
                print("Human wins")
                humanScore+=win
                return True

def makeWinMove():

    for i in range(0,4):
        if Board[i][0] == Board[i][1] and Board[i][1] == Board[i][2] and Board[i][2] == Board[i][3] and Board[i][0] != ' ':
            Board[i][0] = 'O'
            return True

        if Board[0][i] ==  Board[1][i] and Board[1][i] == Board[2][i] and Board[2][i] == Board[3][i] and Board[0][i] != ' ':
            Board[0][i] = 'O'
            return True

    if Board[0][0] == Board[1][1] and Board[1][1] == Board[2][2] and Board[2][2] == Board[3][3] and Board[0][0] != ' ':
        Board[0][0] = 'O' 
        return True

    if Board[0][3] == Board[1][2] and Board[1][2] == Board[2][1] and Board[2][1] == Board[3][0] and Board[0][3] != ' ':
        Board[0][3] = 'O'
        return True

def blockWin():
    for i in range(0,4):
        if Board[i][0] == Board[i][1] and Board[i][1] == Board[i][2] and Board[i][2] == Board[i][3] and Board[i][0] == 'X' :
            Board[i][0] = 'O'
            return True

        if Board[0][i] ==  Board[1][i] and Board[1][i] == Board[2][i] and Board[2][i] == Board[3][i] and Board[0][i] == 'X':
            Board[0][i] = 'O'
            return True

    if Board[0][0] == Board[1][1] and Board[1][1] == Board[2][2] and Board[2][2] == Board[3][3] and Board[0][0] == 'X':
            Board[0][0] = 'O' 
            return True

    if Board[0][3] == Board[1][2] and Board[1][2] == Board[2][1] and Board[2][1] == Board[3][0] and Board[0][3] == 'X':
            Board[0][3] = 'O'
            return True


def checkMeritScore():
    global aiScore
    global humanScore

    for i in range(0,4):
# horizontals
        if Board[i][0] == Board[i][1] and Board[i][1] == Board[i][2] and Board[i][0] != ' ':
            if Board[i][0] == 'X':
                print("Merit Points for Computer")
                aiScore+=merit
                return True
            if Board[i][0] == 'O':
                print("Merit Points for Human")
                humanScore+=merit
                return True

        if Board[i][1] == Board[i][2] and Board[i][2] == Board[i][3] and Board[i][1] != ' ':
            if Board[i][1] == 'X':
                print("Merit Points for Computer")
                aiScore+=merit
                return True
            if Board[i][1] == 'O':
                print("Merit Points for Human")
                humanScore+=merit
                return True
# verticals
        if Board[0][i] ==  Board[1][i] and Board[1][i] == Board[2][i] and Board[0][i] != ' ':
            if Board[0][i] == 'X':
                print("Merit Points for Computer")
                aiScore+=merit
                return True
            if Board[0][i] == 'O':
                print("Merit Points for Human")
                humanScore+=merit
                return True

        if Board[1][i] == Board[2][i] and Board[2][i] == Board[3][i] and Board[1][i] != ' ':
            if Board[1][i] == 'X':
                print("Merit Points for Computer")
                aiScore+=merit
                return True
            if Board[1][i] == 'O':
                print("Merit Points for Human")
                humanScore+=merit
                return True
# left diag
    if Board[0][0] == Board[1][1] and Board[1][1] == Board[2][2] and Board[0][0] != ' ':
            if Board[0][0] == 'X':
                print("Merit Points for Computer")
                aiScore+=merit
                return True
            if Board[0][0] == 'O':
                print("Merit Points for Human")
                humanScore+=merit
                return True

    if Board[1][1] == Board[2][2] and Board[2][2] == Board[3][3] and Board[1][1] != ' ':
            if Board[1][1] == 'X':
                print("Merit Points for Computer")
                aiScore+=merit
                return True
            if Board[1][1] == 'O':
                print("Merit Points for Human")
                humanScore+=merit
                return True
# right diag
    if Board[0][3] == Board[1][2] and Board[1][2] == Board[2][1] and Board[0][3] != ' ':
            if Board[0][3] == 'X':
                print("Merit Points for Computer")
                aiScore+=merit
                return True
            if Board[0][3] == 'O':
                print("Merit Points for Human")
                humanScore+=merit
                return True

    if Board[1][2] == Board[2][1] and Board[2][1] == Board[3][0] and Board[1][2] != ' ':
            if Board[1][2] == 'X':
                print("Merit Points for Computer")
                aiScore+=merit
                return True
            if Board[1][2] == 'O':
                print("Merit Points for Human")
                humanScore+=merit
                return True

    if Board[0][2] == Board[1][1] and Board[1][1] == Board[2][0] and Board[0][2] != ' ':
            if Board[0][2] == 'X':
                print("Merit Points for Computer")
                aiScore+=merit
                return True
            if Board[0][2] == 'O':
                print("Merit Points for Human")
                humanScore+=merit
                return True
# left diag
    if Board[0][1] == Board[1][2] and Board[1][2] == Board[2][3] and Board[0][1] != ' ':
            if Board[0][1] == 'X':
                print("Merit Points for Computer")
                aiScore+=merit
                return True
            if Board[0][1] == 'O':
                print("Merit Points for Human")
                humanScore+=merit
                return True

    if Board[1][0] == Board[2][1] and Board[2][1] == Board[3][2] and Board[1][0] != ' ':
            if Board[1][0] == 'X':
                print("Merit Points for Computer")
                aiScore+=merit
                return True
            if Board[1][0] == 'O':
                print("Merit Points for Human")
                humanScore+=merit
                return True

    if Board[1][3] == Board[2][2] and Board[2][2] == Board[3][1] and Board[1][3] != ' ':
            if Board[1][3] == 'X':
                print("Merit Points for Computer")
                aiScore+=merit
                return True
            if Board[1][3] == 'O':
                print("Merit Points for Human")
                humanScore+=merit
                return True


def makeMeritMove():

    for i in range(0,4):
# horizontals
        if Board[i][0] == Board[i][1] and Board[i][2] == ' ' and Board[i][0] == 'O':
            Board[i][2] = 'O'
            return True

        if Board[i][1] == Board[i][2]  and Board[i][3] == ' ' and Board[i][1] == 'O':
            Board[i][3] = 'O'
            return True
        elif Board[i][1] == Board[i][2]  and Board[i][0] == ' ' and Board[i][1] == 'O':
                Board[i][0] = 'O'
                return True
# horizontal splits
        # if Board[i][0] == Board[i][2] and Board[i][1] == ' ' and Board[i][0] == 'O':
        #     Board[i][1] == 'O'
        #     print("what is happening right now?")
        #     return True

        # if Board[i][1] == Board[i][3] and Board[i][2] == ' ' and Board[i][1] == 'O':
        #     Board[i][2] == 'O'
        #     return True

# verticals
        if Board[0][i] ==  Board[1][i] and Board[2][i] == ' ' and Board[0][i] == 'O':
            Board[2][i] = 'O'
            return True

        if Board[1][i] == Board[2][i] and Board[3][i] == ' ' and Board[1][i] == 'O':
            Board[3][i] = 'O'
            return True
        elif Board[1][i] == Board[2][i] and Board[0][i] == ' ' and Board[1][i] == 'O':
                Board[0][i] = 'O'
                return True
# vertical splits
        if Board[0][i] ==  Board[2][i] and Board[1][i] == ' ' and Board[0][i] == 'O':
            Board[1][i] = 'O'
            return True

        if Board[1][i] ==  Board[3][i] and Board[2][i] == ' ' and Board[1][i] == 'O':
            Board[2][i] = 'O'
            return True

# left diag
    if Board[0][0] == Board[1][1] and Board[2][2] == ' ' and Board[0][0] == 'O':
        Board[2][2] = 'O'
        return True

    if Board[1][1] == Board[2][2] and Board[3][3] == ' ' and Board[1][1] == 'O':
        Board[3][3] = 'O'
        return True
    elif Board[1][1] == Board[2][2] and Board[0][0] == ' ' and Board[1][1] == 'O':
            Board[0][0] = 'O'
            return True

    if Board[2][2] == Board[3][3] and Board[1][1] == ' ' and Board[2][2] == 'O':
        Board[1][1] = 'O'
        return True

# right diag
    if Board[0][3] == Board[1][2] and Board[2][1] == ' ' and Board[0][3] == 'O':
        Board[2][1] = 'O'
        return True

    if Board[1][2] == Board[2][2] and Board[0][3] == ' ' and Board[1][2] == 'O':
        Board[0][3] = 'O'
        return True
    elif Board[1][2] == Board[2][2] and Board[3][0] == ' ' and Board[1][2] == 'O':
            Board[3][0] = 'O'
            return True

    if Board[0][3] == Board[1][2] and Board[2][1] == ' ' and Board[0][3] == 'O':
        Board[2][1] = 'O'
        return True


    if Board[0][2] == Board[1][1] and Board[2][0] == ' ' and Board[0][2] == 'O':
        Board[2][0] = 'O'
        return True
    
    if Board[1][1] == Board[2][0] and Board[0][2] == ' ' and Board[1][1] == 'O':
        Board[1][2] = 'O'
        return True

    if Board[0][1] == Board[1][2] and Board[2][3] == ' ' and Board[0][1] == 'O':
        Board[2][3] = 'O'
        return True

    if Board[1][2] == Board[2][3] and Board[0][1] == ' ' and Board[1][2] == 'O':
        Board[0][1] = 'O'
        return True

    if Board[1][0] == Board[2][1] and Board[3][2] == ' ' and Board[1][0] == 'O':
        Board[3][2] = 'O'
        return True

    if  Board[2][1] == Board[3][2] and Board[1][0] == ' ' and Board[2][1] == 'O':
        Board[1][0] = 'O'
        return True

    if Board[1][3] == Board[2][2] and Board[3][1] == ' ' and Board[1][3] == 'O':
        Board[3][1] = 'O'
        return True

    if Board[2][2] == Board[3][1] and Board[1][3] == ' ' and Board[2][2] == 'O':
        Board[1][3] = 'O'
        return True

# all other splits
    if Board[0][2] == Board[2][0] and Board[1][1] == ' ' and Board[0][2] == 'O':
        Board[1][1] = 'O'
        return True

    if Board[0][3] == Board[2][1] and Board[1][2] == ' ' and Board[0][3] == 'O':
        Board[1][2] = 'O'
        return True

    if Board[0][0] == Board[2][2] and Board[1][1] == ' ' and Board[0][0] == 'O':
        Board[1][1] = 'O'
        return True

    if Board[1][1] == Board[3][3] and Board[2][2] == ' ' and Board[1][1] == 'O':
        Board[2][2] = 'O'
        return True

    if Board[0][1] == Board[2][3] and Board[1][2] == ' ' and Board[0][1] == 'O':
        Board[1][2] = 'O'
        return True

    if Board[1][0] == Board[3][2] and Board[2][1] == ' ' and Board[1][0] == 'O':
        Board[2][1] = 'O'
        return True

    if Board[1][3] == Board[3][1] and Board[2][2] == ' ' and Board[1][3] == 'O':
        Board[2][2] = 'O'
        return True

    if Board[3][0] == Board[1][2] and Board[2][1] == ' ' and Board[3][0] == 'O':
        Board[2][1] = 'O'
        return True


def blockMeritScore():
    for i in range(0,4):
# horizontals
        if Board[i][0] == Board[i][1] and Board[i][2] == ' ' and Board[i][0] == 'X':
            Board[i][2] = 'O'
            return True

        if Board[i][1] == Board[i][2]  and Board[i][3] == ' ' and Board[i][1] == 'X':
            Board[i][3] = 'O'
            return True
        elif Board[i][1] == Board[i][2]  and Board[i][0] == ' ' and Board[i][1] == 'X':
                Board[i][0] = 'O'
                return True
# horizontal splits
        # if Board[i][0] == Board[i][2] and Board[i][1] == ' ' and Board[i][0] == 'X':
        #     Board[i][1] == 'O'
        #     print(":this shit buggin", Board[i][1], "no fucking way bro")
        #     return True
        # if Board[i][1] == Board[i][3] and Board[i][2] == ' ' and Board[i][1] == 'X':
        #     Board[i][2] == 'O'
        #     print(":this shit buggin", Board[1][2], "no fucking way bro")
        #     return True

# verticals
        if Board[0][i] ==  Board[1][i] and Board[2][i] == ' ' and Board[0][i] == 'X':
            Board[2][i] = 'O'
            return True

        if Board[1][i] == Board[2][i] and Board[3][i] == ' ' and Board[1][i] == 'X':
            Board[3][i] = 'O'
            return True
        elif Board[1][i] == Board[2][i] and Board[0][i] == ' ' and Board[1][i] == 'X':
                Board[0][i] = 'O'
                return True


# vert splits
        if Board[0][i] ==  Board[2][i] and Board[1][i] == ' ' and Board[0][i] == 'X':
            Board[1][i] = 'O'
            return True

        if Board[1][i] ==  Board[3][i] and Board[2][i] == ' ' and Board[1][i] == 'X':
            Board[2][i] = 'O'
            return True





# left diag
    if Board[0][0] == Board[1][1] and Board[2][2] == ' ' and Board[0][0] == 'X':
        Board[2][2] = 'O'
        return True

    if Board[1][1] == Board[2][2] and Board[3][3] == ' ' and Board[1][1] == 'X':
        Board[3][3] = 'O'
        return True
    elif Board[1][1] == Board[2][2] and Board[0][0] == ' ' and Board[1][1] == 'X':
            Board[0][0] = 'O'
            return True

    if Board[2][2] == Board[3][3] and Board[1][1] == ' ' and Board[2][2] == 'X':
        Board[1][1] = 'O'
        return True

# right diag
    if Board[0][3] == Board[1][2] and Board[2][1] == ' ' and Board[0][3] == 'X':
        Board[2][1] = 'O'
        return True

    if Board[1][2] == Board[2][2] and Board[0][3] == ' ' and Board[1][2] == 'X':
        Board[0][3] = 'O'
        return True
    elif Board[1][2] == Board[2][2] and Board[3][0] == ' ' and Board[1][2] == 'X':
            Board[3][0] = 'O'
            return True

    if Board[0][3] == Board[1][2] and Board[2][1] == ' ' and Board[0][3] == 'X':
        Board[2][1] = 'O'
        return True


    if Board[0][2] == Board[1][1] and Board[2][0] == ' ' and Board[0][2] == 'X':
        Board[2][0] = 'O'
        return True
    
    if Board[1][1] == Board[2][0] and Board[0][2] == ' ' and Board[1][1] == 'X':
        Board[1][2] = 'O'
        return True

    if Board[0][1] == Board[1][2] and Board[2][3] == ' ' and Board[0][1] == 'X':
        Board[2][3] = 'O'
        return True

    if Board[1][2] == Board[2][3] and Board[0][1] == ' ' and Board[1][2] == 'X':
        Board[0][1] = 'O'
        return True


    if Board[1][0] == Board[2][1] and Board[3][2] == ' ' and Board[1][0] == 'X':
        Board[3][2] = 'O'
        return True

    if  Board[2][1] == Board[3][2] and Board[1][0] == ' ' and Board[2][1] == 'X':
        Board[1][0] = 'O'
        return True

    if Board[1][3] == Board[2][2] and Board[3][1] == ' ' and Board[1][3] == 'X':
        Board[3][1] = 'O'
        return True

    if Board[2][2] == Board[3][1] and Board[1][3] == 'O' and Board[2][2] == 'X':
        Board[1][3] = 'O'
        return True
# all other splits
    if Board[0][2] == Board[2][0] and Board[1][1] == ' ' and Board[0][2] == 'X':
        Board[1][1] = 'O'
        return True

    if Board[0][3] == Board[2][1] and Board[1][2] == ' ' and Board[0][3] == 'X':
        Board[1][2] = 'O'
        return True

    if Board[0][0] == Board[2][2] and Board[1][1] == ' ' and Board[0][0] == 'X':
        Board[1][1] = 'O'
        return True

    if Board[1][1] == Board[3][3] and Board[2][2] == ' ' and Board[1][1] == 'X':
        Board[2][2] = 'O'
        return True

    if Board[0][1] == Board[2][3] and Board[1][2] == ' ' and Board[0][1] == 'X':
        Board[1][2] = 'O'
        return True

    if Board[1][0] == Board[3][2] and Board[2][1] == ' ' and Board[1][0] == 'X':
        Board[2][1] = 'O'
        return True

    if Board[1][3] == Board[3][1] and Board[2][2] == ' ' and Board[1][3] == 'X':
        Board[2][2] = 'O'
        return True

    if Board[3][0] == Board[1][2] and Board[2][1] == ' ' and Board[3][0] == 'X':
        Board[2][1] = 'O'
        return True

def randomMove():
    while True:
        i = randint(0, 3)
        j = randint(0, 3)
        if Board[i][j] == ' ':
            print("The move is: ", i," ",j)
            Board[i][j] = 'O'
            break

def humanTurn():
    if (makeWinMove() == True):
        # return True
        print("this works1")   
        pass
    elif (blockWin() == True):
        # return True
        print("this works2")   
        pass
    elif (makeMeritMove() == True):
        # return True
        
        print("this works3")
        pass
    elif (blockMeritScore() == True):
        # return True
        print("this works4")   
        pass
    else:
        print("this works5")   
        randomMove()

def myTurn():
    while True:
        i = int(input("Enter row: "))
        j = int(input("enter column: "))
        if (Board[i][j] == ' '):   
            Board[i][j] = 'X'
            break



boardScores = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]



def neighborCheck(i, j):
    try:
        if Board[i-1][j-1] == 'X' and  i >= 0 and i < 4 and j >= 0 and j < 4:
            boardScores[i][j]+=1
    except IndexError:
        pass

    try:
        if Board[i-1][j] == 'X' and  i >= 0 and i < 4 and j >= 0 and j < 4:
            boardScores[i][j]+=1
    except IndexError:
        pass

    try:
        if Board[i-1][j+1] == 'X' and  i >= 0 and i < 4 and j >= 0 and j < 4:
            boardScores[i][j]+=1
    except IndexError:
        pass

    try:
        if Board[i][j-1] == 'X' and  i >= 0 and i < 4 and j >= 0 and j < 4:
            boardScores[i][j]+=1
    except IndexError:
        pass

    try:
        if Board[i][j+1] == 'X' and  i >= 0 and i < 4 and j >= 0 and j < 4:
            boardScores[i][j]+=1
    except IndexError:
        pass

    try:
        if Board[i+1][j-1] == 'X' and  i >= 0 and i < 4 and j >= 0 and j < 4:
            boardScores[i][j]+=1
    except IndexError:
        pass

    try:
        if Board[i+1][j] == 'X' and  i >= 0 and i < 4 and j >= 0 and j < 4:
            boardScores[i][j]+=1
    except IndexError:
        pass

    try:
        if Board[i+1][j+1] == 'X' and  i >= 0 and i < 4 and j >= 0 and j < 4:
            boardScores[i][j]+=1
    except IndexError:
        pass


def setBoardScores():
    for i in range(0,4):
        for j in range(0,4):
            if Board[i][j] == ' ':
                neighborCheck(i,j)

def makeBestMove():
    highest = boardScores[0][0]
    iCoord = 0
    jCoord = 0
    for i in range(0,4):
        for j in range(0,4):
            if boardScores[i][j] > highest and Board[i][j] != 'X':
                highest = boardScores[i][j]
                iCoord = i
                jCoord = j
    print("i: ", iCoord, "j: ", jCoord)
    return iCoord, jCoord

def aiMove():
    i,j = makeBestMove()
    Board[i][j] = 'X'
    setBoardScores()
    
def printBoardScores():
    for j, block in enumerate(boardScores):
        for i, square in enumerate(block):
            print(square, end="")
            if i < len(block)-1:
                print('|',end="")
        print()
        if j < 3:
            print("_ _ _ _")
            print()

humanScore = 0
aiScore = 0
for j in range(100):
    Board = [
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
    ]
    boardScores = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    
    for i in range(8):
        printBoardScores()
        humanTurn()
        if (checkWin() == True):
            break
        printBoard()
        print()
        print()
        aiMove()
        if (checkWin() == True):
            break
        printBoard()
    checkMeritScore()
    print("Human Score: ", humanScore, "\nComputer Score: ", aiScore)




print("FINAL SCORES")
print("Human Score: ", humanScore, "\nComputer Score: ", aiScore)