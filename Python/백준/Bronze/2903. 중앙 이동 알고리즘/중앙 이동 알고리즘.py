n = int(input())

dots = 2

for i in range(n):
    dots += dots - 1

print(dots ** 2)