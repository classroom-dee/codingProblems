def solution(arr1, arr2):
    n = len(arr1[0])
    n2 = len(arr2[0])
    res = []
    for k, r in enumerate(arr1):
        new_row = []
        for i in range(n2):
            new_dat = []
            for j in range(n):
                new_dat.append(r[j] * arr2[j][i])
            new_row.append(sum(new_dat))
        res.append(new_row)
    return res