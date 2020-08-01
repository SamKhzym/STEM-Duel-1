import itertools, pdb, Shaw, Ahmed

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
def get_win(board):
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

def check_turn_order(order, check_type):

    board = [" "," "," "," "," "," "," "," "," "]
    
    for i in range(len(order)):
        if i % 2 == 0: board[order[i]] = "X"
        else: board[order[i]] = "O"

    if check_type == "generate": return get_win(board)
    elif check_type == "test": return Ahmed.get_win(board)



def turn_order_get_win(order, check_type):
    
    for i in range(5,10,1):
        result = check_turn_order(order[0:i], check_type)
        if result != 0: return result

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

def main():
    all_board_states = list(itertools.permutations([0,1,2,3,4,5,6,7,8], 9))
    all_results = []
    win = True
    
    for perm in all_board_states:
        result = turn_order_get_win(perm, "generate")
        all_results.append([perm, result])

    print("Combinations generated.")

    counter = 0

    for result in all_results:
        new_res = turn_order_get_win(result[0], "test")
        if counter % 1000 == 0: print(counter)
        counter += 1
        if result[1] != new_res:
            print("TEST FAIL: SEED " + str(result[0]))
            print("EXPECTED: " + str(result[1]) + ", GOT: " + str(new_res))
            print()
            win = False
            break

    if win: print("ALL TESTS PASSED! CONGRTULATIONS, WINNER!!!")

if __name__ == "__main__": main()
