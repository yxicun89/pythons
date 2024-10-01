def show_othello_result(s:str) -> list[int]:
    board = "bw"
    count=0
    for i in S:
        if i == "L":
            if count % 2 == 0:
               board = "b" +board
            else:
               board = "w" +board
        else:
            if count % 2 == 0:
               board += "b"
            else:
               board += "w"

        if board[0] == "b" and board[0] ==board[-1]:
           board = "b" * len(board)
        elif board[0] == "w" and board[0] ==board[-1]:
           board = "w" * len(board)
        
        
        count += 1

    return [board.count("b"),board.count("w")]

S=input()
result = show_othello_result(S)
print(result)
