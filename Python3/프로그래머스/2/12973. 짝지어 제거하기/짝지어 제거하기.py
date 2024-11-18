# paired elimination prob
# def solution(s):
#     prev = ''
#     i = 0
#     while s:
#         if i >= len(s): break
#         c = s[i]
#         if c == prev:
#             s = ''.join(s.split(f'{c}{c}'))
#             # print(s)
#             i = 0
#             prev = ''
#         else:
#             prev = c
#             i += 1
#     return 1 if len(s) == 0 else 0

# using stack
def solution(s):
    track = []
    for c in s:
        # end to end compare
        if track and track[-1] == c:
            track.pop()
        else:
            track.append(c)
        # print(track)
    return 1 if not track else 0