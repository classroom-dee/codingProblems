# 2 by 1 rectangle fitting prob
# from math import factorial as fac
def solution(n):
    # prob = 0
    # for fits_one in range(n+1):
    #     if (n - fits_one) % 2 != 0: continue
    #     fits_two = (n - fits_one) // 2
    #     # print(fits_one, fits_two)
    #     if fits_one < 0: continue
    #     if fits_two == 0 or fits_one == 0:
    #         # print("adding 1")
    #         prob += 1
    #         continue
    #     symm = min(fits_two, n - fits_two)
    #     comb = 1
    #     for i in range(symm):
    #         comb = comb * (fits_one + fits_two - i) // (i + 1)
    #     prob += comb
    #     prob %= 1000000007
    #     # prob += fac(fits_one + fits_two) // (fac(fits_one) * fac(fits_two))
    # return prob
    if n == 1: return 1
    rec = [0] * (n + 1)
    rec[0], rec[1] = 1, 1
    for i in range(2, n + 1):
        rec[i] = (rec[i - 1] + rec[i - 2]) % 1000000007
    return rec[-1]