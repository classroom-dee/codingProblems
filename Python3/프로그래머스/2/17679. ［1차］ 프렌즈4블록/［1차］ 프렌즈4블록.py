def solution(m, n, board): # 2 <= n, m <= 30
    board = [list(ppl) for ppl in board]
    cnt = 0
    # idx = 0 # for test
    rec = set()
    while True:
        for i in range(m):
            for j in range(n):
                if i + 1 < m and j + 1 < n:
                    if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != '#':
                        rec.add((i, j))
                        rec.add((i+1, j))
                        rec.add((i, j+1))
                        rec.add((i+1, j+1))
        # print(rec)
        if not rec: break
        for r in sorted(rec, key=lambda x: x[0]):
            for i in range(r[0], 0, -1):
                board[i][r[1]] = board[i-1][r[1]]
                if i == 1:
                    board[i-1][r[1]] = '#'
            cnt += 1
        # test
        # for b in board:
        #     print(b)
        rec = set()
        # idx += 1
        # if idx == 2: break # for test
    return cnt