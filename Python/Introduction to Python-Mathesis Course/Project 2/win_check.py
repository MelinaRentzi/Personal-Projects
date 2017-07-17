def win_check(board,marker):
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or # across the top
            (board[4] == marker and board[5] == marker and board[6] == marker) or # across the middle
            (board[1] == marker and board[2] == marker and board[3] == marker) or # across the bottom
            (board[7] == marker and board[4] == marker and board[1] == marker) or # down the left side
            (board[8] == marker and board[5] == marker and board[2] == marker) or # down the middle
            (board[9] == marker and board[6] == marker and board[3] == marker) or # down the right side
            (board[7] == marker and board[5] == marker and board[3] == marker) or # diagonal
            (board[9] == marker and board[5] == marker and board[1] == marker)) # diagonal
