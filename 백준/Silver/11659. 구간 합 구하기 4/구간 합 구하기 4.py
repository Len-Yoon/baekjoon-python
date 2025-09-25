import sys
input = sys.stdin.readline

dataNum, questionNum = map(int,input().split())
numbers = list(map(int,input().split()))
sum = [0]
temp = 0

for i in numbers:
    temp += i
    sum.append(temp)

for i in range(questionNum):
    a, b = map(int, input().split())

    print(sum[b]-sum[a-1])
