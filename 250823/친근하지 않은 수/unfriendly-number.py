n = int(input())

count = 0

for i in range(n):
    if not((i % 2 == 0) or (i % 3 == 0) or (i % 5 == 0)):
        count += 1
    continue
print(count)