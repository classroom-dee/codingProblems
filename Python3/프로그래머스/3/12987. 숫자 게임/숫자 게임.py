def solution(A, B):
    A.sort(reverse=True) # 2 * n log n
    B.sort(reverse=True)
    score = 0
    
    while B:
        if B[-1] > A[-1]:
            B.pop()
            A.pop()
            score += 1
        elif B[-1] <= A[-1]: # else
            B.pop()
            
    return score