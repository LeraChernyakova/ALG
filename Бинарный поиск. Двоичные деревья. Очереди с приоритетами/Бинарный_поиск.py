import decimal

def solve(L, x):
    first = 0
    last = len(L)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if abs(L[mid] - x) < 0.00001:
            index = mid
        else:
            if x < L[mid]:
                last = mid -1
            else:
                first = mid +1
    return index
