## METHOD 1
# def solution(numbers):
#     l = len(numbers)
#     res = sortdem(numbers, l)
#     return ''.join(res)
# def sortdem(numbers, length, res=[]):
#     for i in range(length):
#         for j in range(i, length):
#             s_curr, s_prev = str(numbers[j]), str(numbers[i])
#             if int(s_curr[0]) > int(s_prev[0]):
#                 numbers[i] = s_curr
#                 numbers[j] = s_prev
#             elif int(s_curr[0]) == int(s_prev[0]):
#                 if int(s_curr + s_prev) > int(s_prev + s_curr):
#                     numbers[i] = s_curr
#                     numbers[j] = s_prev
#                 else:
#                     numbers[i] = s_prev
#                     numbers[j] = s_curr
#     return numbers  
## METHOD 2
from functools import cmp_to_key
def solution(numbers):
    stringified = list(map(str, numbers))
    def comp(a, b):
        if a + b > b + a: return -1
        elif b + a > a + b: return 1
        else: return 0
    new_nums = sorted(stringified, key=cmp_to_key(comp))
    res = ''.join(new_nums)
    if res[0] == '0': return '0'
    return res