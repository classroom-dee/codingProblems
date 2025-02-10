# def solution(k, d):
#    cnt = 0
#    for x in range(d + 1):
#        for y in range(d + 1):
#            if (x * k) ** 2 + (y * k) ** 2 <= d ** 2:
#                cnt += 1
#            else:
#                break
#    return cnt
import math
def solution(k, d):
    cnt = 0
    for x in range(0, d // k + 1):
        max_y = math.isqrt(d**2 - (x * k)**2) // k
        cnt += (max_y + 1)
    return cnt
