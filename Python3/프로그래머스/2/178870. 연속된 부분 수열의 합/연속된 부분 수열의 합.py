# def solution(seq, k):
#     l = len(seq)
#     res = 0
#     for i in range(l):
#         res = search(k, l, seq, i+1)
#         # if i == 5: break # temp break
#         if res[0] != 0:
#             break
#     return res[1]
# def search(target, s_len, seq, length, idx=0):
#     for i, _ in enumerate(seq):
#         # print(i, seq[i:i+length]
#         s = sum(seq[i:i+length])
#         if s == target:
#             return s, [i, i+length-1]
#         if i + length >= s_len: break
#     # print('-----function ends----')
#     return 0, []
def solution(seq, k):
    m_len = float('inf')
    res = []
    curr = 0
    init = 0
    # ]]]] [[ ]]
    for tail in range(len(seq)):
        curr += seq[tail]
        # print(f'\nTail: {tail}, current sum: {curr}', end=" ")
        # if curr < k: print(f'{curr} < k --> skipping loop', end=" ") # test
        while curr >= k:
            if curr == k:
                # print(f'\n// Sum {curr} == k -->', end=" ")
                if tail - init + 1 < m_len: # len check
                    m_len = tail - init + 1
                    res = [init, tail]
                    # print(f"candidate: {res}", end=" ")
            # else: print(f'\n// Sum {curr} > k --> skip extraction:', end=" ") # test
            # print(f'sum({curr}) = sum({curr}) - elem({seq[init]}), m_len:{m_len}, start from {init} + 1', end=" ")
            curr -= seq[init]
            init += 1
    return res