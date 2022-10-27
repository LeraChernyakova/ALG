#python

n, arr = int(input()), [int(i) for i in input().split()]
steps = []
for i in range(n // 2, -1, -1):
  while i < n:
    m, left, right = i, 2 * i + 1, 2 * i + 2
    if left < n and arr[left] < arr[m]:
        m = left
    if right < n and arr[right] < arr[m]:
        m = right
    if m == i:
        break
    steps += [[i, m]]
    arr[i], arr[m], i = arr[m], arr[i], m
print(len(steps))
for step in steps:
    print(*step)
