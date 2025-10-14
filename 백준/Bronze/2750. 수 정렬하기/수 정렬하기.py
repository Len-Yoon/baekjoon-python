import sys

input = sys.stdin.readline


num = int(input())

arr = [0] * num

for i in range(num):
    arr[i] = int(input())

for i in range(num-1):
    for j in range(num-1-i):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

for i in arr:
    print(i)
