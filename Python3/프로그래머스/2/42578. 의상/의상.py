# 착용하거나 해야합니다 & shitty paragraph problem learn korean first
from collections import Counter
def solution(clothes):
    cnts_dic = Counter(tp for _, tp in clothes)
    cnts = cnts_dic.values()
    arr = [1] + [0] * len(cnts)
    for cnt in cnts:
        for i in range(len(arr) - 1, 0, -1):
            # print(f'arr{arr}, arr[{i}]({arr[i]}) += arr[{i-1}]({arr[i-1]}) * cnt({cnt})', end=" ")
            arr[i] += arr[i - 1] * cnt
            # print(f'-> arr{arr}')
    return sum(arr[1:])