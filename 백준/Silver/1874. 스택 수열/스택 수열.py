import sys

input = sys.stdin.readline

n = int(input())
stack = []
answer = []
flag = 0
result = True
cur = 1

for i in range(n):
    num = int(input())
    while cur <= num:          # 입력한 수를 만날 때 까지 오름차순으로 push
        stack.append(cur)
        answer.append('+')
        cur += 1

    if stack[-1] == num:       # 스택의 top이 입력한 숫자와 같다면 스택 top 꺼내 수열 만들어줌
        stack.pop()
        answer.append('-')

    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)
