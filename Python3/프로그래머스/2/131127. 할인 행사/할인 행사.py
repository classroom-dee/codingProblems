# frugal nerd's vain and desperate attempt prob
from collections import Counter
def solution(want, number, discount):
    shop = Counter({w:n for w, n in zip(want, number)})
    # sliding window
    l = sum(number)
    res = 0
    for i in range(len(discount)-l+1):
        res += shop == Counter(discount[i:i+l])
    return res