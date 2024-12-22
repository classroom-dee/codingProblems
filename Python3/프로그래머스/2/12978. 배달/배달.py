def solution(N, road, K):
    # init
    import heapq
    dists = [float('inf'), 0] + [float('inf')] * (N - 1) # -> [dummy, Node1=0, Node2=inf, Node3=inf... ...]
    q = []
    heapq.heappush(q, (1, 0)) # (node, dist)
    while q:
        curr_node, curr_dist = heapq.heappop(q)
        # CAN BE IMPROVED WITH A DICTIONARY
        # we WILL have moved this far if we continue on to dest ->
        for orig, dest, dist in road:
            next_dist = dist + curr_dist
            # check two flip cases (cuz the nodes are bi-directional)
            if orig == curr_node and next_dist < dists[dest]:
                dists[dest] = next_dist
                heapq.heappush(q, (dest, next_dist))
            elif dest == curr_node and next_dist < dists[orig]:
                dists[orig] = next_dist
                heapq.heappush(q, (orig, next_dist))
    return len([d for d in dists if d <= K])