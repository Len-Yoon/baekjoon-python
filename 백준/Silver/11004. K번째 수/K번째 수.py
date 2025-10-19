import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
k -= 1  # 0-index

lo, hi = 0, n - 1
while True:
    pivot = a[(lo + hi) // 2]  
    i, j = lo, hi
    
    while i <= j:
        while a[i] < pivot: i += 1
        while a[j] > pivot: j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1; j -= 1
    
    if k <= j:
        hi = j
    elif k >= i:
        lo = i
    else:
        print(a[k])
        break