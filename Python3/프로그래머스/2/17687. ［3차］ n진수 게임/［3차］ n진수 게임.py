from collections import deque
def convert(dec, base):
    if dec == 0: 
        return deque("0")
    dig = deque()
    while dec:
        rem = dec % base
        if rem < 10:
            dig.appendleft(str(rem))
        else:
            dig.appendleft(chr(rem - 10 + ord('A')))
        dec //= base
    return dig
def solution(n, t, m, p):
    nums_len = 0
    decimal_to_convert = 0
    decimal_to_n_base = convert(decimal_to_convert, n)
    who = 0
    nums = ""
    while nums_len < t:
        while decimal_to_n_base:
            target = decimal_to_n_base.popleft()
            if who % m == p - 1:
                # print(f"who: {who}")
                nums += target
                nums_len += 1
                if nums_len >= t: 
                    break
            who += 1
        decimal_to_convert += 1
        decimal_to_n_base = deque(convert(decimal_to_convert, n))
    return nums