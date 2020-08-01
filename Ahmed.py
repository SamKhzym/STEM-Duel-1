board = [" ", " ", " "," ", " ", " "," ", " ", " "]

def draw_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("_____")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("_____")
    print(board[6] + "|" + board[7] + "|" + board[8])

def get_win(board):
    winner = "N"
    while (winner == "N"):
        #check verticals
        winner = check(board[0], board[3], board[6])
        if winner != "N": break
        winner = check(board[1], board[4], board[7])
        if winner != "N": break
        winner = check(board[2], board[5], board[8])
        if winner != "N": break

        #check horizontal
        winner = check(board[0], board[1], board[2])
        if winner != "N": break
        winner = check(board[3], board[4], board[5])
        if winner != "N": break
        winner = check(board[6], board[7], board[8])
        if winner != "N": break

        #check diagonals
        winner = check(board[0], board[4], board[8])
        if winner != "N": break
        winner = check(board[2], board[4], board[6])
        if winner != "N": break
        break

    if winner == "X":
        return 1
    elif winner == "O":
        return 2
    else:
        if not " " in board:
            return 3
        return 0

def check(box1, box2, box3):
    if(box1 == box2 and box2 == box3):
        if box1 == "X":
            winner = "X"
            return "X"
        elif box1 == "O":
            winner = "O"
            return "O"
    else:
        return "N"

def make_move(player):
    while True:
        try:
            move = int(input("Player " + player + "'s turn. Enter a spot."))
        except:
            print("Wrong input. Please try a number from 1-9.")
            continue
        if move < 1 or move > 9:
            print("Wrong input. Please try a number from 1-9.")
            continue
        move -= 1
        if board[move] == " ":
            board[move] = player
            break
        elif board[move] != " ":
            print("Spot taken, try again.")
            continue
        # else:
        #     break

def main():
    winner = "N"

    while True:
        gameInPlay = True
        turn = "X"

        while gameInPlay:
            draw_board()
            if turn == "X":
                make_move("X")
                turn = "O"
            else:
                make_move("O")
                turn = "X"
        
            test = get_win(board)
            if test == 1 or test == 2 or test == 3:
                gameInPlay = False
        break

if __name__ == "__main__": main()
