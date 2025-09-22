# def solution(n, q, ans):
#     # Cartesian version
#     from itertools import combinations, product
    
#     DIGITS = 5
#     tree = [list(combinations(q[i], ans[i])) for i in range(len(q))]

#     all_possible = product(*tree)

#     res_set = set()
#     for ap in all_possible:
#         combined = set()
#         for e in ap:
#             combined.update(e)
#         if len(combined) == DIGITS:
#             res_set.add(frozenset(combined))
    
#     return res_set


# def solution(n, q, ans):
      # uhgghg back tracking
#     from itertools import combinations
#     DIGITS = 5
#     res_set = set()

#     def backtrack(index, current_set):
#         if index == len(q):
#             if len(current_set) == DIGITS:
#                 res_set.add(frozenset(current_set))
#             return

#         # Generate all combinations for this query
#         for comb in combinations(q[index], ans[index]):
#             # Only proceed if combining doesn't exceed DIGITS
#             if len(current_set | set(comb)) <= DIGITS:
#                 backtrack(index + 1, current_set | set(comb))

#     backtrack(0, set())
#     return res_set



def solution(n, q, ans):
    from itertools import combinations
    DIGITS = 5
    res_count = 0
    
    # Generate all possible shits
    for code in combinations(range(1, n+1), DIGITS):
        # Check against all guesses
        for guess, cnt in zip(q, ans):
            # count how many numbers in guess are in the pw
            if len(set(code) & set(guess)) != cnt:
                break
        else:
            res_count += 1
    
    return res_count

# tests = [
#     [10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]],
#     [15, [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]], [2, 1, 3, 0, 1]]
# ]
# for i, t in enumerate(tests):
#     res = solution(*t)
#     print(f'Test {i+1}, result: {res}')
#     print("--------------------------")

    
