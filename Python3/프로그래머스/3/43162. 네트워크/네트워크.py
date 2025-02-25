def solution(n, compuuta):
    visited = set()

    # dfs: do effing shit
    def search(node):
        for neighbor in range(n):
            # connected and not dupe
            if compuuta[node][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                search(neighbor) # 코드멀미난다 🤢

    cnt = 0
    for node in range(n):
        if node not in visited:
            # 고립된거는 세지 마라구우우우우우 
            # node 기준 연결과 다른 node 기준 연결 체크 ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ
            if sum(compuuta[node]) > 1 or any(compuuta[other][node] for other in range(n)): # node 고정이니 O(n)
                visited.add(node)
                search(node)
                cnt += 1 # 찾앗다요넘

    return cnt