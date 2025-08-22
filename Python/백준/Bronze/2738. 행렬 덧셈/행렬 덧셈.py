n, m = input().split()
n, m = int(n), int(m)

mat1 = []
for i in range(n):
    row = input().split()
    temp_row = []
    for j in range(m):
        temp_row.append(int(row[j]))
    mat1.append(temp_row)
    
for i in range(n):
    row = input().split()
    for j in range(m):
        mat1[i][j] += int(row[j])

for row in mat1:
    print(''.join(f"{num} " for num in row).rstrip())

