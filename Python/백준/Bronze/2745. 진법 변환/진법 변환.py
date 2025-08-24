a_ord = ord('A')
n, b = input().split()

b = int(b)

def digit_reducer(namba: str):
    return int(namba) if namba.isdigit() else ord(namba) - a_ord + 10

total = 0
digits = len(n)
for i in range(digits):
    total += (b ** i) * digit_reducer(n[-1-i])

print(total)