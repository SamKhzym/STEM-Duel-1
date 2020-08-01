import itertools

def draw_board(board):
    print(" " + str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]) + " \n" +
          "___________\n" +
          " " + str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]) + " \n" +
          "___________\n" +
          " " + str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]) + " \n")



"""
0 = no win
1 = x win
2 = o win
3 = tie
"""
def get_win(old_board):

    board = old_board.copy()

    for i in range(len(board)):
        if board[i] != "X" and board[i] != "O":
            board[i] = " "
    
    #Top row
    if board[0] == board[1] and board[1] == board[2]:
        if board[0] == "X": return 1
        elif board[0] == "O": return 2
    #Middle row
    if board[3] == board[4] and board[4] == board[5]:
        if board[3] == "X": return 1
        elif board[3] == "O": return 2
    #Bottom row
    if board[6] == board[7] and board[7] == board[8]:
        if board[6] == "X": return 1
        elif board[6] == "O": return 2
    #First Column
    if board[0] == board[3] and board[3] == board[6]:
        if board[0] == "X": return 1
        elif board[0] == "O": return 2
    #Second column
    if board[1] == board[4] and board[4] == board[7]:
        if board[1] == "X": return 1
        elif board[1] == "O": return 2
    #Third column
    if board[2] == board[5] and board[5] == board[8]:
        if board[2] == "X": return 1
        elif board[2] == "O": return 2
    #Diagonal left to right
    if board[0] == board[4] and board[4] == board[8]:
        if board[0] == "X": return 1
        elif board[0] == "O": return 2
    #Diagonal right to left
    if board[2] == board[4] and board[4] == board[6]:
        if board[2] == "X": return 1
        elif board[2] == "O": return 2
    #No win condition
    if " " in board: return 0
    return 3

def update_board(board, turn, counter):
    
    if counter % 2 == 0: board[turn] = "X"
    else: board[turn] = "O"

    return board

def main():
    print("WELCOME TO THE DEMO PROGRAM! I WISH ALL COMPETITORS GOOD LUCK.")

    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    done = False
    counter = 0
    
    while not done:
        draw_board(board)
        if counter % 2 == 0: print("X turn. Input a number between 1 and 9.")
        else: print("O turn. Input a number between 1 and 9.")

        turn_over = False
        while not turn_over:
            turn_over = False
            try:
                turn = int(input())
                if str(turn) in board:
                    board = update_board(board, turn-1, counter)
                    
                    win = get_win(board)
                    if win == 1:
                        print("X WINS!")
                        done = True
                    elif win == 2:
                        print("O WINS!")
                        done = True
                    elif win == 3:
                        print("GAME OVER, DRAW!")
                        done = True
                    else:
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    
                    turn_over = True
                    counter += 1
                else:
                    print("Invalid input.")
            except:
                print("Invalid input.")

if __name__ == "__main__": main()
