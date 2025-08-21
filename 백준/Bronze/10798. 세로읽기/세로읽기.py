mat = [input() for _ in range(5)]

longest_row = len(max(mat, key=lambda x: len(x)))
final = ''
for i in range(longest_row):
    for j in range(5):
        if i < len(mat[j]):
            final += mat[j][i]

print(final)