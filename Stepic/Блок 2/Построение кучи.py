n = int(input())
A = [int(x) for x in input().split()]
S = []


def sift_down(i):
    max_index = i
    left = 2 * i + 1
    if left < n and A[left] < A[max_index]:
        max_index = left
    right = 2 * i + 2
    if right < n and A[right] < A[max_index]:
        max_index = right
    if i != max_index:
        A[i], A[max_index] = A[max_index], A[i]
        S.append((i, max_index))
        sift_down(max_index)


for k in range((n - 1) // 2, -1, -1):
    sift_down(k)

print(len(S))
for x in S:
    print(*x)