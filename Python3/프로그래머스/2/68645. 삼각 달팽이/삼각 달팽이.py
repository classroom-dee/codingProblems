# from collections import deque
# def solution(n):
#     init = n
#     res = []
#     start = 1
#     shells = []
#     while n >= 1:
#         # get each shell's start - end
#         first = start
#         last = first + n * 3 - 4
#         if n == 1:
#             shells.append(deque([start]))
#         else:
#             # convert them to queues
#             shells.append(deque(range(first, last + 1)))
#         start = last + 1
#         n -= 3
#     # pop and append
#     for i in range(init):
#         # print(shells)
#         if i == 0:
#             res.append(shells[i].popleft())
#         elif i == init - 1:
#             for j in range(init):
#                 res.append(shells[0].popleft())
#         else:
#             shell_depth = i + 1
#             # print(f'depth: {shell_depth}')
#             for j in range(shell_depth // 2):
#                 res.append(shells[j].popleft())
#             if shell_depth % 2 != 0:
#                 middle = shell_depth // 2 + 1
#                 res.append(shells[middle - 1].popleft())
#             for j in range(shell_depth // 2 - 1, -1, -1):
#                 res.append(shells[j].pop())
#         # print(res)
#     return res
# snail shell sol 2
def solution(n):
    grid = [[0] * (i + 1) for i in range(n)]
    num = 1
    start_x, start_y = -1, 0
    for layer_size in range(n, 0, -3):
        # down
        for _ in range(layer_size):
            start_x += 1
            grid[start_x][start_y] = num
            num += 1
        # right
        for _ in range(layer_size - 1):
            start_y += 1
            grid[start_x][start_y] = num
            num += 1
        # up
        for _ in range(layer_size - 2):
            start_x -= 1
            start_y -= 1
            grid[start_x][start_y] = num
            num += 1
    # flatten 
    res = [num for row in grid for num in row]
    return res