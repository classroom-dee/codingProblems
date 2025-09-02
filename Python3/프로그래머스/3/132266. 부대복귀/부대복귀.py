from collections import deque

def solution(n, roads, sources, destination):
    # 1-based neighbor graph
    graph = [[] for _ in range(n + 1)]
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    # BFS from the destination
    dist = [-1] * (n + 1)  # default -1
    dist[destination] = 0
    q = deque([destination])

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:  # not visited yet
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)

    return [dist[s] for s in sources]