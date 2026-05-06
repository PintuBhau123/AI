board = [" " for _ in range(9)]
def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
]
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

def play():
    player = "X"
    
    for turn in range(9):
        print_board()
        move = int(input(f"Player {player}, enter position (1-9): ")) - 1
        
        if board[move] == " ":
            board[move] = player
            
            if check_winner(player):
                print_board()
                print(f"Player {player} wins!")
                return
            player = "O" if player == "X" else "X"
        else:
            print("Invalid move! Try again.")
    print_board()
    print("It's a draw!")

play()
print("Jayant75")