def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} |{board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} |{board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} |{board[8]}")
    print("\n")
def check_winner(board,player):
    win_condition = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
        ]
    for condition in win_condition:
        if board[condition[0]] ==  board[condition[1]] == board[condition[2]] == player:    return True
    return False
def check_draw(board):
    return " " not in board
def tic_tac_toe():
    board = [" "]*9
    current_player = "X"
    print("wellcome to tic tac toe !")
    print("position are odered ! through top 9 [top left to bottom right]")
    print(" 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 ")
    while True:
        print_board(board)
        try:
            choice = int(input(f"player {current_player} 's turn. choose position (1-):"))
            if choice < 0 or choice >8:
                print("invaid input ! please choose a number between 1 to 9 .")
                continue
            if board[choice] != " ":
                print("that position already taken ! try another one .")
                continue
        except ValueError:
            print("invalid input ! please enter valid number. ")
            continue
        board[choice] = current_player
        if check_winner(board, current_player):
            prpint_board(board)
            print(f"congratulation ! player {current_player} wins !")
            break
        if check_draw(board):
            print_board(board)
            print(" it's a DRAW")
            break
        current_player = "0" if current_player == "X" else "x"
if __name__=="__main__":
    tic_tac_toe()
    
        
