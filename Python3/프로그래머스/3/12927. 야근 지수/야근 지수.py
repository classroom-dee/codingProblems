import heapq
def solution(n, works):

    mx_heap = []
    fatigue = 0
    for w in works:
        heapq.heappush(mx_heap, -w)

        fatigue += w**2

    for _ in range(n):
        stressige_arbeit = -heapq.heappop(mx_heap)
        if stressige_arbeit < 1:
            break

        fatigue -= stressige_arbeit ** 2
        stressige_arbeit -= 1
        fatigue += stressige_arbeit ** 2
        heapq.heappush(mx_heap, -stressige_arbeit)


    return fatigue