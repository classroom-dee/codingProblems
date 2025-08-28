def check_condition(arr: list, divisor: int):
    for num in arr:
        if num >= divisor and num % divisor == 0:
            return False
    else:
        return True

def solution(a1: list, a2: list):
    def _gcd(arr: list):
        import math
        from functools import reduce
        return reduce(math.gcd, arr)

    g1, g2 = _gcd(a1), _gcd(a2)
    is_a2_div_a1_indiv = check_condition(a1, g2)
    is_a2_indiv_a1_div = check_condition(a2, g1)
    
    if is_a2_div_a1_indiv and is_a2_indiv_a1_div:
        return max(g1, g2)
    elif is_a2_indiv_a1_div:
        return g1
    elif is_a2_div_a1_indiv:
        return g2
    else:
        return 0