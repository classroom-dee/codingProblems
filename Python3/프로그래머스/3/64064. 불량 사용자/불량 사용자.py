# UPDATE PYTHON VERSION ? GAWD 🫠
def solution(user_id: list, banned_id: list):
    import re
    cand = []
    for b in banned_id:
        rec = []
        for u in user_id:
            reg = re.compile("^" + re.escape(b).replace(r"\*", ".") + "$")
            if reg.fullmatch(u):
                rec.append(u)
        cand.append(rec)

    results = set()
    n = len(banned_id)

    # refilter and distribute
    # e.g., [['frodo', 'crodo'], ['frodo', 'crodo'], ...]
    # -> [['frodo'], ['crodo'], ...]
    def dfs(idx: int, chosen: set):
        # banned idx
        # chosen : chosen set of uids
        if idx == n:
            # dedupe frozenset, no order
            results.add(frozenset(chosen))
            return
        for u in cand[idx]:
            if u not in chosen:
                chosen.add(u)
                dfs(idx + 1, chosen)
                chosen.remove(u)

    dfs(0, set())
    # print(results)
    return len(results)
    
# cases = [
#     [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"], 2],
#     [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"], 2],
#     [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"], 3]
# ]

# for i, c in enumerate(cases):
#     [u, b, correct] = c
#     res = solution(u, b)
#     assert res == correct, f"test {i+1}: should be {correct}. res: {res}"