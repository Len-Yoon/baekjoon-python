import sys
input = sys.stdin.readline

n = int(input()) # 재료의 갯수
m = int(input()) # 번호의 합
arr = list(map(int, input().split())) #재료들

arr.sort()
count = 0

i = 0 # 시작 인덱스
j = n - 1 # 종료 인덱스

while i < j:
    if arr[i] + arr[j] < m:
        i += 1
    elif arr[i] + arr[j] > m:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1

print(count)
