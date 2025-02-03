def solution(board):
    rows, cols = len(board), len(board[0])
    # init dp list
    landfill = [[0] * cols for _ in range(rows)]
    max_len = 0

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                # (0, *) or (*, 0)
                if i == 0 or j == 0:
                    landfill[i][j] = 1
                else:
                    # dp update
                    landfill[i][j] = min(landfill[i-1][j], landfill[i][j-1], landfill[i-1][j-1]) + 1
                max_len = max(max_len, landfill[i][j])
            # print(f'result:')
            # for l in landfill:
                # print(l)
    return max_len * max_len