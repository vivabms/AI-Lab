board = [" "] * 9
player = "X"

for turn in range(9):
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

    pos = int(input("Player " + player + " (1-9): ")) - 1
    if board[pos] != " ":
        print("Taken! Try again.")
        continue
    board[pos] = player

    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    won = False
    for a, b, c in wins:
        if board[a] == player and board[b] == player and board[c] == player:
            won = True

    if won:
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print("Player " + player + " wins")
        break

    player = "O" if player == "X" else "X"
else:
    print("Draw match")




# Output:

# Player X (1-9): 1
# X    
     
     
# Player O (1-9): 5
# X    
#   O  
     
# Player X (1-9): 9
# X    
#   O  
#     X
# Player O (1-9): 8
# X    
#   O  
#   O X
# Player X (1-9): 2
# X X  
#   O  
#   O X
# Player O (1-9): 3
# X X O
#   O  
#   O X
# Player X (1-9): 7
# X X O
#   O  
# X O X
# Player O (1-9): 4
# X X O
# O O  
# X O X
# Player X (1-9): 6
# Game over
