import sys

input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
result = []
result.append(arr[0])

for i in range(1, n):
    result.append(arr[i] + result[i-1])

print(sum(result))