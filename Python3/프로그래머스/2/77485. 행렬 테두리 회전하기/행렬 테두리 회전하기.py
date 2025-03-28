from typing import List
def solution(rows: int, cols: int, queries: List[List[int]]) -> List[int]:
    # init mat
    n = 1
    mat = []
    for r in range(rows):
        tmp_col = []
        for c in range(cols):
            tmp_col.append(n)
            n += 1
        mat.append(tmp_col)

    # to indexes
    queries = list(map(lambda x: list(map(lambda y: y - 1, x)), queries))

    # min
    res = []

    # rotate
    for query in queries:
        top_left, bottom_right = (query[0], query[1]), (query[2], query[3])
        curr = mat[top_left[0]][top_left[1]]
        smallest = float("inf") # 24 bytes, 10000 = 28 bytes

        # top
        c = top_left[1]
        while c < bottom_right[1]:
            smallest = min(smallest, curr)
            next = mat[top_left[0]][c+1]
            mat[top_left[0]][c+1] = curr
            curr = next
            c += 1
        
        # right
        r = top_left[0]
        while r < bottom_right[0]:
            smallest = min(smallest, curr)
            next = mat[r+1][bottom_right[1]]
            mat[r+1][bottom_right[1]] = curr
            curr = next
            r += 1

        # bottom
        c = bottom_right[1]
        while c > top_left[1]:
            smallest = min(smallest, curr)
            next = mat[bottom_right[0]][c-1]
            mat[bottom_right[0]][c-1] = curr
            curr = next
            c -= 1

        # left
        r = bottom_right[0]
        while r > top_left[0]:
            smallest = min(smallest, curr)
            next = mat[r-1][top_left[1]]
            mat[r-1][top_left[1]] = curr
            curr = next
            r -= 1

        res.append(smallest)
    return res