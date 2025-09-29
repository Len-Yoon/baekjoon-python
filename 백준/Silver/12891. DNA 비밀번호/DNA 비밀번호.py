# 투 포인터
import sys

input = sys.stdin.readline

S, P = map(int, input().split())
st = input()
min_count = list(map(int, input().split()))

answer = 0

s = 0
e = P

check = [0] * 4
check[0] = st[s: e].count('A')
check[1] = st[s: e].count('C')
check[2] = st[s: e].count('G')
check[3] = st[s: e].count('T')

while (True):
    answer += 1
    for i in range(4):
        if (min_count[i] > check[i]):
            answer -= 1
            break

    if (e >= S):
        break

    if (st[s] == 'A'):
        check[0] -= 1
    elif (st[s] == 'C'):
        check[1] -= 1
    elif (st[s] == 'G'):
        check[2] -= 1
    elif (st[s] == 'T'):
        check[3] -= 1
    s += 1

    if (st[e] == 'A'):
        check[0] += 1
    elif (st[e] == 'C'):
        check[1] += 1
    elif (st[e] == 'G'):
        check[2] += 1
    elif (st[e] == 'T'):
        check[3] += 1
    e += 1

print(answer)