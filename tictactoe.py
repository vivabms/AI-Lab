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