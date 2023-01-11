#Tic Tac Toe Game Python

import random
from array import*
import copy

print()   # Welcome Message.
print("DEVELOPED BY Hamza Shaukat(BCT-008)")
print("converted the code from 1D array to 2D array by Faisal Mahmood")
print("this project is for testing")
print()
user = input("Please enter your Name: ").capitalize()



def printBoard2D(board2d):
    # "theBoard" is a list of 10 strings representing the board (0 not included)
    print(' ' + str(board2d[0][0]) + ' | ' + str(board2d[0][1]) + ' | ' + str(board2d[0][2])) 
    print('--- --- ---')
    print(' ' + str(board2d[1][0]) + ' | ' + str(board2d[1][1]) + ' | ' +str(board2d[1][2]))
    print('--- --- ---')
    print(' ' + str(board2d[2][0]) + ' | ' + str(board2d[2][1]) + ' | ' + str(board2d[2][2])) 
# This Function decides the symbols of player and the computer.
def userSymbol():
    letter = ''
    while not (letter == "X" or letter == "O" ):
        print()
        letter =input("Choose what you want to be (X or O)? : ").upper()
    if letter == "X":
        return ["X","O"] 
    else:
        return ["O","X"]

# This Function wil perform a toss & decide who will make the first move.
def firstMoveCheck():
    print()
    mainPlayer = eval(input(user+" Please choose 1 for heads & 2 for tails : "))
    if mainPlayer == 1:
        print(user," is Heads and Computer is Tails. SO LET'S TOSS: ")
    elif mainPlayer == 2:
        print(user," is Tails and Computer is Heads. SO LET'S TOSS: ")

    toss = random.randint(1,2)
    if toss==1 and mainPlayer ==1:
        print("It's HEADS & ","user", " You Won the Toss ")
        return 'player'
    elif toss==2  and  mainPlayer==2:
        print("It's TAILS & ","user", " You Won the Toss")
        return 'player'
    elif toss==2  and  mainPlayer==1:
        print("It's TAILS & ","Computer", " Won the Toss")
        return 'computer'
    elif toss==1 and  mainPlayer==2:
        print("It's HEADS & ","Computer", " Won the Toss ")
        return 'computer'
    
#This Function will make a move considering 3 things: (The board, The symbol and the specific Index).    
def makeMove(board , letter , move):

    board[move] = letter

def makeMove2D(board2D , letter , move):
    if move==1:
        board2D[0][0] = letter
    elif move==2:
        board2D[0][1]=letter
    elif move==3:
         board2D[0][2]=letter
    elif move==4:
         board2D[1][0]=letter
    elif move==5:
         board2D[1][1]=letter 
    elif move==6:
         board2D[1][2]=letter
    elif move==7:
         board2D[2][0]=letter
    elif move==8:
         board2D[2][1]=letter
    elif move==9:
         board2D[2][2]=letter


# This function returns True if that player has won.


def winnerCondition2D(board2D, letter): 
    return ((board2D[0][0] == letter and board2D[0][1] == letter and board2D[0][2] == letter) or 
    (board2D[1][0] == letter and board2D[1][1] == letter and board2D[1][2] == letter) or
    (board2D[2][0] == letter and board2D[2][1] == letter and board2D[2][2] == letter) or
    (board2D[0][0] == letter and board2D[1][0] == letter and board2D[2][0] == letter) or
    (board2D[0][1] == letter and board2D[1][1] == letter and board2D[2][1] == letter) or
    (board2D[0][2] == letter and board2D[1][2] == letter and board2D[2][2] == letter) or
    (board2D[0][0] == letter and board2D[1][1] == letter and board2D[2][2] == letter) or
    (board2D[2][0] == letter and board2D[1][1] == letter and board2D[0][2] == letter) )
#This Function will create an imaginary list (board). So computer can run game on that board and find it's perfect next move.

def boardCopy2D(board2D): 
    q = copy.deepcopy(board2D)
    return q
# dupeBoard = []
   # row,column=2,2
   # dupeBoard=[[' ' for i in range(3)]  for j in range(3)]
   
   # for i in board2D:
    #    for j in board2D:
     #       dupeBoard.append[i][j]
    #return dupeBoard

    

