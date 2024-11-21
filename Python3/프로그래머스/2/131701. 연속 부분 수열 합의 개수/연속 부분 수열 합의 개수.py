# partial consecutive sequence combination prob
def solution(elem):
    sums = set()
    for i in range(1, len(elem)+1): # subseq len
        for start in range(len(elem)): # subseq start idx
            partial = []
            if i + start > len(elem):
                partial = elem[start:start + i] + elem[:abs(len(elem) - (i + start))]
            else:
                partial = elem[start:start + i]
            # print(partial)
            sums.add(sum(partial))
    return len(sums)