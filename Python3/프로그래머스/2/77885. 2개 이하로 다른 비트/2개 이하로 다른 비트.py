# bits prob sol 2
def solution(numbers):
    res = []
    for n in numbers:
        if n % 2 ==0:
            res.append(n + 1)
        else:
            # print(f'source dec: {n}, bin: {bin(n)} -> ', end=" ")
            mask = 1
            while n & mask:
                mask <<= 1
            t = n + mask
            # print(f'dec: {t}, bin: {bin(t)}', end=" ")
            diff = mask >> 1
            # print(f'diff: {diff}', end=" ")
            r = t - diff
            # print(f'result: {r}')
            res.append(r)
    return res