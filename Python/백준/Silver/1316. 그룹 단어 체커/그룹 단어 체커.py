n = int(input())
str_list = [input() for _ in range(n)]

def check(s, dic):
    prev = ''
    for c in s:
        # print(dic)
        if prev != c and dic.get(c, 0) != 0:
            return 0
        dic.setdefault(c, 0)
        dic[c] += 1
        prev = c
    return 1

group_count = 0
for line in str_list:
    s = line.strip()
    dic = {}
    group_count += check(s, dic)

print(group_count)