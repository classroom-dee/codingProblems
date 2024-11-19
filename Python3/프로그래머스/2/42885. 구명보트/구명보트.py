# life boat problem
## Optimized
def solution(people, limit):
    people.sort()
    head, tail = 0, len(people) - 1
    rescued = 0
    while head <= tail:
        if people[head] + people[tail] <= limit:
            head += 1
        tail -= 1
        rescued += 1
    return rescued
## Bloated code
# def solution(people, limit):
#     from collections import Counter
#     cnt = Counter(people)
#     weights = sorted(set(people))
#     rescued = 0
#     for w in weights:
#         while cnt[w] > 0:
#             candidates = list(filter(lambda x: x <= limit - w, weights))
#             if candidates:
#                 candidates = sorted(candidates, reverse=True)
#                 for i in range(len(candidates)):
#                     if cnt[candidates[i]] > 0:
#                         cnt[candidates[i]] -= 1
#                         break
#             cnt[w] -= 1
#             rescued += 1
#     return rescued