a, b = map(int, input().split())

seq = [a, b]

while len(seq) < 10:
    next_num = (seq[-1] + seq[-2]) % 10
    seq.append(next_num)

for num in seq:
    print(num, end=" ")