num = int(input())
numbers = list(map(int, input().split()))

maxScore = max(numbers)

for i in range(num):
    numbers[i] = numbers[i]/maxScore*100

print(sum(numbers)/num)