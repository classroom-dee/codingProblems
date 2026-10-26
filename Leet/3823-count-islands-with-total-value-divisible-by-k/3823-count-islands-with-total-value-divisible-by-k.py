class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] != 0 and (i, j) not in visited:
                    uwu = [(i, j)]
                    total = 0

                    while uwu:
                        curr_r, curr_c = uwu.pop()

                        # Check boundaries first
                        if (curr_r < 0 or curr_c < 0 or
                            curr_r >= len(grid) or
                            curr_c >= len(grid[0])):
                            continue

                        # Skip visited cells and 0
                        if (curr_r, curr_c) in visited:
                            continue
                        if grid[curr_r][curr_c] == 0:
                            continue

                        visited.add((curr_r, curr_c))

                        # Add this cell's value to the island sum
                        total += grid[curr_r][curr_c]

                        for r, c in dirs:
                            uwu.append((curr_r + r, curr_c + c))

                    # Finished exploring one entire island
                    if total % k == 0:
                        count += 1

        return count