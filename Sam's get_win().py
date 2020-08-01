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
