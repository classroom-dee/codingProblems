# Old
# from itertools import chain

# def solution(begin: int, end: int):
#     get_factors = lambda n: sorted(set(chain.from_iterable((i, n // i) for i in range(1, int(n**0.5) + 1) if n % i == 0)))
#     res = []
#     for i in range(begin, end+1):
#         factors = get_factors(i)
#         big = 0
#         if len(factors) > 2:
#             big = factors[-2] # biggest factor that is not self
#         elif len(factors) == 2:
#             big = 1 # if it's a prime number, use 1 -> blind spot
        
#         res.append(big)
    
#     return res

# New: float sqrt can be off by 1 for very large n -> use isqrt
# from math import isqrt

# def solution(begin: int, end: int):
#     res = []
#     for n in range(begin, end + 1):
#         if n == 1:
#             res.append(0)
#             continue
#         big = 1  # default for primes
#         r = isqrt(n)
#         for d in range(2, r + 1):
#             if n % d == 0:
#                 big = n // d  # largest proper divisor
#                 break
#         res.append(big)
#     return res

# UGghghghg
def solution(begin, end):
    MAX_BLOCK = 10_000_000
    result = []
    
    for i in range(begin, end + 1):
        if i == 1:
            result.append(0)
            continue
        
        block = 1  # default
        # check divisors up to sqrt(i)
        for d in range(2, int(i**0.5) + 1):
            if i % d == 0:
                pair = i // d
                if pair <= MAX_BLOCK:
                    block = max(block, pair)
                    break  # pair is always larger, so best
                elif d <= MAX_BLOCK:
                    block = max(block, d)
        result.append(block)
    
    return result