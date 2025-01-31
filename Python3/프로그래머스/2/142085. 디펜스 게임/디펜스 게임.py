import heapq
def solution(n, k, enemy):
    mx_heap = []
    fallen = 0
    skipped = 0
    defended = 0

    for i, wave in enumerate(enemy):
        fallen += wave
        heapq.heappush(mx_heap, -wave) # flip the min heap
        if fallen > n:
            if skipped < k:
                # backtracking stupid mistakes 😛
                largest = -heapq.heappop(mx_heap)
                fallen -= largest
                skipped += 1
                # print(f'used skip at wave {wave}')
            else:
                # have no force nor the passes
                break
        defended += 1
        # print(f'on wave {wave}, fallen: {fallen}, heap stat: {mx_heap}')
    return defended