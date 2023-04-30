import random
T_T_T = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

you = input("Welcome to tic-tac-toe, you take X or O:?  ").upper()
if you == 'X':
    comp = "0"
if you == '0':
    comp = "X"
print("You take:",you,"and","Computer takes:",comp)

winner = None
PlayGame = True

def printBoard(T_T_T):
    print(T_T_T [0] + " | " + T_T_T [1] + " | " + T_T_T [2])
    print(T_T_T [3] + " | " + T_T_T [4] + " | " + T_T_T [5])
    print(T_T_T [6] + " | " + T_T_T [7] + " | " + T_T_T [8])

def playerInput(T_T_T):
    inp = int(input("Select a spot 1-9: "))
    if T_T_T [inp-1] == "-":
        T_T_T [inp-1] = you    

def match(T_T_T ):
    global winner
    if T_T_T [0] == T_T_T [1] == T_T_T [2] and T_T_T [0] != "-":
        winner = T_T_T [0]
        return True
    elif T_T_T [3] == T_T_T [4] == T_T_T [5] and T_T_T [3] != "-":
        winner = T_T_T [3]
        return True
    elif T_T_T [6] == T_T_T [7] == T_T_T [8] and T_T_T [6] != "-":
        winner = T_T_T [6]
        return True
    elif T_T_T [0] == T_T_T [3] == T_T_T [6] and T_T_T [0] != "-":
        winner = T_T_T [0]
        return True
    elif T_T_T [1] == T_T_T [4] == T_T_T [7] and T_T_T [1] != "-":
        winner = T_T_T [1]
        return True
    elif T_T_T [2] == T_T_T [5] == T_T_T [8] and T_T_T [2] != "-":
        winner = T_T_T [2]
        return True
    elif T_T_T [0] == T_T_T [4] == T_T_T [8] and T_T_T [0] != "-":
        winner = T_T_T [0]
        return True
    elif T_T_T [2] == T_T_T [4] == T_T_T [6] and T_T_T [4] != "-":
        winner = T_T_T [2]
        return True

def forWin(T_T_T ):
    global PlayGame
    if match(T_T_T):
        printBoard(T_T_T)
        print(f"Congratulations! The winner is {winner}!")
        PlayGame = False

def forTie(T_T_T ):
    global PlayGame
    if "-" not in T_T_T :
        printBoard(T_T_T)
        print("The game tie!")
        PlayGame = False

def switchPlayer():
    global you
    global comp
    if you == "X":
        comp = "0"
    elif you =="0":
        comp="X"

def computer(T_T_T):     
    global comp    
    if comp == "0":
        position = random.randint(0, 8)
        if T_T_T [position] == "-":
            T_T_T [position] = "0"
            switchPlayer()
    elif comp == "X":
        position = random.randint(0, 8)
        if T_T_T [position] == "-":
            T_T_T [position] = "X"
            switchPlayer()

while PlayGame:
    printBoard(T_T_T )
    playerInput(T_T_T )
    switchPlayer()
    computer(T_T_T )
    forWin(T_T_T )
    forTie(T_T_T )