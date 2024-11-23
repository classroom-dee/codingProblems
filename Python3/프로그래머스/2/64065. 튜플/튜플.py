# tuple prob
def solution(s):
    import re
    pre = s.strip("{}").split("},{")
    res = {}
    max = 0
    for p in pre:
        nums = re.findall(r'\d+', p)
        l = len(nums)
        if l > max: max = l
        res[l-1] = set(nums)
    res2 = set()
    f = []
    for i in range(max):
        tmp = res[i].difference(res2)
        res2.update(res[i].difference(res2))
        # print(i, tmp)
        f.append(int(tmp.pop()))
    return f