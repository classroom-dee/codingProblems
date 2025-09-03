from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    SCALE = 2
    MAX = 51 * SCALE # 50 limit
    grid = [[0] * (MAX + 1) for _ in range(MAX + 1)]

    # border as 1, interior as 2
    for x1, y1, x2, y2 in rectangle:
        x1 *= SCALE; y1 *= SCALE; x2 *= SCALE; y2 *= SCALE
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x in (x1, x2) or y in (y1, y2):
                    if grid[x][y] != 2: # don't overwrite interior
                        grid[x][y] = 1 # border
                else:
                    grid[x][y] = 2 # interior

    # Remove interiors, keep border cells
    for x in range(MAX + 1):
        for y in range(MAX + 1):
            if grid[x][y] == 2:
                grid[x][y] = 0

    # BFS over border cells
    sx, sy = characterX * SCALE, characterY * SCALE
    tx, ty = itemX * SCALE, itemY * SCALE
    q = deque([(sx, sy, 0)])
    visited = set([(sx, sy)])
    for_pop = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        x, y, d = q.popleft()
        if (x, y) == (tx, ty):
            return d // SCALE  # scale back
        for dx, dy in for_pop:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= MAX and 0 <= ny <= MAX and grid[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny, d + 1))

    return "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"