# Function to check if the specific box is occupied or not

def isSpaceFree2D(board2D, move):
    if move==1:
        return board2D[0][0]==' '
    elif move==2:
       return board2D[0][1]==' '
    elif move==3:
       return board2D[0][2]==' '
    elif move==4:
       return board2D[1][0]==' '
    elif move==5:
       return board2D[1][1]==' '
    elif move==6:
       return board2D[1][2]==' '
    elif move==7:
       return board2D[2][0]==' '
    elif move==8:
       return board2D[2][1]==' '
    elif move==9:
       return board2D[2][2]==' '
   
# This Function will return the box number choose by the player (After checking conditions).

def getPlayerMove2D(board2D):
    move = ' '
    while move not in [1,2,3,4,5,6,7,8,9] or not isSpaceFree2D(board2D, int(move)):
        print()
        move = int(input('Please enter your box number? (1-9): '))
        if move!=1  or move!=2  or move!=3  or move!=4  or move!=5  or move!=6  or move!=7  or move!=8  or move!=9:
            print("Enter correct move.")    
    return move

# This Function will create a list of possible moves and return a random number from that list.

def randomMoveFromList2D(board2D, movesList):
    possibleMoves = [] 
    for i in movesList:
        if isSpaceFree2D(board2D, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

# This function will run many conditions and find a best possibe move for computer.


def computerMove2D(board2D, computerSymbol):
    if computerSymbol == 'X':
        playerSymbol = 'O'
    else:
        playerSymbol = 'X'
        
    #Check for possible winning move of computer.   
    for i in range(1, 10):
        
        imaginaryBoard2D = boardCopy2D(board2D)
        if isSpaceFree2D(imaginaryBoard2D, i):
            makeMove2D(imaginaryBoard2D, computerSymbol, i)
            if winnerCondition2D(imaginaryBoard2D, computerSymbol):
                return i
            
    #Check for possible winning move of player to block opponents winning move       
    for i in range(1, 10):
        
        imaginaryBoard2D = boardCopy2D(board2D)
        if isSpaceFree2D(imaginaryBoard2D, i):
            makeMove2D(imaginaryBoard2D, playerSymbol, i)
            if winnerCondition2D(imaginaryBoard2D, playerSymbol):
                return i
    
    if main_Move == 1:
        move = randomMoveFromList2D(board2D, [5])
        if move != None:
            return move
        move = randomMoveFromList2D(board2D, [1])
        if move != None:
            return move
        move = randomMoveFromList2D(board2D, [3])
        if move != None:
            return move
        move = randomMoveFromList2D(board2D, [ 7])
        if move != None:
            return move
        move = randomMoveFromList2D(board2D, [9])
        if move != None:
            return move
        return randomMoveFromList2D(board2D, [2, 4, 6, 8])
    
    if main_Move == 2:
        if isSpaceFree2D(board2D, 5):
            move = randomMoveFromList2D(board2D, [5])
            if move != None:
                return move
        if super_Move == 1: 
            move = randomMoveFromList2D(board2D, [1])
            if move != None:
                return move
        if super_Move == 1: 
            move = randomMoveFromList2D(board2D, [3])
            if move != None:
                return move
        if super_Move == 1: 
            move = randomMoveFromList2D(board2D, [7])
            if move != None:
                return move
        if super_Move == 1: 
            move = randomMoveFromList2D(board2D, [9])
            if move != None:         
             return randomMoveFromList2D(board2D, [2, 4, 6, 8])
            
            return randomMoveFromList2D

        else:
            move = randomMoveFromList2D(board2D, [1, 3, 7, 9])
            if move != None:
                return move
            move = randomMoveFromList2D(board2D, [5])
            if move != None:
                return move
            move = randomMoveFromList2D(board2D, [2, 4, 6, 8])
            if move != None:
                return move


def superTrick2D(board2D):
    if isSpaceFree2D(board2D , 5):
        return 1
    else:
        return 0
    

#This Function will return TRUE if the game is TIE.

def isBoardFull2D(board2D):
    skip = 0 # Just to continue the condition
    tie = 0  # For draw
    for i in range(1, 10):
        
        if isSpaceFree2D(board2D, i):
            skip+=1
        else:
            tie+=1
    if tie == 9:
        return True
    else: 
        return False

# This function will ask you if you want to keep playing the game.
def playAgain():
    
    play2 = input("Do you want to play again? (yes or no): ").lower()
    if play2=='no':
        pass
    elif play2=='yes' or 'y':
        return play2

#Main game Crux to call all defined functions.

while True: #Main game loop
    row,column=2,2
    theBoard2D=[[' ' for i in range(3)]  for j in range(3)]
    #theBoard = [' ' for x in range(10)]
    playerSymbol, computerSymbol  = userSymbol()  
    turn = firstMoveCheck()
    print('The ' + turn + ' will go first.')
    main_Move =0
    counter = 0
    super_Move = 0
    if turn == "player":
        main_Move = 2
    elif turn == "computer":
        main_Move = 1
    while True:
        if turn == 'player':
        # Player's TURN  
          #  move = getPlayerMove(theBoard)
          #  print(theBoard)
           # print()
          
            move2D=getPlayerMove2D(theBoard2D)
            print(theBoard2D)
           # makeMove(theBoard, playerSymbol, move)
            makeMove2D(theBoard2D, playerSymbol, move2D)
            
            if winnerCondition2D(theBoard2D,playerSymbol):
                printBoard2D(theBoard2D)
                print(' Congrats',user,'! You have won the 2D game! :)')
                print(" ")
                break
            else:
                if isBoardFull2D(theBoard2D):
                    printBoard2D(theBoard2D)
                    print('The 2D game is DRAW! :|')
                    break
                else:
                    printBoard2D(theBoard2D)
                    print()
                    print()
                    turn = 'computer'
                    while counter !=1 :
                        if superTrick2D(theBoard2D) == 1:
                            super_Move = 1
                            counter+=1
                            break
                        else:
                            counter+=1
                            break
             # Computer's 2D TURN            
        else:
                
            move2D = computerMove2D(theBoard2D, computerSymbol)
            makeMove2D(theBoard2D, computerSymbol, move2D)
            print("   Computer's Move")
            print(" ")
                
            if winnerCondition2D(theBoard2D, computerSymbol):
                printBoard2D(theBoard2D)
                print('The computer has won the game! You lost. :(')
                print()
                break
            else:
                if isBoardFull2D(theBoard2D):
                    printBoard2D(theBoard2D)
                    print('The game is a tie! No more spaces left. :|')
                    break
                else:
                    printBoard2D(theBoard2D)
                    print()
                    print()
                    turn = 'player'
    if not playAgain():
        print()
        print('THANKS FOR PLAYING :)')
        break
            
 #       if winnerCondition(theBoard, playerSymbol):
  #          printBoard(theBoard)
  #          print(' Congrats',user,'! You have won the game! :)')
   #         print(" ")
    #        break
     #   else:
      #      if isBoardFull(theBoard):
       #         printBoard(theBoard)
        #        print('The game is DRAW! :|')
         #       break
          #  else:
           #     printBoard(theBoard)
            #    print()
             #   print()
             #   turn = 'computer'
              #  while counter !=1 :
               #     if superTrick(theBoard) == 1:
                #        super_Move = 1
                 #       counter+=1
              #          break
             #       else:
             #           counter+=1
             #           break
        
        # Computer's TURN            
       # else:
        #    move = computerMove(theBoard, computerSymbol)
         #   makeMove(theBoard, computerSymbol, move)
         #   print("   Computer's Move")
         #   print(" ")
                
          #  if winnerCondition(theBoard, computerSymbol):
          #      printBoard(theBoard)
          #      print('The computer has won the game! You lost. :(')
          #      print()
          #      break
          #  else:
          #      if isBoardFull(theBoard):
          #          printBoard(theBoard)
          #          print('The game is a tie! No more spaces left. :|')
          #          break
          #      else:
          #          printBoard(theBoard)
          #          print()
          #          print()
          #          turn = 'player'
  #  if not playAgain():
  #      print()
  #      print('THANKS FOR PLAYING :)')
  #      break
        


#END OF THE GAME
