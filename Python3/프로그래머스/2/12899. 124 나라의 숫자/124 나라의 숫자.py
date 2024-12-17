def solution(n):
    nums = ['1', '2', '4']
    l = len(nums)
    res = []
    while n > 0:
        n -= 1
        res.append(nums[n % l])
        n //= l
    # res = lesgo(n, nums)
    return ''.join(res[::-1])
    # return int(res[-1])
# def lesgo(n, nums, i=0, res=[]):
#     # print(f'i:{i}, res:{res}')
#     if i < len(nums):
#         res.append(nums[i])
#         i += 1
#         return lesgo(n, nums, i, res)
#     else:
#         if i == n: return res
#         else:
#             tmp = []
#             for k in nums:
#                 for r in res:
#                     tmp.append(k+r)
#                     i += 1
#                     if i == n: return tmp
#             res = lesgo(n, nums, i, tmp)
#             return res