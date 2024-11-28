import heapq
def solution(scoville, K):
    l = len(scoville)
    heapq.heapify(scoville)
    i = 0
    while True:
        # print(i, end=" ")
        one = heapq.heappop(scoville)
        if one >= K: return i
        if len(scoville) < 1: return -1
        two = heapq.heappop(scoville)
        heapq.heappush(scoville, one + (two * 2))
        i += 1