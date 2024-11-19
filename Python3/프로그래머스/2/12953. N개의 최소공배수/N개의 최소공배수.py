# Least common shoobam problem
def solution(arr):
    arr = sorted(arr)
    n = arr.pop() # max
    i = 1
    while True:
        target = n * i
        if sum(map(lambda x: target % x == 0, arr)) == len(arr): # all True
            return target
        else:
            i += 1