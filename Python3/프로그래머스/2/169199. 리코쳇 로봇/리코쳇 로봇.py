# ricochet robot prob
from collections import deque
def solution(board):
    rows, cols = len(board), len(board[0])

    start, goal = None, None
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'R':
                start = (r, c)
            elif board[r][c] == 'G':
                goal = (r, c)
    # U D L R
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return search(board, start, goal, dirs, rows, cols)

def search(board, start, goal, dirs, rows, cols):
    q = deque([(start[0], start[1], 0)])
    records = set()
    records.add(start)
    while q:
        x, y, moves = q.popleft()
        if (x, y) == goal:
            return moves
        # 4 dirs
        for dx, dy in dirs:
            nx, ny = x, y # init
            # take steps
            while 0 <= nx + dx < rows and 0 <= ny + dy < cols and board[nx + dx][ny + dy] != 'D':
                nx += dx
                ny += dy
            if (nx, ny) not in records:
                records.add((nx, ny))
                q.append((nx, ny, moves + 1))
    return -1