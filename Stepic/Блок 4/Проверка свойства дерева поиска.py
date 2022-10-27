import sys


def dfs(r):
    if r != -1:
        yield from dfs(tree[r][1])
        yield tree[r][0]
        yield from dfs(tree[r][2])


sys.setrecursionlimit(100000)
tree = [tuple(map(int, input().split())) for _ in range(int(input()))]
if tree:
    gen = dfs(0)
    prev = next(gen)
    for curr in gen:
        if curr < prev:
            print('INCORRECT')
            exit()
        prev = curr
print('CORRECT')