# def solution(maps):
#     landmass = [set()]
#     for i, row in enumerate(maps):
#         for j, prov in enumerate(row):
#             connection = False
#             for l in landmass:
#                 if maps[i][j] != "X":
#                     if not l or (i + 1, j) in l or (i - 1, j) in l or (i, j + 1) in l or (i, j - 1) in l:
#                         l.add((i, j))
#                         connection = True
#             if not connection and maps[i][j] != "X":
#                 landmass.append(set(((i, j),)))
#     if not landmass[0]: return [-1]
#     else:
#         return sorted(list(map(lambda x: sum(int(maps[coord[0]][coord[1]]) for coord in x), landmass)))
def solution(maps):
    landmasses = []
    rec = set()
    def search(x, y):
        stk = [(x, y)]
        tot = 0
        while stk:
            i, j = stk.pop()
            if (i, j) in rec or maps[i][j] == "X": continue
            rec.add((i, j))
            tot += int(maps[i][j])
            for c_i, c_j in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= c_i < len(maps) and 0 <= c_j < len(maps[0]) and (c_i, c_j) not in rec:
                    stk.append((c_i, c_j))
        return tot
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and (i, j) not in rec:
                landmasses.append(search(i, j))
    return sorted(landmasses) if landmasses else [-1]