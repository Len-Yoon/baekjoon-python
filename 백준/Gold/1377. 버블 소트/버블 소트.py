import sys

input = sys.stdin.readline


num = int(input())
arr = []

for i in range(num):
    arr.append((int(input()),i))

max = 0
sorted_arr = sorted(arr)

for i in range(num):
    if max < sorted_arr[i][1]-i:
        max = sorted_arr[i][1]-i

print(max+1)