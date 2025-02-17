def solution(name):
    n = len(name)
    moves = 0

    # Vertical moves (changing each character)
    for char in name:
        moves += min(ord(char) - ord('A'), 26 - (ord(char) - ord('A')))

    # Finding the optimal horizontal moves
    min_moves = n - 1  # Worst case: move right all the way

    for i in range(n):
        next_index = i + 1
        # Find the next position that is not 'A'
        while next_index < n and name[next_index] == 'A':
            next_index += 1

        # Option 1: Move right then backtrack left
        right_then_left = i + (i + (n - next_index))

        # Option 2: Move left first then right
        left_then_right = (n - next_index) + (n - next_index + i)

        # Update min_moves
        min_moves = min(min_moves, right_then_left, left_then_right)

    return moves + min_moves
