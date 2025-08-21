def covered_area(squares):
    """
    Exact union area (in square units) 
    covered by axis-aligned 10×10 squares
    inside a 100×100 board, integer coordinates:
    Cell-count method
    """
    covered = set()
    for x, y in squares:
        # clamp to the 100×100 board
        x0 = max(0, min(100, x))
        y0 = max(0, min(100, y))
        x1 = max(0, min(100, x0 + 10))
        y1 = max(0, min(100, y0 + 10))
        # cellcount: size 1 for each
        for i in range(x0, x1):
            for j in range(y0, y1):
                covered.add((i, j))
    return len(covered)  

n_squares = int(input())
squares = [tuple(map(lambda x: int(x), input().split())) for _ in range(n_squares)]
print(covered_area(squares))