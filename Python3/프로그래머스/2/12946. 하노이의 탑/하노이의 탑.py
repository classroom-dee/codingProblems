# The tower of Hanoi
def solution(n):
    res = search(n, 1, 3, 2)
    return res

def search(n, orig, dest, buff, movs=None):
    if movs is None:
        movs = []
    if n == 1:
        movs.append([orig, dest])
        return movs
    else:
        search(n-1, orig, buff, dest, movs)
        movs.append([orig, dest])
        search(n-1, buff, dest, orig, movs)
    return movs

# a = solution(3)
# print(a)