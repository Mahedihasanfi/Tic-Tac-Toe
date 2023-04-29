def sign():
    you = input("Welcome to tic-tac-toe, you take X or O:?  ")
    if you == 'X':
        comp = '0'
    elif you == '0':
        comp = 'X'
    else:
        print("Invalid input!")
    print("you:",you)
    print("comp:",comp)   
    
position = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
position= ["-", "-", "-", "-", "-", "-","-", "-", "-"]
def print_position():
    print(position[0] + " | " + position[1] + " | " + position[2])
    print(position[3] + " | " + position[4] + " | " + position[5])
    print(position[6] + " | " + position[7] + " | " + position[8])

sign()
print_position()