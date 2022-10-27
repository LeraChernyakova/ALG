import bisect

size, n = map(int, input().split())
ends = []

for i in range(n):
    arrival, duration = map(int, input().split())
    del ends[0:bisect.bisect(ends, arrival)]
    if len(ends) < size:
        begin = max(ends[-1], arrival) if ends else arrival
        print(begin)
        ends.append(begin + duration)
    else:
        print(-1)