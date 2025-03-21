def solution(players: list, m: int, k: int) -> int:
    """
    Good function
    """
    replicas = 0
    TIME = 24
    table = {t: [player, 0] for t, player in enumerate(players)}
    # print(f"capacity: {m}, up time limit: {k}")
    for t in range(TIME):
        n = table[t][0] // m
        # print(f"time: {t}, players: {table[t][0]}, currently running {table[t][1]} servers. need {n} servers.", end=" ")
        if n and table[t][1] < n:
            provision = n - table[t][1]
            # print(f"provisioning {provision} server.", end=" ")
            replicas += provision
            for up_time in range(t, t+k):
                if up_time < TIME:
                    table[up_time][1] += provision
        # print()
    return replicas