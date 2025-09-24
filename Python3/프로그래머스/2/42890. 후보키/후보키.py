def solution(relation):
    from itertools import combinations

    n_rows = len(relation)
    n_cols = len(relation[0])
    cand_keys = []

    for r in range(1, n_cols + 1): # number of colums to combine
        for cols in combinations(range(n_cols), r): # column index combinations
            
            # minimality: skip if any known key is a subset of 'cols'
            # bc a composite key {A, B} cannot be minimal if {A} or {B} is already a key
            if any(set(k).issubset(cols) for k in cand_keys):
                continue

            # project rows onto the chosen columns
            projection = [tuple(row[c] for c in cols) for row in relation]

            # uniqueness
            if len(set(projection)) == n_rows:
                cand_keys.append(cols)

    return len(cand_keys)