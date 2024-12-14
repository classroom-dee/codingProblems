from collections import defaultdict, deque
def solution(n, wires):
    def search(start, connection):
        visited = set()
        dq = deque([start])
        visited.add(start)
        while dq:
            pylon = dq.popleft()
            for next in connection[pylon]:
                if next not in visited:
                    visited.add(next)
                    dq.append(next)
        return len(visited)
    
    min_df = float('inf') # min comparison
    for i in range(len(wires)):
        # I need {1:[2,3,4,5], 2:[3,4,5,6] ...}
        connection = defaultdict(list)
        for j in range(len(wires)):
            # excluding the cut
            if i != j:
                # build
                p1, p2 = wires[j]
                connection[p1].append(p2)
                connection[p2].append(p1)
        group1 = search(wires[i][0], connection)
        group2 = n - group1
        min_df = min(min_df, abs(group1 - group2))
    return min_df