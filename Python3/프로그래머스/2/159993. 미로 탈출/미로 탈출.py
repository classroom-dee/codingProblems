from collections import deque
def solution(maps):
    # init positions
    width, height = len(maps[0]), len(maps)
    start, lever, goal = None, None, None
    for i in range(height):
        for j in range(width):
            if maps[i][j] == 'S': start = (i, j)
            elif maps[i][j] == 'L': lever = (i, j) 
            elif maps[i][j] == 'E': goal = (i, j)
    
    # path to lever
    lever_time = search(start, maps, width, height, lever)
    if lever_time == -1: return -1

    # path to goal
    goal_time = search(lever, maps, width, height, goal)
    if goal_time == -1: return -1

    return lever_time + goal_time

def search(start, maps, width, height, target):
    dq = deque([(start[0], start[1], 0)]) # coord, time, lever stat
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rec = set([(start[0], start[1])])
    
    while dq:
        t_x, t_y, time = dq.popleft()

        # exit check
        if (t_x, t_y) == target: return time
        
        # traverse
        for dir in dirs:
            vec_x, vec_y = t_x + dir[0], t_y + dir[1]
            if 0 <= vec_x < height and 0 <= vec_y < width:
                if maps[vec_x][vec_y] != 'X':
                    if (vec_x, vec_y) not in rec:
                        rec.add((vec_x, vec_y))
                        dq.append((vec_x, vec_y, time + 1))
    return -1